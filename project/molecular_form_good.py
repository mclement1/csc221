#!/usr/bin/env python3.4

import sys

import pprint

from molecular_form_base_functions import (
        get_elements,
        rem_comm_spaces,
        only_alpha,
        format_input,
        #validate_elements,
        #list_elements,
        get_numbers,
        only_num,
        comp_lists,
        zip_lists,
        calc_molar_mass,
        what_calc,
        clean_what_calc,
        is_alpha,
        check_len_what_calc,
        #check_what_calc,
        analyze_what_calc,
        how_many_moles,
        format_moles,
        confirm_float_moles,
        make_moles_float,
        how_many_grams,
        format_grams,
        confirm_float_grams,
        make_grams_float,
        handle_not_float,
        moles_to_grams,
        grams_to_moles,
        another_calc,
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

atomic_masses = (1.007944,4.0026022,6.9412,9.0121823,10.8117,12.01078,14.00672,
15.99943,
18.99840325,20.17976,22.989769282,24.30506,26.98153868,28.08553,
30.9737622,32.0655,35.4532,39.9481,39.09831,40.0784,44.9559126,47.8671,
50.94151,51.99616,54.9380455,55.8452,58.9331955,58.69344,63.5463,65.382,
69.7231,72.641,74.921602,78.963,79.9041,83.7982,85.46783,87.621,88.905852,
91.2242,92.906382,95.962,98,101.072,102.905502,106.421,107.86822,112.4118,
114.8183,118.7107,121.7601,127.603,126.904473,131.2936,132.90545192,
137.3277,138.905477,140.1161,140.907652,144.2423,145,150.362,151.9641,
157.253,158.925352,162.5001,164.930322,167.2593,168.934212,173.0545,
174.96681,178.492,180.947882,183.841,186.2071,190.233,192.2173,195.0849,
196.9665694,200.592,204.38332,207.21,208.980401,209,210,222,223,226,227,
232.038062,231.035882,238.028913,237,244,243,247,247,251,252,257,258,259,262,
267,268,271,272,270,276,281,280,285,)


#Create a dictionary linking atomic symbol with appropriate
#mass

data_table = dict(zip(atomic_symbols, atomic_masses))

def func_one():
    elements = get_elements()
    elements_stripped = rem_comm_spaces(elements)
    alpha_only = only_alpha(elements_stripped)
    while alpha_only == False:
        print('\n')
        print("I'm sorry, but you seem to have entered \
a numerical value, invalid punctuation mark, or the empty string. \
Please try again." + '\n')
        #print('\n')
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
    elements_list = []
    for element in elements:
        if element in atomic_symbols:
            elements_list.append(element)
            #return elements_list

        else:
            continue
    return elements,elements_list
    #return elements_list
    #if len(elements) == len(elements_list):
        #return True
    #else:
        #return False
    #bool_value = all(i in atomic_symbols for i in elements)
    #return bool_value
    #if all( i in elements in atomic_symbols:
        #return True
    #else:
        #return False
    #for element in elements:
        #if element in atomic_symbols:
            #continue
        #else:
            #print("I'm sorry, but you have entered \
    #a non-valid atomic symbol. Please try again." + '\n')
            #print('\n')
            #elements = func_one()
            #elements_formatted = func_two(elements)
            #break
            #return elements_formatted
            #legit_bool = func_three(elements_formatted)
            #continue
    #return elements
    #legit_bool = lambda atomic_symbols,elements: all(x in atomic_symbols for x in elements)
    #print(legit_bool)
    #return legit_bool, elements

#def func_three_half(legit_bool,elements):
    #while legit_bool == False:
        #print("I'm sorry, but you have entered \
#a non-valid atomic symbol. Please try again." + '\n')
        #print('\n')
        #elements = func_one()
        #elements_formatted = func_two(elements)
        #legit_bool = func_three(elements_formatted)
        #continue
        #func_three_half(legit_bool,elements)
        #return elements
        #return legit_bool
        #continue
    #return elements
    #for element in elements:
    #while elements not in atomic_symbols:
        #elements = func_one()
        #elements_formatted = func_two(elements)
        #elements = elements_formatted.split(',')
        #return elements
            #continue

        #if element in atomic_symbols:
            #return True
            #continue
        #else:
            #print('\n')
            #print("I'm sorry, but you have entered \
#a non-valid atomic symbol. Please try again." + '\n')
            #print('\n')
            #elements = func_one()
            #elements_formatted = func_two(elements)
            #elements = elements_formatted.split(',')
            #break
            #return elements
            #return elements_formatted
            #continue
    #return element


def func_three_a(elements, elements_list):
    bool_legit = len(elements) == len(elements_list)
    return bool_legit


def func_three_b(bool_legit):
    while bool_legit == False:
        print("I'm sorry, but you have entered an invalid \
atomic symbol. Please try again." + '\n')
        elements = func_one()
        elements_formatted = func_two(elements)
        elements, elements_list = func_three(elements_formatted)
        bool_legit = func_three_a(elements,elements_list)

    return elements_list





#def func_three_a(bool_legit):
    #if bool_legit == True:
        #print('yay')

    #else:
        #pass


def func_four():
    #print('\n')
    numbers = get_numbers()
    numbers_stripped = rem_comm_spaces(numbers)
    num_only = only_num(numbers_stripped)
    while num_only == False:
        numbers = format_input(numbers)
        if numbers == 'quit':
            sys.exit()
        else:
            #print('\n')
            print("I'm sorry, but you seem to have entered \
a letter, an invalid punctuation mark, or the empty string. \
Please try again." + '\n')
            #print('\n')
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
    while bool_value == False:
        #print('\n')
        print("I'm sorry, but you have not entered the \
same number of integers as atomic symbols. Please try again." + '\n')
        #print('\n')
        elements_list = func_three(func_two(func_one()))
        numbers_list = func_five(func_four())
        return elements_list, numbers_list
        bool_value = comp_lists(elements_list, numbers_list)
        continue
    return elements_list, numbers_list


def func_seven(elements_list, numbers_list):
    elements_dict = zip_lists(elements_list, numbers_list)
    return elements_dict


def func_eight(elements_dict, data_table):
    molar_mass = calc_molar_mass(elements_dict, data_table)
    #print(molar_mass)
    return molar_mass


def func_nine():
    calc = what_calc()
    calc_cleaned = clean_what_calc(calc)
    alpha_bool_value = is_alpha(calc_cleaned)
    while alpha_bool_value == False:
        #print('\n')
        print("I'm sorry, but you have entered a number, \
a punctuation mark, or the empty string. Please try again" + '\n')
        #print('\n')
        calc = what_calc()
        calc_cleaned = clean_what_calc(calc)
        alpha_bool_value = is_alpha(calc_cleaned)
        return calc_cleaned
        continue
    return calc_cleaned


def func_ten(calc_cleaned):
    calc_cleaned = calc_cleaned.lower()
    len_bool_value = check_len_what_calc(calc_cleaned)
    while len_bool_value == False:
        if calc_cleaned == 'quit':
            sys.exit()

        else:
            #print('\n')
            print("I'm sorry, but you have entered a non-legitimate \
calculation type. Please try again." + '\n')
            #print('\n')
            calc_cleaned = func_nine()
            len_bool_value = check_len_what_calc(calc_cleaned)
            return calc_cleaned
            continue

    return calc_cleaned


def func_eleven(calc_cleaned, molar_mass):
    calc = analyze_what_calc(calc_cleaned)
    if calc == 'g':
        moles = how_many_moles()
        formatted_moles = format_moles(moles)
        float_bool_value = confirm_float_moles(formatted_moles)
        while float_bool_value == False:
            bool_not_float = handle_not_float(formatted_moles)
            if bool_not_float == True:
                sys.exit()

            else:
                print("I'm sorry, but you did not enter a floating-point \
value. Please try again." + '\n')
                moles = how_many_moles()
                formatted_moles = format_moles(moles)
                float_bool_value = confirm_float_moles(formatted_moles)
                continue
        moles = make_moles_float(moles)
        grams = moles_to_grams(moles,molar_mass)
        answer = str(grams) + ' ' + 'g'
        print('\n')
        print("You have " + answer + '\n')
        #return str(grams) + ' ' + 'g'
        #return moles

    elif calc == 'm':
        grams = how_many_grams()
        formatted_grams = format_grams(grams)
        float_bool_value = confirm_float_grams(formatted_grams)
        while float_bool_value == False:
            bool_not_float = handle_not_float(formatted_grams)
            if bool_not_float == True:
                sys.exit()

            else:
                print("I'm sorry, but you did not enter a floating-point \
value. Please try again." + '\n')
                grams = how_many_grams()
                formatted_grams= format_grams(grams)
                float_bool_value = confirm_float_grams(formatted_grams)
                continue
        grams = make_grams_float(grams)
        moles = grams_to_moles(grams,molar_mass)
        answer = str(moles) + ' ' + 'm'
        print('\n') 
        print("You have " + answer + '\n')
        #return str(moles) + ' ' + 'mol'
        #return grams

def func_twelve():
    #print('\n')
    another_calc_dec = another_calc()
    cleaned_calc_dec  = rem_comm_spaces(another_calc_dec)
    alpha_bool_value = is_alpha(cleaned_calc_dec)
    while alpha_bool_value == False:
        #print('\n')
        print("I'm sorry, but I did not understand that. \
Please try again. " + '\n')
        #print('\n')
        another_calc_dec = another_calc()
        cleaned_calc_dec = rem_comm_spaces(another_calc_dec)
        alpha_bool_value = is_alpha(cleaned_calc_dec)
        continue
    return another_calc_dec
    
    


def func_thirteen(another_calc_dec,molar_mass):
    form_another_calc = format_input(another_calc_dec)
    while form_another_calc not in ('quit','yes'):
        #print('\n')
        print("I'm sorry, but I did not understand that. \
Please try again. " + '\n')
        another_calc_dec = func_twelve()
        form_another_calc = format_input(another_calc_dec)
        continue

    if form_another_calc == 'quit':
        sys.exit()
    
    else:
       calc_cleaned = func_nine()
       calc_cleaned = func_ten(calc_cleaned)
       answer = func_eleven(calc_cleaned, molar_mass)

    another_calc_dec = func_twelve()
    func_thirteen(another_calc_dec,molar_mass)
    #form_another_calc = format_input(another_calc_dec)
    #continue





def main():
    elements = func_one()
    elements_formatted = func_two(elements)
    elements,elements_list = func_three(elements_formatted)
    #bool_legit = func_three(elements_formatted)
    bool_legit = func_three_a(elements,elements_list)
    elements_list = func_three_b(bool_legit)
    #elements_list = func_three(elements_formatted)
    #legit_bool,elements = func_three(elements_formatted,atomic_symbols)
    #func_three_half(legit_bool,elements)
    numbers = func_four()
    numbers_list = func_five(numbers)
    elements_list, numbers_list = func_six(elements_list, numbers_list)
    elements_dict = func_seven(elements_list, numbers_list)
    molar_mass = func_eight(elements_dict, data_table)
    calc_cleaned = func_nine()
    calc_cleaned = func_ten(calc_cleaned)
    answer = func_eleven(calc_cleaned,molar_mass)
    another_calc_dec = func_twelve()
    func_thirteen(another_calc_dec,molar_mass)
    



if __name__=='__main__':
    main()