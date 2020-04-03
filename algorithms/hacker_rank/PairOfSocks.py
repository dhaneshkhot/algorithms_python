class PairOfSocks:
    def find_no_of_pairs(self, arr):
        pairs = 0
        total_dict = {}

        for i in arr:
            if i not in total_dict:
                total_dict[i] = 1
            else:
                count = total_dict[i]
                total_dict[i] = count+1

        for key, value in total_dict.items():
            pairs += value//2

        return pairs