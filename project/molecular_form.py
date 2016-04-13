#!/usr/bin/env python3.4

import pandas as pd

atomic_symbols = pd.read_csv('atomic_symbols.csv')
atomic_masses = pd.read_csv('atomic_masses.csv')
#atomic_symbols['x'].str.lower()
#atomic_masses = []
#print(atomic_symbols) 

def get_elements():
    elements = str(input('Please list the elements of which \
your molecule is composed as a comma-separated list. \
[ex: for water, type "H,O"] Type "quit" to quit. '))
    return elements

def check_elements(elements):
    elements = (elements.lower()).replace(' ','')
    while True:
        if elements == 'quit':
            break
        elif elements == '':
            elements = str(input("I'm sorry, but your input was not \
of the correct form. Please try again (Type 'quit' to quit.) "))
            continue
        else:
            return elements
#
#def clean_elements(elements):
#    elements_list = []
#    #elements = elements.lower()
#    #elements = elements.replace(' ','')
#    elements = elements.split(',')
#    for i in elements:
#        elements_list.append(i)
#    return elements_list
#
#def check_legit(elements_list, atomic_symbols):
#    for i in elements_list:
#        if i not in atomic_symbols:
#            elements = input("I'm sorry, but {} is not \
#a legitimate atomic symbol. Please re-enter your list of \
#atomic symbols").format(i)
#            #call get_elements
#
#
#def get_numbers():
#    numbers = str(input('Please list the number of each \
#type of element present in your molecule as a \
#comma-separated list. Please list the numbers in the \
#same order you listed the elements above. Please input \
#only positive integers. [ex: for water, type "2,0"] Type \
#"quit" to quit. '))
#
#def check_numbers(numbers):
#    numbers = (numbers.lower()).replace(' ','')
#    while True:
#        if numbers == 'quit':
#            break
#        elif numbers == '':
#            numbers = str(input("I'm sorry, but your input was not \
#of the correct form. Please try again (Type 'quit' to quit.) "))
#        else:
#            return numbers
#
#
#def clean_numbers():
#    numbers_list = []
#    numbers = numbers.split(',')
#    for i in numbers:
#        numbers_list.append(int(i))
#
#
#def comp_lists(elements_list, numbers_list):
#    if len(elements_list) != len(numbers_list):
#        user_answer = input("I'm sorry, but the number \
#of elements that you entered and the number of numerical \
#values that you entered are not the same. Would you like \
#to try again? Type 'y' to continue or 'n' to quit")
#        return user_answer
#
#def parse_user_answer(user_answer):
#    user_answer = (user_answer.lower()).replace(' ','')
#    while True:
#        if user_answer == 'y':
#            #call get_elements
#        elif user_answer == 'n':
#            break
#        else:
#            user_answer = input("I'm sorry, but I did \
#not understand your answer. Please try again.")
#            return user_answer
#
##def molar_mass():
##def what_value():
##def compute_moles():
##def compute_grams():
##def continue():
#
##def get_elements():
#    #elements_list = []
#    
#    #elements = str(input('Please list the elements of which \
##your molecule is composed as a comma-separated list. \
##[ex: for water, type "H,O"] Type "quit" to quit. '))
#    
#    
#    #while elements == '':
#        #elements = str(input("I'm sorry, but your input was not \
##of the correct form. Please try again (Type 'quit' to quit.) "))
#
#        
#    #while elements != '':
#
#        #if elements.lower() == 'quit':
#            #break
#
#        #else:
#            #elements = elements.lower()
#            #elements = elements.replace(' ','')
#            #elements = elements.split(',')
#            #for i in elements:
#                #elements_list.append(i)
#        
#        #print(elements_list)
#        #break
#    #return elements_list
#
#
##def check_elements(passed_list):
#    #print(passed_list)
#
#
#    
#
def main():
    elements = get_elements()
    check_elements(elements)
if __name__ == '__main__':
    main()
#
#    
