# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:38:26 2021

@author: stock
"""

#Function to change state and check if final state is part of the accepted 
#states' set
def AFD(transitions, initial, accepting, s):
    if s == "-":
        return "rejeita"
    else:
        state = initial
        for c in s:
            state = transitions[state][c]
            
        if (str(state) in accepting) is not True:        
            return "rejeita"
        else:
            return "aceita"
        

#Dictionary populator if you have multiple values for a single key
def add_values_in_dict1(sample_dict, key, value):
    if key not in sample_dict:
        sample_dict[key] = value
    return sample_dict

#Dictionary populator for populating dictionary keys with another dictionary
def add_values_in_dict2(sample_dict, key, sup_dict):
    if key not in sample_dict:
        sample_dict[key] = {}
    sample_dict[key] = sup_dict
    return sample_dict

transitions_dictionary = {}
sup_dictionary = {}

#Receiving acceptance states from user
acceptance_states = input("Enter acceptance states separated by space: ")
acceptance_states = set(acceptance_states.split())

#Receiving number of transitions from user
t = int(input("Input number of transitions present in the transition function: "))

#Receiving transitions from user
transitions = []
for i in range(t):
    transitions.append(input("Enter input {}: " .format(i+1)))

#Populating transitions dictionary
cur_state = 0
for trans in transitions:
    state, key, value = trans.split()
    
    if state != str(cur_state):
        cur_state += 1
        sup_dictionary = {}
        
    add_values_in_dict1(sup_dictionary, key, int(value))
    add_values_in_dict2(transitions_dictionary, cur_state, sup_dictionary)


#Receiving number of strings to be tested
c = int(input("Input number of strings that are going to be tested: "))

#Receiving strings one by one
strings = []
for i in range(c):
    strings.append(str(input("input string {}: " .format(i+1))))
