import oracle_utils


def blind_selection_sort(arr):
    swaps = 0
    for i in range(len(arr)):
        if arr[i] == i:
            continue
        j = i + 1
        while not arr[i] == i:
            if arr[j] != j:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
            j += 1

    assert arr == sorted(arr)
    return swaps


def blind_selection_sort_reversed(arr):
    swaps = 0
    for i in reversed(range(len(arr))):
        if arr[i] == i:
            continue
        j = i - 1
        while not arr[i] == i:
            if arr[j] != j:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
            j -= 1

    assert arr == sorted(arr)
    return swaps


def blind_selection_sort_oracle(arr):
    element_to_index_map = oracle_utils.get_after_elements(arr)
    swaps = 0
    while element_to_index_map:
        smallest_element = min(element_to_index_map)
        idx = element_to_index_map[smallest_element]
        swaps += oracle_utils.bubble_down(arr, idx, element_to_index_map)
        element_to_index_map.pop(smallest_element)
    assert arr == sorted(arr)
    return swaps


def blind_selection_sort_reversed_oracle(arr):
    element_to_index_map = oracle_utils.get_before_elements(arr)
    swaps = 0
    while element_to_index_map:
        smallest_element = max(element_to_index_map)
        idx = element_to_index_map[smallest_element]
        swaps += oracle_utils.bubble_up(arr, idx, element_to_index_map)
        element_to_index_map.pop(smallest_element)
    assert arr == sorted(arr)
    return swaps
