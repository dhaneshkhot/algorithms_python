class TwoStrings:
    def do_they_share_common_substring_1(self, s1, s2):
        for i in range(len(s1)):
            for j in range(0, i + 1):
                substring = s1[j: i + 1]
                if substring in s2:
                    return "YES"
        return "NO"

    def do_they_share_common_substring_2(self, s1, s2):
        return 'YES' if set(s1) & set(s2) else 'NO'

    def do_they_share_common_substring_3(self, s1, s2):
        return 'YES' if any(i in s2 for i in s1) else 'NO'
