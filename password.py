# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:03:30 2021

@author: Joanna
"""

from checker import Checker
from score import Score


class Password:
    def __init__(self):
        self.password = ""
        self.length = self.number = self.special = self.upper = self.lower = 0
        self.words = []
        self.dict = False

    def get_password(self):  # gets password from input
        print("Enter password:")
        self.password = input()
        return self.password

    def check_password(self):  # check password if contain requirements and print results
        checker = Checker(self.password)
        self.length = checker.check_length()
        self.number = checker.check_number()
        self.special = checker.check_special()
        self.upper = checker.check_upper_case()
        self.lower = checker.check_lower_case()
        self.words = checker.find_string()
        self.dict = checker.check_dict(self.words)
        print("Length: " + str(self.length))
        print("Number: " + str(self.number))
        print("Special: " + str(self.special))
        print("Upper case: " + str(self.upper))
        print("Lower case: " + str(self.lower))
        print("Dictionary (if false then exist or no word to check): " + str(self.dict))

    def give_score(self):  # give scores and print results
        counter = Score()
        print("-----------------------------")
        score = counter.give_score(self.length, self.number, self.special, self.upper, self.lower, self.dict)
        print("-----------------------------")
        print("Score: " + str(score))


passwd = Password()
passwd.get_password()
passwd.check_password()
passwd.give_score()