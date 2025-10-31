# Manual version: custom bubble sort to mimic sorting behavior

def manual_sort_dict_list(items, key, reverse=False, in_place=False):
    """
    A manual implementation of sorting dictionaries by key.
    Uses bubble sort (O(n^2)) for demonstration.
    """
    data = items if in_place else items.copy()
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if reverse:
                if data[j][key] < data[j + 1][key]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:
                if data[j][key] > data[j + 1][key]:
                    data[j], data[j + 1] = data[j + 1], data[j]
    return data

# --- Example Test ---
data2 = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

print("Manual (ascending):", manual_sort_dict_list(data2, "age"))
print("Manual (descending):", manual_sort_dict_list(data2, "age", reverse=True))
