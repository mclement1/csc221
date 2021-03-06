#Project Requirements

The grams to mole two-way conversion program shall be able to accept user
input, perform conversions between grams and moles, and output the desired
answer to standard out.

1. Accept user input:

    -The program shall be able to accept a list of atomic symbols,
    parse this list, and determine whether the input consists of
    legitimate atomic symbols.

    -The program shall be able to accept a list of numerical values
    relating to the atomic symbols entered previously, parse this list,
    and confirm that the same number of atomic symbols as numerical
    values was entered by the user.

    -The program shall be able to accept user input dictating which
    conversion the program is to perform (i.e., from grams to moles
    or from moles to grams) as well as the initial value needing
    to be converted.

    -The program shall be able to recognize when the user input is the
    empty string, at which point it shall prompt the user to re-enter his
    data.

    -The program shall be able to recognize when the user input is the
    word 'quit', at which point it shall exit the program.

2. Perform calculations:

    -The program shall be able to look up the atomic masses corresponding
    to the user-entered atomic symbols.

    -The program shall be able to compute the molar mass of the molecule
    in question by adding up the appropriate atomic masses.

    -The program shall be able to convert from grams to moles and from
    moles to grams.

3. Output data:

    -The program shall be able to output the result of the conversion
    calculation to standard out.


