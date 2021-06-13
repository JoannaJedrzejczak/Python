# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:03:36 2021

@author: Joanna
"""

import re
import enchant


class Checker:
    def __init__(self, password):
        self.dicAng = enchant.Dict("en_US")
        self.dicPL = enchant.Dict("pl_PL")
        self.password = password

    def check_length(self):  # check length of password
        return len(self.password)

    def check_number(self):  # count how many numbers
        pattern = '[0-9]'
        return len(re.findall(pattern, self.password))

    def check_special(self):  # count how many special characters
        pattern = '[^A-Za-z0-9+]'
        return len(re.findall(pattern, self.password))

    def check_upper_case(self):  # count how many upper case letters
        pattern = '[A-Z]'
        return len(re.findall(pattern, self.password))

    def check_lower_case(self):  # count how many lower case letters
        pattern = '[a-z]'
        return len(re.findall(pattern, self.password))

    def find_string(self):  # find words (between special characters or numbers)
        pattern = '[a-zA-Z]+'
        words = re.findall(pattern, self.password)
        return words

    def check_dict(self, words):  # check in dictionaries - PL and EN - if exist - enchant library and hunspell dictionary
        if not words:
            return False
        for word in words:
            print(word)
            if self.dicAng.check(word) or self.dicPL.check(word):
                return False
        return True

    