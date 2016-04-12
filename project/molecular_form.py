#!/usr/bin/env python3.4

import pandas as pd

atomic_symbols = pd.read_csv('periodic_table_data.csv')
#atomic_symbols['x'].str.lower()
atomic_masses = []
print(atomic_symbols) 



def get_elements():
    elements_list = []
    
    elements = str(input('Please list the elements of which \
your molecule is composed as a comma-separated list. \
[ex: for water, type "H,O"] Type "quit" to quit. '))
    
    
    while elements == '':
        elements = str(input("I'm sorry, but your input was not \
of the correct form. Please try again (Type 'quit' to quit.) "))

        
    while elements != '':

        if elements.lower() == 'quit':
            break

        else:
            elements = elements.lower()
            elements = elements.replace(' ','')
            elements = elements.split(',')
            for i in elements:
                elements_list.append(i)
        
        #print(elements_list)
        break
    return elements_list


def check_elements(passed_list):
    print(passed_list)


    

def main():
    passed_list = get_elements()
    check_elements(passed_list)

if __name__ == '__main__':
    main()

    
