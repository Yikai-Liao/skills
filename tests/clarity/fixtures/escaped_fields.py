"""A single-pass parser whose state transitions are audited together."""


def split_escaped(text):
    """Split unescaped commas; decode \\, \\\\, \\n, \\t and \\uXXXX escapes.

    Empty fields are kept. Unicode escapes require four hexadecimal digits;
    surrogate code points are rejected. Raw non-ASCII characters are retained.
    Error messages are part of the existing public contract.
    """
    parts = []
    current = []
    escaped = False
    unicode_digits_left = 0
    code_point = 0

    for char in text:
        if unicode_digits_left:
            if "0" <= char <= "9":
                digit = ord(char) - ord("0")
            elif "a" <= char <= "f":
                digit = ord(char) - ord("a") + 10
            elif "A" <= char <= "F":
                digit = ord(char) - ord("A") + 10
            else:
                raise ValueError("invalid unicode escape")
            code_point = code_point * 16 + digit
            unicode_digits_left -= 1
            if unicode_digits_left == 0:
                if 0xD800 <= code_point <= 0xDFFF:
                    raise ValueError("surrogate escape")
                current.append(chr(code_point))
            continue

        if escaped:
            escaped = False
            if char == "u":
                unicode_digits_left = 4
                code_point = 0
            elif char == "n":
                current.append("\n")
            elif char == "t":
                current.append("\t")
            elif char == "\\" or char == ",":
                current.append(char)
            else:
                raise ValueError("unknown escape")
            continue

        if char == "\\":
            escaped = True
        elif char == ",":
            parts.append("".join(current))
            current.clear()
        else:
            current.append(char)

    if unicode_digits_left:
        raise ValueError("incomplete unicode escape")
    if escaped:
        raise ValueError("dangling escape")
    parts.append("".join(current))
    return parts
