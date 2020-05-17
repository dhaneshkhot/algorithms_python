from random import randint


# Avg: O(n log2n) (This is best worst case for sorting algorithm)
# worst-case scenario is theoretically O(n2) when the pivot is the smallest or largest value of the array
def quick_sort(arr):
    if len(arr) < 2:
        return arr

    left, match, right = [], [], []

    pivot = arr[randint(0, len(arr) - 1)]

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            match.append(i)
        else:
            right.append(i)

    return quick_sort(left)+match+quick_sort(right)


if __name__ == '__main__':
    myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(quick_sort(myList))
