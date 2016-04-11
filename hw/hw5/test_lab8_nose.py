#import lab8
from nose.tools import (assert_equal,
                       assert_not_equal,
                       assert_true,
                       assert_false)

#Test count_letters function
from lab8_2 import count_letters

def test_blank():
    assert_equal(count_letters('','a'), 0)

def test_none():
    assert_equal(count_letters('none','a'), 0)

def test_potato():
    assert_equal(count_letters('potato','p'), 1)

def test_fuzzy():
    assert_equal(count_letters('fuzzy','z'), 2)


#Test reverse_string function
from lab8_2 import reverse_string

def test_empty():
    assert_equal(reverse_string(''), '')

def test_a():
    assert_equal(reverse_string('a'), 'a')

def test_camper():
    assert_equal(reverse_string('camper'), 'repmac')

def test_racecar():
    assert_equal(reverse_string('racecar'), 'racecar')


#Test is_palindrome funtion
from lab8_2 import is_palindrome

def test_empty_string():
    assert_true(is_palindrome(''))

def test_b():
    assert_true(is_palindrome('b'))

def test_racecar():
    assert_true(is_palindrome('racecar'))

def test_captain():
    assert_false(is_palindrome('captain'))


#Test match_ends function
from lab8_2 import match_ends

def test_list_1():
    assert_equal(match_ends(['','a','cat','dog','hat']), 0)

def test_list_2():
    assert_equal(match_ends(['pop','jump','hop','skip','b']), 1)

def test_list_3():
    assert_equal(match_ends(['cat','dog','mom','dad']), 2)

def test_list_4():
    assert_equal(match_ends(['dad','sings','songs','sometimes','aa']), 5)


#Test front_x function
from lab8_2 import front_x

def test_list_one():
    assert_equal(front_x(['fish','frog','turkey','cow']),
                ['cow','fish','frog','turkey'])

def test_list_two():
    assert_equal(front_x(['pizza','wheel','saucer','xylophone','circle']),
                ['xylophone','circle','pizza','saucer','wheel'])

def test_list_three():
    assert_equal(front_x(['xxx','aaa','ttt','yyy','xxz','xxzy']),
                ['xxx','xxz','xxzy','aaa','ttt','yyy'])


#Test sort_last function
from lab8_2 import sort_last

def test_list_uno():
    assert_equal(sort_last([(5,5),(2,3),(1,0),(4,6)]),
                [(1,0),(2,3),(5,5),(4,6)])



