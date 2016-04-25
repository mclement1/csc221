#!/usr/bin/env python3.4

import sys


#Tuple containing all valid atomic symbols

atomic_symbols = ('H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al',
'Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu',
'Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh',
'Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm',
'Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir',
'Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np',
'Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs',
'Mt','Ds','Rg','Cn',)

atomic_symbols = [x.lower() for x in atomic_symbols]

#Tuple containing the atomic masses corresponding to the
#atomic symbols

atomic_masses = (1.007944,4.0026022,6.9412,9.0121823,10.8117,12.01078,14.00672,15.99943,
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


#Collect list of atomic symbols from user
def get_elements():
    elements = str(input('Please list the elements of which \
your molecule is composed as a comma-separated list. \
[ex: for water, type "H,O"] Type "quit" to quit. '))
    return elements


#Convert all user input to lowercase and remove
#excess spaces
def format_elements(elements):
    elements = (elements.lower()).replace(' ','')
    return elements


#Determine if user has entered something other
#than a comma-separated list
def validate_elements(elements):
        if elements == 'quit' or elements == '':
            return False
        
        else:
            return True
         

#Determine which of the atomic symbols entered
#by the user are legitimate, and add these
#to a python list called 'elements_list'
def list_elements(elements,atomic_symbols):
    elements_list = []
    elements = elements.split(',')
    for element in elements:
        if element in atomic_symbols:
            elements_list.append(element)
        else:
            continue
    return elements_list


#Collect list of numerical values from user
def get_numbers():
    numbers = str(input('Please list the number of each type of element \
elements of which your molecule is composed as a comma-separated list. \
Please list the values in the same order that you listed the elements \
and please only enter integers. [ex: for water, type "2,1"] \
Type "quit" to quit. '))
    return numbers



#Remove excess spaces from user input and,
#if the user's input is non-numerical,
#convert it to lowercase
def format_numbers(numbers):
    numbers = numbers.replace(' ','')
    try:
        numbers = numbers.lower()
    except:
        pass
    return numbers


#Determine if the user has entered something other
#than a comma-separated list
def validate_numbers(numbers):
        if numbers == 'quit' or numbers == '':
            return False
        
        else:
            return True
         

#Confirm that the input from the user is a comma-
#separated list of numbers, and add all integers
#to a python list called 'numbers_list'
def list_numbers(numbers):
    numbers_list = []
    numbers = numbers.split(',')
    for number in numbers:
        try:
            number = int(number)
            numbers_list.append(number)

        except:
            continue
    return numbers_list


#Confirm that the user entered the same number
#of atomic symbols as numbers
def comp_lists(elements_list, numbers_list):
    if len(elements_list) == len(numbers_list):
        return True

    else:
        return False



#Combine elements_list and numbers_list together
#into a dictionary called 'elements_dict'
def zip_lists(elements_list,numbers_list):
    elements_dict = dict(zip(elements_list, numbers_list))
    return elements_dict


#Collect input from the user concerning the kind
#of calculation he would like to perform
def what_calc():
    calc = str(input("Would you like to convert to grams or to moles? \
Enter 'g' for grams and 'm' for moles. "))
    return calc


#Strip excess spaces from the user's input
#and convert the input to lowercase
def clean_what_calc(calc):
    calc = (calc.lower()).replace(' ','')
    return calc


#Check to see that the input is one-character
#in length
def check_len_what_calc(calc):
    if len(calc) == 1:
        return True
    else:
        return False


#Confirm that the user input is one of the
#two valid options
def check_what_calc(calc):
    if calc == 'g' or calc == 'm':
        return True
    else:
        return False

#Determine which calculation the user would
#actually like to perform
def analyze_what_calc(calc):
    if calc == 'g':
        return 'g'
    elif calc == 'm':
        return 'm'


#Collect user input regarding his
#starting number of moles
def how_many_moles():
    moles = str(input('How many moles \
do you have? '))
    return moles


#Remove excess spaces from number of moles
def format_moles(moles):
    moles = moles.replace(' ','')
    return moles

#Determine whether or not a floating point
#number was entered
def confirm_float_moles(moles):
    try:
        moles = float(moles)
        return True
    except:
        return False
    

#Convert entered number of moles
#to floating point number
def make_moles_float(moles):
    moles = float(moles)
    return moles




#Collect user input regarding his
#starting number of grams
def how_many_grams():
    grams = str(input('How many grams \
do you have? '))
    return grams



#Remove excess spaces from number of grams
def format_grams(grams):
    grams = grams.replace(' ','')
    return grams

#Determine whether or not a floating point
#number was entered
def confirm_float_grams(grams):
    try:
        grams = float(grams)
        return True
    except:
        return False
    

#Convert entered number of grams
#to floating point number
def make_grams_float(grams):
    grams = float(grams)
    return grams



#Handle cases where a floating point number
#was not entered
def handle_not_float(starting):
    starting = starting.lower()
    if starting == 'quit':
        return True
    else:
        return False

#Calculate the molar mass of the molecule
#in question
def calc_molar_mass(elements_dict,data_table):
    molar_mass = 0
    for element in elements_dict.keys():
        atomic_mass = float(data_table[element])
        coefficient = float(elements_dict[element])
        composite_mass = coefficient*atomic_mass
        molar_mass = molar_mass + composite_mass
        #return molar_mass
    #print(molar_mass)
    return molar_mass



#Convert from moles to grams
def moles_to_grams(moles,molar_mass):
    grams = moles*molar_mass
    return grams




#Convert from grams to moles
def grams_to_moles(grams, molar_mass):
    moles = grams/molar_mass
    return moles




def main_elements():
    elements = get_elements()
    elements = format_elements(elements)
    bool_value = validate_elements(elements)
    while bool_value == False:
        if elements == 'quit':
            sys.exit()
        else:
            elements = format_elements(get_elements())
            bool_value = validate_elements(elements)
    elements_list = list_elements(elements,atomic_symbols)
    return elements_list
    #print(elements_list)


def main_numbers():
    numbers = get_numbers()
    numbers = format_numbers(numbers)
    bool_value_num = validate_numbers(numbers)
    while bool_value_num == False:
        if numbers == 'quit':
            sys.exit()
        else:
            numbers = format_numbers(get_numbers())
            bool_value_num = validate_numbers(numbers)
    numbers_list = list_numbers(numbers)
    return numbers_list
    #print(numbers_list)


def prepare_calc(elements_list, numbers_list):
    comp = comp_lists(elements_list, numbers_list)
    while comp == False:
        elements_list = main_elements()
        numbers_list = main_numbers()
    elements_dict = zip_lists(elements_list, numbers_list)
    #print(blah)
    return elements_dict

def main():
    elements_list = main_elements()
    numbers_list = main_numbers()
    elements_dict = prepare_calc(elements_list, numbers_list)
    calc_molar_mass(elements_dict,data_table)
    #print(data_table)


if __name__ == '__main__':
    main()
         
         
         
