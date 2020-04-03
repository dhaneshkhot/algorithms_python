class SherlockMiniMax:

    def get_sherlock_mini_max(self, arr, p, q):
        m_range = range(p, q + 1)
        m_min = []
        mini_max_dict = {}

        for i in range(len(arr)):
            tmp = []
            for j in m_range:
                tmp.append(abs(arr[i] - j))
            mini_max_dict[i] = tmp

        for i in range(len(m_range)):
            m_min.append(0)

        for key, value in mini_max_dict.items():
            for i in range(len(value)):
                if key == 0:
                    m_min[i] = value[i]
                elif m_min[i] > value[i]:
                    m_min[i] = value[i]

        max_value_from_m_min = max(m_min)

        mini_max = []
        for i in range(len(m_min)):
            if m_min[i] == max_value_from_m_min:
                mini_max.append(m_range[i])  # gets all values from m_range where we have max_value_from_m_min

        return min(mini_max)

    def get_sherlock_mini_max_2(self, arr, p, q):
        m = set([])
        i = 0
        arr.sort()
        while i+1 in range(len(arr)):
            mid_of_adjacent_elements = (arr[i] + arr[i + 1]) // 2
            if (arr[i] + arr[i + 1]) % 2 == 0 and p <= mid_of_adjacent_elements <= q:
                m.add(mid_of_adjacent_elements)
            # elif p <= mid_of_adjacent_elements <= q:
            #     m.add(mid_of_adjacent_elements)
            #     m.add(mid_of_adjacent_elements + 1)
            i += 1

        print(m)
        m.add(p)
        m.add(q)

        m_sorted = sorted(m)

        print(m_sorted)

        min_placeholder = -1
        ans = 0

        for i in m_sorted:
            if p <= i <= q:
                minimum = p + q
                for j in arr:
                    minimum = minimum if minimum < abs(i - j) else abs(i - j)
                if minimum > min_placeholder:
                    min_placeholder = minimum
                    ans = i

        return ans
