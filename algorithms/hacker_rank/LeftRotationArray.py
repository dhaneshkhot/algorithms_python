class LeftRotation:

    def left_rotation_by_value(self, arr, n, d):
        arr_len = n
        if arr_len == 0 | arr_len == 1:
            return arr

        for i in range(d):
            first_item = arr[0]
            for j in range(arr_len):
                arr[j] = arr[j + 1]

                if j + 1 == arr_len - 1:
                    break
            arr[arr_len - 1] = first_item
        return " ".join(map(lambda x: str(x), arr))

    def left_rotation_by_index(self, arr, d):
        return " ".join(map(lambda x: str(x), (arr[d:] + arr[:d])))

