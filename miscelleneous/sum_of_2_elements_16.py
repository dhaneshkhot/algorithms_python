def get_list_of_tuples_from_list_for_which_sum_is_16(a, b):
    l = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == b:
                l.append((a[i], a[j]))
    return l
