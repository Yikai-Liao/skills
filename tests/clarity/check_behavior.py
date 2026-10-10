"""Maintainer-only behavior checks; never include this file in solver input.

Usage: python tests/clarity/check_behavior.py catalog /path/to/catalog.py
Uses only the standard library. Passing checks says nothing about readability.
"""

import argparse
import csv
import importlib.util
import itertools
from pathlib import Path
import sys
import unittest

sys.dont_write_bytecode = True


class RecordingStore:
    def __init__(self, failure=None):
        self.calls = []
        self.failure = failure

    def replace(self, items):
        self.calls.append(list(items))
        if self.failure is not None:
            raise self.failure


class CatalogChecks(unittest.TestCase):
    def test_empty_input_commits_once(self):
        for text in ("", "sku,price_cents\n"):
            with self.subTest(text=text):
                store = RecordingStore()
                self.assertEqual(candidate.import_catalog(text, store), 0)
                self.assertEqual(store.calls, [[]])

    def test_valid_rows_keep_order_and_csv_quoting(self):
        store = RecordingStore()
        count = candidate.import_catalog('sku,price_cents\n B ,20\n"A,C",0\n', store)
        self.assertEqual(count, 2)
        self.assertEqual(store.calls, [[("B", 20), ("A,C", 0)]])

    def test_bad_rows_do_not_commit_and_keep_error(self):
        cases = [
            ("sku,price_cents\n ,2\n", ValueError, ("empty sku",)),
            ("sku,price_cents\nA,1\n A ,2\n", ValueError, ("duplicate sku",)),
            ("sku,price_cents\nA,-1\n", ValueError, ("negative price",)),
            ("sku,price_cents\nA,nope\n", ValueError, ("invalid literal for int() with base 10: 'nope'",)),
            ("price_cents\n1\n", KeyError, ("sku",)),
            ("sku\nA\n", KeyError, ("price_cents",)),
            ("sku,price_cents\rA,1\r", csv.Error, ("new-line character seen in unquoted field - do you need to open the file with newline=''?",)),
        ]
        for text, error_type, error_args in cases:
            with self.subTest(text=text):
                store = RecordingStore()
                with self.assertRaises(error_type) as caught:
                    candidate.import_catalog(text, store)
                self.assertIs(type(caught.exception), error_type)
                self.assertEqual(caught.exception.args, error_args)
                self.assertEqual(store.calls, [])

    def test_missing_cell_keeps_builtin_failure(self):
        try:
            int(None)
        except TypeError as error:
            expected_args = error.args
        store = RecordingStore()
        with self.assertRaises(TypeError) as caught:
            candidate.import_catalog("sku,price_cents\nA\n", store)
        self.assertEqual(caught.exception.args, expected_args)
        self.assertEqual(store.calls, [])

    def test_first_error_wins_without_partial_commit(self):
        cases = [
            ("sku,price_cents\nA,1\n A ,nope\n", "duplicate sku"),
            ("sku,price_cents\n ,nope\n", "empty sku"),
            ("sku,price_cents\nA,-1\nA,2\n", "negative price"),
        ]
        for text, message in cases:
            with self.subTest(text=text):
                store = RecordingStore()
                with self.assertRaises(ValueError) as caught:
                    candidate.import_catalog(text, store)
                self.assertEqual(caught.exception.args, (message,))
                self.assertEqual(store.calls, [])

    def test_store_failure_propagates_same_object(self):
        failure = OSError("disk unavailable")
        store = RecordingStore(failure)
        with self.assertRaises(OSError) as caught:
            candidate.import_catalog("sku,price_cents\nA,1\n", store)
        self.assertIs(caught.exception, failure)
        self.assertEqual(store.calls, [[("A", 1)]])


class RecordingService:
    def __init__(self, outcomes, fail_at=None):
        self.outcomes = outcomes
        self.fail_at = fail_at
        self.failure = OSError("service unavailable")
        self.calls = []
        self.result = object()

    def call(self, name, request):
        self.calls.append((name, request))
        if name == self.fail_at:
            raise self.failure
        return self.outcomes[name] if name != "commit" else self.result

    def authenticated(self, request):
        return self.call("auth", request)

    def has_quota(self, request):
        return self.call("quota", request)

    def valid_input(self, request):
        return self.call("validate", request)

    def commit(self, request):
        return self.call("commit", request)


class WorkflowChecks(unittest.TestCase):
    def test_all_check_combinations_preserve_first_error_and_call_order(self):
        names = ("auth", "quota", "validate")
        errors = (PermissionError("unauthorized"), RuntimeError("quota exceeded"), ValueError("invalid input"))
        for flags in itertools.product((False, True), repeat=3):
            with self.subTest(flags=flags):
                request = object()
                service = RecordingService(dict(zip(names, flags)))
                if all(flags):
                    self.assertIs(candidate.submit(request, service), service.result)
                    expected_names = [*names, "commit"]
                else:
                    first = flags.index(False)
                    expected = errors[first]
                    with self.assertRaises(type(expected)) as caught:
                        candidate.submit(request, service)
                    self.assertIs(type(caught.exception), type(expected))
                    self.assertEqual(caught.exception.args, expected.args)
                    expected_names = list(names[:first + 1])
                self.assertEqual(service.calls, [(name, request) for name in expected_names])

    def test_each_service_failure_propagates_without_retry(self):
        names = ("auth", "quota", "validate", "commit")
        for index, name in enumerate(names):
            with self.subTest(name=name):
                request = object()
                service = RecordingService(dict.fromkeys(names, True), fail_at=name)
                with self.assertRaises(OSError) as caught:
                    candidate.submit(request, service)
                self.assertIs(caught.exception, service.failure)
                self.assertEqual(service.calls, [(n, request) for n in names[:index + 1]])


class ParserChecks(unittest.TestCase):
    def test_regular_delimiters_and_empty_fields(self):
        for text, expected in [("", [""]), (",", ["", ""]), ("a,,b,", ["a", "", "b", ""]), ("猫,λ", ["猫", "λ"])]:
            with self.subTest(text=text):
                self.assertEqual(candidate.split_escaped(text), expected)

    def test_escapes_do_not_become_delimiters(self):
        for text, expected in [(r"a\,b,c", ["a,b", "c"]), (r"a\\,b", ["a\\", "b"]), (r"\n,\t", ["\n", "\t"]), (r"\u002c,\u03bb", [",", "λ"]), (r"\u0041\u0042,\uFfFe", ["AB", "\ufffe"])]:
            with self.subTest(text=text):
                self.assertEqual(candidate.split_escaped(text), expected)

    def test_malformed_escapes_keep_errors(self):
        cases = [("a\\", "dangling escape"), (r"\q", "unknown escape"), (r"\u1", "incomplete unicode escape"), (r"\u12,G", "invalid unicode escape"), (r"\uD800", "surrogate escape"), (r"\uDFFF", "surrogate escape")]
        for text, message in cases:
            with self.subTest(text=text):
                with self.assertRaises(ValueError) as caught:
                    candidate.split_escaped(text)
                self.assertEqual(caught.exception.args, (message,))

    def test_long_input_preserves_transition_order(self):
        self.assertEqual(candidate.split_escaped((r"x\,y,\u0041," * 1000)), ["x,y", "A"] * 1000 + [""])


class InlineChecks(unittest.TestCase):
    def test_names_preserve_order_and_duplicates(self):
        self.assertEqual(candidate.item_names({"items": [{"name": "B"}, {"name": "A"}, {"name": "B"}]}), ["B", "A", "B"])
        self.assertEqual(candidate.item_names({"items": []}), [])

    def test_missing_keys_still_raise(self):
        for payload, key in [({}, "items"), ({"items": [{}]}, "name")]:
            with self.subTest(payload=payload):
                with self.assertRaises(KeyError) as caught:
                    candidate.item_names(payload)
                self.assertEqual(caught.exception.args, (key,))


if __name__ == "__main__":
    checks = {"catalog": CatalogChecks, "workflow": WorkflowChecks, "parser": ParserChecks, "inline": InlineChecks}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=checks)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    # Solver source is expected to be ordinary trusted task code, not a sandbox.
    spec = importlib.util.spec_from_file_location("candidate", args.source.resolve())
    candidate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(candidate)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(checks[args.case])
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
