import unittest
from lab8_2 import (count_letters,
                    reverse_string,
                    is_palindrome,
                    match_ends,
                    front_x,
                    sort_last)



class TestLetterCount(unittest.TestCase):

    def setUp(self):
        pass

    def test_abcd_e(self):
        self.assertEqual(count_letters('abcd','e'),0)

    def test_peanut_t(self):
        self.assertEqual(count_letters('peanut','t'),1)

    def test_happy_p(self):
        self.assertEqual(count_letters('happy','p'),2)


class TestReverseString(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_empty(self):
        self.assertEqual(reverse_string(''),'')

    def test_a(self):
        self.assertEqual(reverse_string('a'),'a')

    def test_horse(self):
        self.assertEqual(reverse_string('horse'),'esroh')

    def test_racecar(self):
        self.assertEqual(reverse_string('racecar'),'racecar')


class TestIsPalindrome(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_empty(self):
        self.assertTrue(is_palindrome(''))

    def test_a(self):
        self.assertTrue(is_palindrome('a'))

    def test_abcddcba(self):
        self.assertTrue(is_palindrome('abcddcba'))

    def test_mountain(self):
        self.assertFalse(is_palindrome('mountain'))


class TestMatchEnds(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_list_1(self):
        self.assertEqual(match_ends(['cat','dog','parrot','hamster']),0)

    def test_list_2(self):
        self.assertEqual(match_ends(['','a','b','c']),0)

    def test_list_3(self):
        self.assertEqual(match_ends(['slips',
                        'runs','trots','walks','canters']),1)

    def test_list_4(self):
        self.assertEqual(match_ends(['pup','pip','par','pat']),2)

    def test_list_5(self):
        self.assertEqual(match_ends(['mom','mum','dad','sis','aa']),5)


class TestFrontX(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_list_1(self):
        self.assertEqual(front_x(['dog','bat','aardvark','cat']),
                        ['aardvark','bat','cat','dog'])

    def test_list_2(self):
        self.assertEqual(front_x(['brazil','argentina','xalapa',
                        'congo','russia']),['xalapa','argentina',
                        'brazil','congo','russsia'])

    def test_list_3(self):
        self.assertEqual(front_x(['cambodia','rwanda','sahara',
                        'xalapa','xanxere','california']),
                        ['xalapa','xanxere','california',
                        'cambodia','rwanda','sahara'])


class TestSortLast(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_list_1(self):
        self.assertEqual(sort_last([(4,5),(0,1),(3,4),(2,3),(1,2)]),
                       [(0,1),(1,2),(2,3),(3,4),(4,5)])

    def test_list_2(self):
        self.assertEqual(sort_last([(3,2),(3,3),(6,0),(1,4)]),
                       [(6,0),(3,2),(3,3),(1,4)])


if __name__ == '__main__':
    unittest.main()
