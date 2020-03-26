class MaxOccuringCharacter:

    def maximum_occurring_character(self, text):

        occurance_dict = {}
        max_occurance_character = None

        max_count = 0
        for i in text:
            if i not in occurance_dict:
                occurance_dict[i] = 1
            else:
                count = occurance_dict[i]
                occurance_dict[i] = count + 1

        for key, value in occurance_dict.items():
            if max_count < value:
                max_count = value
                max_occurance_character = key

        return max_occurance_character
