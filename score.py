# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def give_score(self, length, number):  # sum of all scores
        score = Score().length_score(length) + Score().number_score(number)
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