def get_extremum(left, right) -> tuple:
    return (min(left[0], right[0]), max(left[1], right[1]))


def get_min_max(arr) -> tuple:

    if len(arr) == 0:
        return (None, None)

    if len(arr) == 1:
        return (arr[0], arr[0])

    mid = len(arr) // 2
    left = get_min_max(arr[:mid])
    right = get_min_max(arr[mid:])

    return get_extremum(left, right)
