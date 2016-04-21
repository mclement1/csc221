#!/usr/bin/env python3.4

import sys

atomic_symbols = ('H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al',
'Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu',
'Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh',
'Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm',
'Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir',
'Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np',
'Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs',
'Mt','Ds','Rg','Cn',)

atomic_symbols = [x.lower() for x in atomic_symbols]

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

data_table = dict(zip(atomic_symbols, atomic_masses)) 


def get_elements():
    elements = str(input('Please list the elements of which \
your molecule is composed as a comma-separated list. \
[ex: for water, type "H,O"] Type "quit" to quit. '))
    return elements


def format_elements(elements):
    elements = (elements.lower()).replace(' ','')
    return elements


def validate_elements(elements):
        if elements == 'quit' or elements == '':
            return False
        
        else:
            return True
         

def list_elements(elements,atomic_symbols):
    elements_list = []
    elements = elements.split(',')
    for element in elements:
        if element in atomic_symbols:
            elements_list.append(element)
        else:
            continue
    return elements_list

#def check_legit(elements_list, atomic_symbols):
    #for element in elements_list:
        #if element in atomic_symbols:
            #return True
            #continue
        #else:
            #break
        #return False
    #break
        #break    
        #continue
        #else:
            #return True
            



def get_numbers():
    numbers = str(input('Please list the number of each type of element \
elements of which your molecule is composed as a comma-separated list. \
Please list the values in the same order that you listed the elements \
and please only enter integers. [ex: for water, type "2,1"] \
Type "quit" to quit. '))
    return numbers

def format_numbers(numbers):
    numbers = numbers.replace(' ','')
    try:
        numbers = numbers.lower()
    except:
        pass
    return numbers


def validate_numbers(numbers):
        if numbers == 'quit' or numbers == '':
            return False
        
        else:
            return True
         

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


def comp_lists(elements_list, numbers_list):
    if len(elements_list) == len(numbers_list):
        return True

    else:
        return False


def zip_lists(elements_list,numbers_list):
    elements_dict = dict(zip(elements_list, numbers_list))
    return elements_dict



def what_calc():
    calc = str(input("Would you like to convert to grams or to moles? \
Enter 'g' for grams and 'm' for moles. "))
    return calc

def clean_what_calc(calc):
    calc = (calc.lower()).replace(' ','')
    return calc

def check_len_what_calc(calc):
    if len(calc) == 1:
        return True
    else:
        return False

def check_what_calc(calc):
    if calc == 'g' or calc == 'm':
        return True
    else:
        return False

def analyze_what_calc(calc):
    if calc == 'g':
        return 'g'
    elif calc == 'm':
        return 'm'


def molar_mass_list(elements_dict,data_table):
    molar_mass_list = []
    for key, value in elements_dict:
        if key in data_table.keys():
            atomic_mass = data_table[key]
            composite_mass = value*atomic_mass
            molar_mass_list.append(composite_mass)
            continue
    print(molar_mass_list)
    return molar_mass_list







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
    elements_list = list_elements(elements)
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
    blah = zip_lists(elements_list, numbers_list)
    print(blah)

#def decision(bool_value,numbers):
    #if bool_value == False:
        #if numbers == 'quit':
            #sys.exit()
        
        #elif numbers == '':
            #pass
    #else:
        #return numbers

def main():
    elements_list = main_elements()
    numbers_list = main_numbers()
    prepare_calc(elements_list, numbers_list)
if __name__ == '__main__':
    main()
         
         
         
         #while elements == '':
         #elements = str(input("I'm sorry, but your input was not \
#of the correct form. Please try again (Type 'quit' to quit.) "))
    #while elements != '':
        #if elements == 'quit':
            #return elements
            #break
            #sys.exit()
        #else:
            #print(elements)
            #return elements
            #clean_elements(elements)
            #return elements
#def check_elements(elements):
    #elements == (elements.lower()).replace(' ','')
    #while elements == '':
        #elements = str(input("I'm sorry, but your input was not \
#of the correct form. Please try again (Type 'quit' to quit.) "))
        #continue
        #while True:
    #while elements == elements:
    #while elements != '':
        #if elements == 'quit':
            #break
        #break
        #elif elements == '':
            #elements = str(input("I'm sorry, but your input was not \
#of the correct form. Please try again (Type 'quit' to quit.) "))
            #continue
        #else:
            #print(elements)
            #return elements
    #return elements



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
        #sys.exit()

        #elif elements == '':
            #elements = str(input("I'm sorry, but your input was not \
#of the correct form. Please try again (Type 'quit' to quit.) "))
            #continue
        
        #else:
            #return elements
#def check_numbers(numbers):
    #try:
        #numbers = numbers.lower()
        #if numbers == 'quit':
            #sys.exit()

        #elif numbers == '':
            #numbers = str(input("I'm sorry, but your input was not \
#of the correct form. Please try again (Type 'quit' to quit.) "))
            #numbers = numbers.replace(' ','')
            #check_numbers(numbers)
    #except:
        #return numbers
        


#def clean_numbers(numbers):
    #numbers_list = []
    #numbers = numbers.replace(' ','')
    #numbers = numbers.split(',')
    #for number in numbers:
        #number = int(number)
        #numbers_list.append(number)
    #return numbers_list

    
#def decision(bool_value,elements):
    #if bool_value == False:
        #if elements == 'quit':
            #sys.exit()
        
        #elif elements == '':
            #pass
    #else:
        #return elements


            #elements = input("I'm sorry, but {i} is not \
#a legitimate atomic symbol. Please re-enter your list of \
#atomic symbols ".format(i = element))
            #elements = check_elements(elements)
            #elements = clean_elements(elements)
            #elements = check_legit(elements,atomic_symbols)
            #break


#def decision(bool_value,numbers):
    #if bool_value == False:
        #if numbers == 'quit':
            #sys.exit()
        
        #elif numbers == '':
            #pass
    #else:
        #return numbers

#def handle_bad_input(elements):
    #if elements == 'quit':
        #sys.exit()

    #else:
        #get_elements()

#def handle_bad_num(numbers):
    #if numbers == 'quit':
        #sys.exit()

    #else:
        #get_numbers
