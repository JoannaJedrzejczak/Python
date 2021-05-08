# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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
