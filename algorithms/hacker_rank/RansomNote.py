class RansomNote:
    def can_note_be_made_from_magazine(self, magazine, note):
        magazine_dict = {}
        note_dict = {}
        for word in magazine.split():
            if word in magazine_dict:
                count = magazine_dict[word]
                magazine_dict[word] = count + 1
            else:
                magazine_dict[word] = 1

        for word in note.split():
            if word in note_dict:
                count = note_dict[word]
                note_dict[word] = count + 1
            else:
                note_dict[word] = 1

        for word, count in note_dict.items():
            if word in magazine_dict:
                if magazine_dict[word] >= count:
                    continue
                else:
                    return "No"
            else:
                return "No"

        return "Yes"
