# Input
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