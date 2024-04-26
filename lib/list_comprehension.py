#!/usr/bin/env python3

def return_evens(num_list):
    evens_num_lists = [ n for n in num_list if n % 2 == 0]
    return evens_num_lists
    pass

def make_exclamation(sentence_list):
    new_sentence_list = [word + '!' for word in sentence_list ]
    return new_sentence_list
    pass