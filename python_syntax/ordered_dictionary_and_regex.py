# Input for ordered dictionary
'''
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
'''
# output
'''
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY  20
'''

from collections import OrderedDict
import re


def ordered_dictionary_example():
    n = int(input())
    item_name_regex = r"^[A-Z ]"
    item_price_regex = r"[0-9]+$"

    ordered_dictionary = OrderedDict()

    for i in range(n):
        row = input()
        item_name = re.search(item_name_regex, row).group(0)
        item_price = int(re.search(item_price_regex, row).group(0))
        if item_name not in ordered_dictionary:
            ordered_dictionary[item_name] = item_price
        else:
            ordered_dictionary[item_name] = ordered_dictionary[item_name] + item_price

    for key, value in ordered_dictionary.items():
        print(key + str(value))


"""
Sample Input 0

4
SomeRandomStuff
-1.00
+4.54
4.0O0
Sample Output 0

False
True
True
False
"""


def check_floating_number(input_value):
    floating_number_regex = r"([+-]?[0-9]*([.]{1}[0-9]+)$)"

    matches = re.search(floating_number_regex, input_value)
    if matches is None:
        result = False
    else:
        regex_matched_value = matches.group(0)
        result = input_value == regex_matched_value
    return result


if __name__ == '__main__':
    # ordered_dictionary_example()

    for i in range(int(input())):
        input_value = input()
        print(check_floating_number(input_value))


"""
Another example of regex usage for split of string

print(re.split(r"[,|.]", "100,000,000.000"))
['100', '000', '000', '000']

"""
