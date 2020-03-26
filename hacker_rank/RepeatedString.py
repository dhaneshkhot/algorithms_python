class RepeatedString:

    def count_occurances_of_a_character(self, s, no_of_chars_to_consider):
        char_count_in_tail_string = 0
        char_count_in_original_string = 0

        str_len = len(s)
        str_repeated_count = no_of_chars_to_consider // str_len
        remainder_no_of_chars = no_of_chars_to_consider % str_len

        for i in range(remainder_no_of_chars):
            if s[i] == 'a':
                char_count_in_tail_string += 1

        for i in s:
            if i == 'a':
                char_count_in_original_string += 1

        char_count_in_total_string = char_count_in_original_string * str_repeated_count + char_count_in_tail_string
        return char_count_in_total_string
