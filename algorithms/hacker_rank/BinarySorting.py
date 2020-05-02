class BinarySorting:
    def rearrange(self, elements):
        original_arr = elements
        arr_len = len(elements)
        binary_values = ["{:04b}".format(i) for i in elements]

        for i in range(arr_len):
            for j in range(0, arr_len - i - 1):
                if get_no_of_ones(binary_values[j]) > get_no_of_ones(binary_values[j + 1]):
                    binary_values[j], binary_values[j + 1] = binary_values[j + 1], binary_values[j]
                    original_arr[j], original_arr[j + 1] = original_arr[j + 1], original_arr[j]
                elif (get_no_of_ones(binary_values[j]) == get_no_of_ones(binary_values[j + 1])) and elements[j] > \
                        elements[j + 1]:
                    binary_values[j], binary_values[j + 1] = binary_values[j + 1], binary_values[j]
                    original_arr[j], original_arr[j + 1] = original_arr[j + 1], original_arr[j]

        return binary_values


def get_no_of_ones(binary):
    ones = 0
    for i in binary:
        if i == '1':
            ones += 1
    return ones
