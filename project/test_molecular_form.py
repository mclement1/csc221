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

from molecular_form import (
                            get_elements,
                            format_elements,
                            validate_elements,
                            list_elements,
                            format_numbers,
                            validate_numbers,
                            list_numbers,
                            comp_lists,
                            clean_what_calc,
                            check_len_what_calc,
                            check_what_calc,
                            analyze_what_calc,
                            molar_mass_list,
                            #check_legit,
                            #atomic_symbols,
                            #atomic_masses,
                            #data_table,
                            #check_elements,
                            #clean_elements,
                            #check_legit,
                            #get_numbers,
                            #check_numbers,
                            #clean_numbers,
)

class TestFormatElements(unittest.TestCase):

    def test_quit(self):
        self.assertEqual(format_elements(' Q   uI   t'),'quit')

    def test_NaOH(self):
        self.assertEqual(format_elements('Na,  O  , h'),'na,o,h')


class TestValidateElements(unittest.TestCase):

    def test_quit(self):
        self.assertFalse(validate_elements('quit'))

    def test_empty(self):
        self.assertFalse(validate_elements(''))

    def test_methanol(self):
        self.assertTrue(validate_elements('c,h,o'))


class TestListElements(unittest.TestCase):

    def test_sulfuric_acid(self):
        self.assertEqual(list_elements('h,s,o',atomic_symbols),['h','s','o'])

    def test_random(self):
        self.assertEqual(list_elements('h,br,aa,li',atomic_symbols),['h','br','li'])

    def test_all_fake(self):
        self.assertEqual(list_elements('aa,bb,cc,dd',atomic_symbols),[])



class TestFormatNumbers(unittest.TestCase):

    def test_string_1(self):
        self.assertEqual(format_numbers('4  , 3, 5,7'),'4,3,5,7')

    def test_quit(self):
        self.assertEqual(format_numbers('q  U  I t   '),'quit')
        
    def test_empty(self):
        self.assertEqual(format_numbers(''),'')



class TestValidateNumbers(unittest.TestCase):

    def test_quit(self):
        self.assertFalse(validate_numbers('quit'))

    def test_empty(self):
        self.assertFalse(validate_numbers(''))

    def test_string_1(self):
        self.assertTrue(validate_numbers('3,6,2,7,4'))



class TestListNumbers(unittest.TestCase):

    def test_list_1(self):
        self.assertEqual(list_numbers('4,2,7,5,7,3'),[4,2,7,5,7,3])

    def test_list_2(self):
        self.assertEqual(list_numbers('4,7,2,3.6,8,2.8'),[4,7,2,8])

    def test_list_3(self):
        self.assertEqual(list_numbers('4.5,3.2,5.6,7.4'),[])



class TestCompLists(unittest.TestCase):

    def test_one(self):
        elements_list = ['h','he','li']
        numbers_list = [2,3,4]
        self.assertTrue(comp_lists(elements_list, numbers_list))

    def test_two(self):
        elements_list = ['h','he','li','be']
        numbers_list = [3,5,1]
        self.assertFalse(comp_lists(elements_list, numbers_list))



class TestCleanWhatCalc(unittest.TestCase):

    def test_grams(self):
        self.assertEqual(clean_what_calc('G   r  AmS  '),'grams')

    def test_moles(self):
        self.assertEqual(clean_what_calc('  mO  lES'),'moles')




class TestCheckLenWhatCalc(unittest.TestCase):

    def test_empty(self):
        self.assertFalse(check_len_what_calc(''))

    def test_g(self):
        self.assertTrue(check_len_what_calc('g'))

    def test_grams(self):
        self.assertFalse(check_len_what_calc('grams'))




class TestCheckWhatCalc(unittest.TestCase):
    
    def test_g(self):
        self.assertTrue(check_what_calc('g'))

    def test_m(self):
        self.assertTrue(check_what_calc('m'))

    def test_a(self):
        self.assertFalse(check_what_calc('a'))




class TestAnalyzeWhatCalc(unittest.TestCase):

    def test_g(self):
        self.assertEqual(analyze_what_calc('g'),'g')

    def test_m(self):
        self.assertEqual(analyze_what_calc('m'),'m')


class TestMolarMassList(unittest.TestCase):

    def test_dict_one(self):
        elements_dict = {'h':1,'he':2,'li':3}
        self.assertEqual(molar_mass_list(elements_dict,data_table), \
[1.007944,8.0052044,20.8236])








if __name__=='__main__':
    unittest.main()
