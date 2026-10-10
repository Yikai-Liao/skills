def _get_items(payload):
    return payload["items"]


def item_names(payload):
    return [item["name"] for item in _get_items(payload)]
