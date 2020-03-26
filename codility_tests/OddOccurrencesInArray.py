class OddOccurrencesInArray:
    def __init__(self):
        self

    # Detected time complexity O(N**2)
    def odd_occurances_in_array(self, arr):
        checked = set([])
        arr_len = len(arr)

        odd_no_count = 0
        found_odd_no = -1

        for i in range(arr_len):
            if checked.__contains__(arr[i]):
                continue
            odd_no_count += 1
            checked.add(arr[i])
            j = i + 1
            while j < arr_len:
                if arr[j] == arr[i]:
                    odd_no_count += 1
                j += 1
            if odd_no_count % 2 != 0:
                found_odd_no = arr[i]
                break

        return found_odd_no

    # Detected time complexity O(N) or O(N*log(N))
    def odd_occurances_in_array_2(self, arr):
        checked = {}
        arr_len = len(arr)

        found_odd_no = -1

        for i in range(arr_len):
            if arr[i] not in checked:
                checked[arr[i]] = 1
            else:
                count = checked[arr[i]] + 1
                checked[arr[i]] = count

        for key, value in checked.items():
            if value % 2 != 0:
                found_odd_no = key
                break

        return found_odd_no
