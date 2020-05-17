class Palindrome:
    def check_if_palidrome(self, string):
        halfway = len(string)//2
        last_index = -1
        for i in range(halfway):
            if string[i] != string[last_index-i]:
                return False
        return True

    """
    Finds first palindrome substring from a given string
    """
    def get_palindrome_substring(self, string):
        stripped = "".join(string.split())
        palindrome_string = ""
        for i in range(len(stripped)):
            for j in range(0, i):
                substring = stripped[j:i + 1]
                if substring == substring[::-1]:
                    palindrome_string = substring
                    break
            if palindrome_string != "":
                break
        return palindrome_string


    """
    Finds largest palindrome substring from a given string
    """
    def get_largest_palindrome_substring(self, string):
        stripped = "".join(string.split())
        palindrome_string = ""
        for i in range(len(stripped)):
            for j in range(0, len(stripped)-i):
                substring = stripped[j:i + 1]
                if substring == substring[::-1] and len(palindrome_string) < len(substring):
                    palindrome_string = substring
        return palindrome_string


if __name__ == "__main__":
    p = Palindrome()
    print(p.get_largest_palindrome_substring("tacocatac"))
