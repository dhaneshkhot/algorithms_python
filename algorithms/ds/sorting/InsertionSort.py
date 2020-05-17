#  O(n^2)
def insertion_sort(arr):
    for i in range(1, len(arr)):  # starts from 1st element
        element = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > element:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = element

    return arr
