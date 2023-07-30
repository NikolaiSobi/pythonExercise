#!/usr/bin/env python3

#1. 
list = ["HELLO", "hi", "goodbye"]
for word in list:
    print(word.upper())

#2.
def print_upper_words(list):
    '''takes word and prints them in upper case'''
    for word in list:
        print(word.upper())

#3.
def print_start_words_e(list):
    for word in list:
        if word[0].lower() == "e":
            print(word.upper())

#4.
def print_certain_upper_words(list, must_start_with):
    for word in list:
        if word[0].lower() == must_start_with[0]:
            print(word.upper())
        elif word[0].lower() == must_start_with[1]:
            print(word.upper())


