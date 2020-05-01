class BubbleSort:

    """
    returns list of num_of_swaps, first element, and last element after sort
    """
    def get_num_of_swaps_with_bubble_sort(self, a):
        swaps = 0
        for i in range(len(a)):
            swap_flag = False
            for j in range(len(a) - i - 1):
                if a[j] > a[j + 1]:
                    swap_flag = True
                    swaps += 1
                    a[j], a[j + 1] = a[j + 1], a[j]
            if swap_flag is False:
                break

        return [swaps, a[0], a[-1]]