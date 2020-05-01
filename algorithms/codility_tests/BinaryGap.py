"""
Binary Gap: Max occurrences of 0's between two 1s in a binary value

E.g.
i/p: 187838748
binary_form: 1011001100100011000100011100
o/p: 3
"""
import re


class BinaryGap:

    def solution(self, number):
        binary_form = "{0:b}".format(number)
        # print(binary_form)
        regx = r"1+"
        list_of_1s = re.findall(regx, binary_form)
        binary_gap = 0

        for i in list_of_1s:
            if len(i) > binary_gap:
                binary_gap = len(i)

        return binary_gap

    def solution2(self, number):
        binary_form = "{0:b}".format(number)
        # print(binary_form)
        binary_gap = 0
        gap_start = False
        zero_counter = 0
        for bit in binary_form:
            if bit == '1':
                gap_start = True
            if bit == '0' and gap_start:
                zero_counter += 1
            if bit == '1' and gap_start and zero_counter > 0:
                if zero_counter > binary_gap:
                    binary_gap = zero_counter
                zero_counter = 0
        return binary_gap
