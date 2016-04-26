#!/usr/bin/env python3.4

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


import unittest

from molecular_form_base_functions import (
        get_elements,
        rem_comm_spaces,
        only_alpha,
        format_input,
        validate_elements,
        list_elements,
        get_numbers,
        only_num,
        comp_lists,
        zip_lists,
        calc_molar_mass,
        what_calc,
        clean_what_calc,
        is_alpha,
        check_len_what_calc,
        check_what_calc,
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
)

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




if __name__=='__main__':
    unittest.main()
