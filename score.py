# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Score:

    def give_score(self, length, number, special, upper_case, lower_case, dictonary):  # sum of all scores
        score = Score().length_score(length) + Score().number_score(number) + Score().special_score(special) + \
                Score().letter_score(upper_case, lower_case) + Score().dict_score(dictonary)
        return score

    def length_score(self, length):  # score for length
        score = 0
        if 5 < length < 10:
            score = 1
        elif 9 < length < 16:
            score = 2
        elif length > 15:
            score = 3
        print("Length: " + str(score))
        return score

    def number_score(self, number):  # score for qt of numbers
        score = 0
        if number > 0:
            score = 1
        print("Number: " + str(score))
        return score

    def special_score(self, special):  # score for qt of special characters
        score = 0
        if 0 < special < 3:
            score = 1
        elif special > 2:
            score = 2
        print("Special: " + str(score))
        return score

    def letter_score(self, upper_case, lower_case):  # score for qt of upper case letters
        score = 0
        if 0 < upper_case < 3:
            score = 1
        if upper_case > 2 and lower_case > 1:
            score = 2
        print("Letter: " + str(score))
        return score

    def dict_score(self, dictionary):  # score for dictionary words
        score = 0
        if dictionary:
            score = 2
        print("Dict: " + str(score))
        return score