#Project Specifications

##Writing the code

###Accepting user input

Input from the user shall be collected by means of the command-line interface
and the Python built-in input function. At every point in the program where
user input is required, the user shall be given an appropriate prompt to
guide him in the type and format of the input to be entered.

If the given input does not meet the formatting requirements, the program
shall further prompt the user to re-enter his data, doing so until the data
is of the right format or until the user has entered 'quit.'

At every point where input is requested, the user shall be able to enter the
word 'quit,' which shall end the program by calling the exit() function from
the sys module.

###Performing calculations

The atomic symbols and masses shall be contained in a dictionary, with the
symbols serving as the keys and the masses serving as the values. The atomic
symbols shall be entirely in lowercase to provide for ease of comparison
between the user input and the keys.

Given the simplicity of the calculations being performed, the standard Python
library of mathematical functions shall ssuffice.

###Outputting data

The result of the desired calculation shall be outputted to standard out.


##Testing the code
In order to test the code, unit tests shall be employed. The following unit
tests shall be written:

-Test to check that incorrectly formatted molecular input data is recognized
before any calculations are performed

-Test to check that illegitimate atomic symbols are recognized before any
calculations are performed

-Test to check that the length of the list of atomic symbols is the same as
the length of the list of numerical values corresponding to those atomic
symbols before any calculations are performed

-Test to check that, if the user enters the word 'quit' at any input prompt
(regardless of capitalization or whitespace), the program will exit

-Test to check that the program correctly gathers atomic mass information
from the lookup table

-Test to check that the program correctly performs addition of atomic masses

-Test to check that the program correctly performs conversions from grams to
moles

-Test to check that the program correctly performs conversions from moles to
grams

In addition, integration testing shall be performed via usage model testing.
