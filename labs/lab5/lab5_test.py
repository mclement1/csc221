#!/usr/bin/env python3
import os
import sys
import inspect
import unittest
import math
from unittest.mock import (
    patch, call,
)

import belhavencs
import belhavencs.harness as harness
from belhavencs.harness import (
    timeout, 
)
from belhavencs import harness

import lab5

class CheckDucklings(unittest.TestCase):
    @unittest.skipIf(hasattr(lab5.ducklings,'skip'), '')
    @patch('lab5.print',create=True)
    def test003_output(self, mock_print):
        '''ducklings: testing output of ducklings

        Your ducklings function doesn't print Ouack

        '''
        lab5.ducklings()
        mock_print.assert_has_calls([call('Ouack')])

    @unittest.skipIf(hasattr(lab5.ducklings,'skip'), '')
    @patch('lab5.print',create=True)
    def test008_output(self, mock_print):
        '''ducklings: testing output of ducklings

        Your ducklings function doesn't print Quack

        '''
        lab5.ducklings()
        mock_print.assert_has_calls([call('Quack')])

    @unittest.skipIf(hasattr(lab5.ducklings,'skip'), '')
    @patch('lab5.print',create=True)
    def test010_output(self, mock_print):
        '''ducklings: testing output of ducklings

        Your ducklings function doesn't output the correct duck names

        '''
        lab5.ducklings()
        calls = [call(v) for v in
                 [l+'ack' if l not in 'QO' else l+'uack'
                  for l in 'JKLMNOPQ']]
        mock_print.assert_has_calls(calls)
        

class CheckCountLetters(unittest.TestCase):
    @unittest.skipIf(hasattr(lab5.count_letters,'skip'), '')
    def test005_test_parameters(self):
        '''count_letters: testing signature for correct parameters

        Your count_letters function is missing two parameters: string
        and char

        '''
        sig = inspect.signature(lab5.count_letters)
        self.assertEqual(['string','char'], list(sig.parameters))

    @unittest.skipIf(hasattr(lab5.count_letters,'skip'), '')
    def test010_test_output(self):
        '''count_letters: testing output of function is an integer

        Your count_letters function is not returning an integer

        '''
        self.assertEqual(type(lab5.count_letters('asdf','a')), int)

    @unittest.skipIf(hasattr(lab5.count_letters,'skip'), '')
    def test015_test_output(self):
        '''count_letters: testing output of function is correct

        Your count_letters function should return 5 for these
        arguments: 'aaaaa','a'

        '''
        self.assertEqual(lab5.count_letters('aaaaa','a'), 5)

    @unittest.skipIf(hasattr(lab5.count_letters,'skip'), '')
    def test020_test_output(self):
        '''count_letters: testing output of function is correct

        Your count_letters function is not returning the correct output

        '''
        for a0,a1 in [('aaaa','a'), ('aaaa','b'), ('abcdabcd','d'),
                      ('asdf','')]:
            self.assertEqual(
                lab5.count_letters(a0,a1),sum(1 for c in a0 if c==a1)
            )

class CheckReverseString(unittest.TestCase):
    @unittest.skipIf(hasattr(lab5.reverse_string,'skip'), '')
    def test010_test_output(self):
        '''reverse_string: testing output of function is a string

        Your reverse_string function not returning a string

        '''
        self.assertEqual(type(lab5.reverse_string('asdf')), str)

    @unittest.skipIf(hasattr(lab5.reverse_string,'skip'), '')
    def test015_test_output(self):
        '''reverse_string: testing output of function is correct

        Your reverse_string function should return 'olleh' for the
        argument: 'hello'

        '''
        self.assertEqual(lab5.reverse_string('hello'), 'olleh')

    @unittest.skipIf(hasattr(lab5.reverse_string,'skip'), '')
    def test020_test_output(self):
        '''reverse_string: testing output of function is correct

        Your reverse_string function is not returning the correct
        output

        '''
        for a0 in ['aaaa','asdf','abcdabcd']:
            self.assertEqual(
                lab5.reverse_string(a0),''.join(reversed(a0))
            )


class CheckIsPalindrome(unittest.TestCase):
    @unittest.skipIf(hasattr(lab5.is_palindrome,'skip'), '')
    def test010_test_output(self):
        '''is_palindrome: testing output of function is a boolean

        Your is_palindrome function not returning a boolean

        '''
        self.assertEqual(type(lab5.is_palindrome('asdf')), bool)

    @unittest.skipIf(hasattr(lab5.is_palindrome,'skip'), '')
    def test015_test_output(self):
        '''is_palindrome: testing output of function is correct

        Your is_palindrome function should return False for the
        argument: 'hello'

        '''
        self.assertEqual(lab5.is_palindrome('hello'),False)

    @unittest.skipIf(hasattr(lab5.is_palindrome,'skip'), '')
    def test016_test_output(self):
        '''is_palindrome: testing output of function is correct

        Your is_palindrome function should return True for the
        argument: 'bananab'

        '''
        self.assertEqual(lab5.is_palindrome('bananab'), True)

    @unittest.skipIf(hasattr(lab5.is_palindrome,'skip'), '')
    def test020_test_output(self):
        '''is_palindrome: testing output of function is correct

        Your is_palindrome function is not returning the correct
        output

        '''
        p = lambda v: ''.join(reversed(v))==v
        for a0 in ['aaaa','asdf','abcddcba','hello','olbbbblo']:
            self.assertEqual(lab5.is_palindrome(a0), p(a0))


class CheckCreateFile(unittest.TestCase):
    def test000_test_existence(self):
        '''create_file: testing existence of create_file

        You haven't created a function named create_file

        '''
        self.assertTrue(hasattr(lab5,'create_file'))
        self.assertTrue(callable(lab5.create_file))

    def test005_test_parameters(self):
        '''create_file: testing signature for correct parameters

        Your create_file function is missing two parameters: string
        and char

        '''
        sig = inspect.signature(lab5.create_file)
        self.assertEqual(['filename','content','N'], list(sig.parameters))

    @patch('lab5.open',create=True)
    def test010_test_output(self, mock_open):
        '''create_file: testing for use of open function

        Your create_file function not use the open function

        '''
        lab5.create_file('test_asdf.txt','data', 5)
        self.assertTrue(mock_open.called)

    @patch('lab5.open',create=True)
    def test011_test_output(self, mock_open):
        '''create_file: testing for use of open function

        Your create_file function not use the open function with the
        correct arguments

        '''
        lab5.create_file('test_asdf.txt','data', 5)
        mock_open.assert_has_calls([call('test_asdf.txt','w')])

    def test015_test_output(self):
        '''create_file: testing output of function is correct

        Your create_file does not create the file with the correct
        content

        '''
        path = '.test_asdfasdfasdf'
        data = 'data'
        N = 5
        lab5.create_file(path,data,N)
        self.assertTrue(os.path.exists(path))
        with open(path) as rfp:
            new = rfp.read()
        self.assertEqual(new, data*N)




def run():
    loader = unittest.TestLoader()

    cases = (CheckDucklings, CheckCountLetters, CheckReverseString,
             CheckIsPalindrome, CheckCreateFile)

    suite = unittest.TestSuite()
    for case in cases:
        tests = loader.loadTestsFromTestCase(case)
        suite.addTests(tests)

    results = harness.TestRunner().run(suite)
    return results

if __name__=='__main__':
    run()

