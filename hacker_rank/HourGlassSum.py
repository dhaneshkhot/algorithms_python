class HourGlassSum:

    def hourglassSum(self, arr):
        hourglass_sum = -1000
        hg_arr_size = 3

        l = 0
        m = 0

        hg_dict = {}

        while l <= 3:
            while m <= 3:
                hg = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                for i in range(hg_arr_size):
                    for j in range(hg_arr_size):
                        hg[i][j] = arr[i+l][j+m]
                hg[1][0] = 0
                hg[1][2] = 0
                hg_dict[str(l)+str(m)] = hg
                m += 1
            l += 1
            m = 0

        hg_sum_dict = {}
        for key, hourglass in hg_dict.items():
            sum = 0
            for i in range(hg_arr_size):
                for j in range(hg_arr_size):
                    sum = sum + hourglass[i][j]
            hg_sum_dict[key] = sum

        for key, value in hg_sum_dict.items():
            if hourglass_sum < value:
                hourglass_sum = value

        return hourglass_sum
