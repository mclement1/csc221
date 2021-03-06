#!/usr/bin/env python3.4

import unittest

from base_functions import (
        get_elements,
        rem_comm_spaces,
        only_alpha,
        format_input,
        get_numbers,
        only_num,
        comp_lists,
        zip_lists,
        calc_molar_mass,
        what_calc,
        clean_what_calc,
        is_alpha,
        check_len_what_calc,
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

class TestRemCommSpaces(unittest.TestCase):

    def test_one(self):
        self.assertEqual(rem_comm_spaces(''),'')

    def test_two(self):
        self.assertEqual(rem_comm_spaces(' , , , , '),'')

    def test_three(self):
        self.assertEqual(rem_comm_spaces(' T! u,/  L'),'T!u/L')

class TestOnlyAlpha(unittest.TestCase):

    def test_one(self):
        self.assertFalse(only_alpha(''))

    def test_two(self):
        self.assertFalse(only_alpha('fhe34sJ'))

    def test_three(self):
        self.assertFalse(only_alpha('!?sdfdsf$'))

    def test_four(self):
        self.assertTrue(only_alpha('fsFGSDF'))

class TestFormatInput(unittest.TestCase):

    def test_one(self):
        self.assertEqual(format_input('fs FSE, sljf  ,'),'fsfse,sljf,')

class TestOnlyNum(unittest.TestCase):

    def test_one(self):
        self.assertTrue(only_num('34205'))

    def test_two(self):
        self.assertFalse(only_num('3.455'))

    def test_three(self):
        self.assertFalse(only_num('23434f234324'))

class TestCompLists(unittest.TestCase):

    def test_one(self):
        self.assertTrue(comp_lists(['df','sdf','fd'],[3,4,5]))

    def test_two(self):
        self.assertFalse(comp_lists(['df','sdf','sdf'],[4,5]))

class TestZipLists(unittest.TestCase):

    def test_one(self):
        self.assertTrue(zip_lists(['wer','fd','sd'],[5,2,6]) \
== {'wer':5,'fd':2,'sd':6})

class TestCalcMolarMass(unittest.TestCase):

    def test_one(self):
        elements_dict = {'h':2,'he':3,'md':2}
        self.assertAlmostEqual(calc_molar_mass(elements_dict,data_table),
                                530.0236946)

    def test_two(self):
        elements_dict = {'h':3,'be':2,'c':6}
        self.assertAlmostEqual(calc_molar_mass(elements_dict,data_table),
                                93.1128766)

class TestCleanWhatCalc(unittest.TestCase):

    def test_one(self):
        self.assertEqual(clean_what_calc('  f,d,g  .dfs '),'f,d,g.dfs')

class TestIsAlpha(unittest.TestCase):

    def test_one(self):
        self.assertTrue(is_alpha('sdfweSDF'))

    def test_two(self):
        self.assertFalse(is_alpha(''))

    def test_three(self):
        self.assertFalse(is_alpha('sdf 434 df'))

    def test_four(self):
        self.assertFalse(is_alpha('@#@$sfds'))


class TestCheckLenWhatCalc(unittest.TestCase):

    def test_one(self):
        self.assertTrue(check_len_what_calc('g'))

    def test_two(self):
        self.assertFalse(check_len_what_calc(''))

    def test_three(self):
        self.assertFalse(check_len_what_calc('sddfsdf'))

class TestAnalyzeWhatCalc(unittest.TestCase):

    def test_one(self):
        self.assertEqual(analyze_what_calc('g'),'g')

    def test_two(self):
        self.assertEqual(analyze_what_calc('m'),'m')

class TestFormatMoles(unittest.TestCase):

    def test_one(self):
        self.assertEqual(format_moles('    4.  235 32'),'4.23532')

class TestConfirmFloatMoles(unittest.TestCase):

    def test_one(self):
        self.assertTrue(confirm_float_moles('3.42342'))

    def test_two(self):
        self.assertFalse(confirm_float_moles('3.43gn5'))


class TestMakeMolesFloat(unittest.TestCase):

    def test_one(self):
        self.assertEqual(make_moles_float('4.2342'),4.2342)

    def test_two(self):
        self.assertEqual(make_moles_float('4'),4)

class TestFormatGrams(unittest.TestCase):

    def test_one(self):
        self.assertEqual(format_grams('s sfs , s'),'ssfs,s')


class TestConfirmFloatGrams(unittest.TestCase):

    def test_one(self):
        self.assertTrue(confirm_float_grams('3.45235'))

    def test_two(self):
        self.assertTrue(confirm_float_grams('2'))

    def test_three(self):
        self.assertFalse(confirm_float_grams('sdfsd343'))


class TestMakeGramsFloat(unittest.TestCase):

    def test_one(self):
        self.assertEqual(make_grams_float('4.3242'),4.3242)

    def test_two(self):
        self.assertEqual(make_grams_float('69'),69)


class TestHandleNotFloat(unittest.TestCase):

    def test_one(self):
        self.assertTrue(handle_not_float('quit'))

    def test_two(self):
        self.assertFalse(handle_not_float('sfds'))

    def test_three(self):
        self.assertFalse(handle_not_float('234wfsdf'))

    def test_four(self):
        self.assertFalse(handle_not_float('wer@#$@534'))


class TestMolesToGrams(unittest.TestCase):

    def test_one(self):
        moles = 3.456
        molar_mass = 2.421
        self.assertAlmostEqual(moles_to_grams(moles,molar_mass),8.366976)


class TestGramsToMoles(unittest.TestCase):

    def test_one(self):
        grams = 5.321
        molar_mass = 89.123
        self.assertAlmostEqual(grams_to_moles(grams, molar_mass), 0.059704005)




if __name__=='__main__':
    unittest.main()
