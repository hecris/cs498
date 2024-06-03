import collections
import itertools


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


def bubble_down(arr, i, element_to_index_map=Dictionary(), swap_counter=collections.defaultdict(int)):
    """Assumes i is not the first element, since we can't bubble up the first element."""
    assert i > 0
    j = i - 1
    swaps = 0
    while arr[i] != i:
        # Search for next unfrozen element
        while arr[j] == j:
            j -= 1
        # Swap elements
        swap_counter[arr[j]] += 1
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
    """Returns a map of elements that are before their position to their index."""
    return Dictionary({x: i for i, x in enumerate(arr) if x > i})


def get_after_elements(arr):
    """Returns a map of elements that are after their position to their index."""
    return Dictionary({x: i for i, x in enumerate(arr) if x < i})


def sort_given_order(arr, order, swap_counter=collections.defaultdict(int)):
    """Bubbles down elements after their position in the specified order."""
    swaps = 0
    element_to_index_map = get_after_elements(arr)
    for x in order:
        idx = element_to_index_map[x]
        swaps += bubble_down(arr,
                             idx, element_to_index_map, swap_counter)
        element_to_index_map.pop(x)
    assert arr == sorted(arr)
    return swaps


def get_best_order(arr):
    """Gets the order of bubbling down that results in the most swaps."""
    element_to_index_map = get_after_elements(arr)
    elements = list(element_to_index_map.keys())
    return min(sort_given_order(list(arr), order) for order in itertools.permutations(elements))


def get_worst_order(arr):
    """Gets the order of bubbling down that results in the least swaps."""
    element_to_index_map = get_after_elements(arr)
    elements = list(element_to_index_map.keys())
    return max(sort_given_order(list(arr), order) for order in itertools.permutations(elements))


if __name__ == '__main__':
    a = [1, 0]
    print(get_before_elements(a))
    bubble_up(a, 0)
    print(a)
