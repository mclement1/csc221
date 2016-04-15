#Project Requirements

The grams to mole two-way conversion program shall be able to accept user
input, perform conversions between grams and moles, and output the desired
answer to standard out.

-Accept user input:
    -The program shall be able to accept a list of atomic symbols,
    parse this list, and determine whether the input consists of
    legitimate atomic symbols.

    -The program shall be able to accept a list of numberical values
    relating to the atomic symbols entered previously, parse this list,
    and confirm that the same number of atomic symbols as numerical
    values were entered by the user.

    -The program shall be able to accept user input dictating which
    convnersion the program is to perform (i.e., from grams to moles
    or from moles to grams) as well as the initial value needing
    to be converted.

    -The program shall be able to recognize when the user input is the
    empty string, at which point it will prompt the user to re-enter his
    data.

    -The program shall be able to recognize when the user input is the
    word 'quit', at which point it will exit the program.

-Perform calculations:
    -The program shall be able to look up the atomic masses corresponding
    to the user-entered atomic symbols.

    -The program shall be able to compute the molar mass of the molecule
    in question by adding up the appropriate atomic masses.

    -The program shall be able to convert from grams to moles and from
    moles to grams.

-Output data:
    -The program shall be able to output the result of the conversion
    calculation to standard out.


The grams to mole two-way conversion program shall be able to accept input
from the user in the form of a comma-separated list of element symbols
and a comma-separated list of numerical values relating the number of each
type of element present in the compound of interest. The program shall be
able to recognize when an illegitimate atomic symbol has been entered,
as well as when the length of the list of atomic symbols is not equal to
the length of the list of numerical values.

Based on the user's input, the program shall compute the molar mass of the
compound of interest and then ask the user if he would like to convert to grams
or to moles. Based on the user's answer to this question, the program shall
then prompt the user to enter the numerical value (either in moles or in grams,
as is appropriate) of the quantity of his starting amount of compound.
The program shall then compute the desired quantity and, after outputting the
value to the user's display, the program shall then ask the user if he would
like to perform another calculation or quit the program.

If the user decides to perform another calculation, the program shall ask
the user if he would like to perform an additional calculation on the same
molecule or if he would like to input a new molecule. The program will then
repeat the appropriate steps relative to the input given to the user. If the
user wishes to exit the program at any point, he may do so by typing 'quit.'