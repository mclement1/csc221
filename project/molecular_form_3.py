#!/usr/bin/env python3.4

import sys

from molecular_form_2 import (
        get_elements,
        rem_comm_spaces,
        only_alpha,
        format_input,
        validate_elements,
        list_elements,
        get_numbers,
        only_num,
        comp_lists,
        zip_lists,
)


atomic_symbols = ('H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al',
'Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu',
'Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh',
'Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm',
'Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir',
'Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np',
'Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs',
'Mt','Ds','Rg','Cn',)

atomic_symbols = [x.lower() for x in atomic_symbols]

def func_one():
    elements = get_elements()
    elements_stripped = rem_comm_spaces(elements)
    alpha_only = only_alpha(elements_stripped)
    while alpha_only == False:
        print('\t')
        print("I'm sorry, but you seem to have entered \
a numerical value, invalid punctuation mark, or the empty string. \
Please try again.")
        print('\t')
        elements = get_elements()
        elements_stripped = rem_comm_spaces(elements)
        alpha_only = only_alpha(elements_stripped)
        continue
    return elements


def func_two(elements):
    elements_formatted = format_input(elements)
    if elements_formatted == 'quit':
        sys.exit()

    else:
        return elements_formatted

def func_three(elements_formatted):
    elements = elements_formatted.split(',')
    for element in elements:
        if element in atomic_symbols:
            continue
        else:
            print('\t')
            print("I'm sorry, but you have entered \
a non-valid atomic symbol. Please try again.")
            print('\t')
            elements = func_one()
            elements_formatted = func_two(elements)
            continue
    return elements


    

def func_four():
    numbers = get_numbers()
    numbers_stripped = rem_comm_spaces(numbers)
    num_only = only_num(numbers_stripped)
    while num_only == False:
        numbers = format_input(numbers)
        if numbers == 'quit':
            sys.exit()
        else:
            print('\t')
            print("I'm sorry, but you seem to have entered \
a letter, an invalid punctuation mark, or the empty string. \
Please try again.")
            print('\t')
            numbers = get_numbers()
            numbers_stripped = rem_comm_spaces(numbers)
            num_only = only_num(numbers_stripped)
            continue
    return numbers


def func_five(numbers):
    numbers_list = []
    numbers = numbers.replace(' ','')
    numbers = numbers.split(',')
    for number in numbers:
        numbers_list.append(int(number))

    return numbers_list




def func_six(elements_list, numbers_list):
    bool_value = comp_lists(elements_list, numbers_list)
    return bool_value

def func_seven(bool_value):    
    while bool_value == False:
        print('\t')
        print("I'm sorry, but you have not entered the \
same number of integers as atomic symbols. Please try again.")
        print('\t')
        elements_list = func_three(func_two(func_one()))
        numbers_list = func_five(func_four())
        bool_value = comp_lists(elements_list, numbers_list)
        continue
    #print(elements_list, numbers_list)
    elements_dict = zip_lists(elements_list, numbers_list)
    #print(elements_dict)
    return elements_dict





def main():
    elements = func_one()
    elements_formatted = func_two(elements)
    elements_list = func_three(elements_formatted)
    numbers = func_four()
    numbers_list = func_five(numbers)
    bool_value = func_six(elements_list, numbers_list)
    #elements_list, numbers_list = func_six(elements_list, numbers_list)
    func_seven(bool_value)



if __name__=='__main__':
    main()
