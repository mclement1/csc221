#Project Specifications

##Writing the code
In order to fulfill the requirements for the grams to mole two-way conversion
program as listed in requirements.md, the program shall be able to collect
user input concerning the molecule of interest and confirm that the input is of
the right format. The program shall then compute the molar mass of the compound,
using atomic mass data organized with the pandas module.

The program shall then be able to collect input from the user concerning
the type of calculation the user would like to perform (i.e., grams to moles
or moles to grams) and then perform the appropriate unit conversion.

Finally, after outputting the result of the conversion to the user's display,
the program shall ask the user if he would like to perform another calculation
or quit the pogram, and in the case that the user decides to perform another
calculation, the program shall collect input from the user concerning whether
he would like to input a new molecule or perform another calculation on the
same molecule.

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

-Test to check that, if the user enters the word 'quit' at any point
(regardless of capitalization or whitespace), the program will exit

-Test to check that the program correctly gathers atomic mass information
from the lookup table

-Test to check that the program correctly performs addition of atomic masses

-Test to check that the program correctly performs conversions from grams to
moles

-Test to check that the program correctly performs conversions from moles to
grams

In addition, integration testing shall be performed via usage model testing.
