from quick_select import quick_select
from min_max import get_min_max

if __name__ == "__main__":

    k = 3
    test = [
        [3, 5, 7, 8, 55, 77, 2, 5, 1, 0, 888, 19, 9, 34, 56, 2, 6, 77, 53],
        [55, 76, 53, 49, -4, 0, 0, 0, 1, 3, 13],
        [],
    ]

    for i, arr in enumerate(test):
        print(f"\nTest case {i}:")
        print(f"arr = {arr}")
        print(f"get_min_max = {get_min_max(arr)}")
        try:
            print(f"quick_select = {quick_select(arr,k)}")
        except Exception as e:
            print(f"quick_select = {e}")
