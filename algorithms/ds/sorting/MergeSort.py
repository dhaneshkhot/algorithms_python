#  Avg: O(n log2n) (This is best worst case for sorting algorithm)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        # print("left")
        # print(left)
        # print("right")
        # print(right)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


if __name__ == '__main__':
    myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merge_sort(myList))
