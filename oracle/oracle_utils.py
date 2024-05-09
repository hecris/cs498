class Dictionary(dict):
    def update(self, k, v):
        """Update the value of a key if it exists in the dictionary."""
        if k in self:
            self[k] = v


def bubble_up(arr, i, element_to_index_map=Dictionary()):
    """Assumes i is not the last element, since we can't bubble up the last element."""
    assert i < len(arr) - 1
    j = i + 1
    swaps = 0
    while arr[i] != i:
        # Search for next unfrozen element
        while arr[j] == j:
            j += 1
        # Swap elements
        arr[i], arr[j] = arr[j], arr[i]
        element_to_index_map.update(arr[i], i)
        element_to_index_map.update(arr[j], j)
        # Increment `swaps` if we swapped different indices.
        if i != j:
            swaps += 1
        # Update `i` to the index we swapped to, and `j` to right after that.
        i = j
        j = i + 1
    return swaps


def bubble_down(arr, i, element_to_index_map=Dictionary()):
    """Assumes i is not the first element, since we can't bubble up the first element."""
    assert i > 0
    j = i - 1
    swaps = 0
    while arr[i] != i:
        # Search for next unfrozen element
        while arr[j] == j:
            j -= 1
        # Swap elements
        arr[i], arr[j] = arr[j], arr[i]
        element_to_index_map.update(arr[i], i)
        element_to_index_map.update(arr[j], j)
        # Increment `swaps` if we swapped different indices.
        if i != j:
            swaps += 1
        # Update `i` to the index we swapped to, and `j` to right before that.
        i = j
        j = i - 1
    return swaps


def get_before_elements(arr):
    return Dictionary({x: i for i, x in enumerate(arr) if x > i})


def get_after_elements(arr):
    return Dictionary({x: i for i, x in enumerate(arr) if x < i})


if __name__ == '__main__':
    a = [1, 0]
    print(get_before_elements(a))
    bubble_up(a, 0)
    print(a)
