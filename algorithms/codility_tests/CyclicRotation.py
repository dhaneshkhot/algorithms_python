
class CyclicRotation:
    def __init__(self):
        self

    def cyclic_rotate_array(self, arr, n):
        arr_len = len(arr)
        if arr_len == 0 | arr_len == 1:
            return arr
        for i in range(n):
            lastItem = arr[arr_len-1]
            for j in range(arr_len):
                arr[arr_len-(j+1)] = arr[arr_len-(j+2)]
                if arr_len-(j+2) == 0:
                    break
            arr[0] = lastItem
        return arr


