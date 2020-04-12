class MinimumSwaps2:

    def get_minimum_swaps_to_sort_array(self, arr):
        # get original values and its indexes in a dictionary
        value_index_dict = {value: index for index, value in enumerate(arr)}
        swaps = 0
        for i in range(len(arr)):
            actual_value, expected_value = arr[i], i + 1

            if actual_value != expected_value:
                expected_value_index = value_index_dict[expected_value]

                arr[i] = expected_value
                arr[expected_value_index] = actual_value

                # Update the index in the dictionary after a swap
                value_index_dict[actual_value] = expected_value_index
                value_index_dict[expected_value] = i
                swaps += 1
        return swaps

    def get_minimum_swaps_to_sort_array_2(self, arr):
        swaps = 0
        i = 0
        while i < len(arr) - 1:
            if arr[i] != i + 1:
                tmp = arr[i]
                arr[i], arr[tmp - 1] = arr[tmp - 1], arr[i]
                swaps += 1
            else:
                i += 1
        return swaps

#  [7, 1, 3, 2, 4, 5, 6]
