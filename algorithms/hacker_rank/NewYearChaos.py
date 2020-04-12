class NewYearChaos:
    def get_minimum_bribes_with_bubble_sort(self, q):
        bribes = {}
        for i in range(len(q)):
            swap_flag = False
            need_to_continue = True
            for j in range(len(q) - i - 1):
                if q[j] > q[j + 1]:
                    swap_flag = True
                    if q[j] in bribes:
                        bribe = bribes[q[j]]
                        bribes[q[j]] = bribe + 1
                        if bribes[q[j]] > 2:
                            need_to_continue = False
                            break
                    else:
                        bribes[q[j]] = 1
                    q[j], q[j + 1] = q[j + 1], q[j]
            if swap_flag is False and need_to_continue is False:
                break
        total_bribes = list(bribes.values())
        return sum(total_bribes) if max(total_bribes) <= 2 else "Too chaotic"

    def get_minimum_bribes_with_index(self, q):
        bribes = 0
        for index, value_at_index in enumerate(q):
            value = value_at_index-1 # to match the index and values since values starts from 1 and index from 0

            if value - index > 2:
                return "Too chaotic"
            # Anyone who bribed cannot get to higher than
            # one position in front if values's original position hence start from (value-1)
            # This way we'll get how many bribes one has taken
            for i in range(max(value-1, 0), index):
                if q[i] > value:
                    bribes += 1
        return bribes
