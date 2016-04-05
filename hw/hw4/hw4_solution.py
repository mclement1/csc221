def is_odd(number):
    try:
        return number % 2 ==1
    except int(number) != number:
        return TypeError

    #if number == int(number):
        #return number % 2 == 1
    #else:
        #raise TypeError

def is_even(number):
    return number % 2 == 0
