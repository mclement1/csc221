# --------------------------------------------------------------------
# Problem 1
# 
# Fix ducklings' names
# 
# In Robert McCloskey’s book Make Way for Ducklings, the names of the
# ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and
# Quack. This loop tries to output these names in order.
# 
# Of course, that’s not quite right because Ouack and Quack are
# misspelled. Can you fix it?

def ducklings():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        if letter in ["O", "Q"]:
            print(letter + "u" + suffix)

        else:
            print(letter + suffix)


# --------------------------------------------------------------------
# Problem 2
# 
# Letter count
#
# Modify the count_letters function below so that:
#
# 1. It has two parameters: string and char
# 2. It implements the functionality specified in the comments
#
# Essentially, the function is returning the number of occurances of the
# parameter char in the parameter string.

def count_letters(string, char): # need two parameters here: string and char
    count = 0
    # initialize the variable count to zero
    for c in string:
        if c == char:
            count += 1
        # if c is equal to char then,
        #     add one to count
        pass  
    return count
    # return the count variable


# --------------------------------------------------------------------
# Problem 3
#
# Reversing a string
# 
# Complete the following function such that it reverses the parameter
# string.

def reverse_string(string):
    rev_string = ''
    for c in reversed(string):
        rev_string = rev_string + c
    return rev_string
    # initialize the variable rev_string to ''
    # for each c in string 
        # add c to the beginning of rev_string
    # return the rev_string variable

    #pass # this line can be removed after you have your other code


# --------------------------------------------------------------------
# Problem 4
# 
# Checking for palindromes
# 
# Complete the following such that it correctly determines whether the
# given parameter, string, is a palindrome
# 

def is_palindrome(string):
    mod_string = string.lower()
    mod_string = mod_string.translate('.,!?"\'')
    mod_string = mod_string.replace(" ", "")
    rev_mod_string = reverse_string(mod_string)
    if rev_mod_string == mod_string:
        return True
    else:
        return False

    #pass
    #if rev_mod_string == mod_string:
        #return True
    #else:
        #return False
    #if mod_string == rev_mod_string:
        #return True
    #else:
        #return False
    #pass


# --------------------------------------------------------------------
# Problem 5
# 
# Create a new file with content
# 
# Create a new function named create_file that takes three parameters:
# 
# - filename (str): name of the file to create
# - content (str): data to put into the file
# - N (int): number of times to repeat the given content
#
# The function should create a new file with the the given filename
# and it should populate this file with the given content duplicated N
# times.

def create_file(filename, content, N):
    new_file = open(filename, 'w')
    for i in range(0, N):
        new_file.write(content)
    new_file.close


def main():
    ducklings()
    count_letters()
    reverse_string()
    is_palindrome()
    create_file()

if __name__=='__main__':
    import lab5_test
    lab5_test.run()



