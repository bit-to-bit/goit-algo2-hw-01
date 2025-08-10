import random

def quick_select(arr, k):
    if not 1 <= k <= len(arr):
        raise ValueError("k must be between 1 and the length of the array")

    def partition(left, right, pivot_index):
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left

        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1

        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    def select(left, right, k_smallest):
        if left == right:
            return arr[left]

        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)

        elif k_smallest > pivot_index:
            return select(pivot_index + 1, right, k_smallest)

        else:
            return arr[pivot_index]

    return select(0, len(arr) - 1, k - 1)
