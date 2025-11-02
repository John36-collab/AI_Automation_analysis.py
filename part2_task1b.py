# Copilot version: Sort a list of dictionaries by a given key

def sort_dict_list(items, key, reverse=False, in_place=False):
    """
    Sorts a list of dictionaries by a specific key.
    Uses Python's built-in sorted() or list.sort() for efficiency.
    """
    get_key = lambda x: x[key]

    if in_place:
        items.sort(key=get_key, reverse=reverse)
        return items
    return sorted(items, key=get_key, reverse=reverse)

# --- Example Test ---
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

print("Copilot (ascending):", sort_dict_list(data, "age"))
print("Copilot (descending):", sort_dict_list(data, "age", reverse=True))
