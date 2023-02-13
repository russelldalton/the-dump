'''
Program: test_rational.py, Spring 2023
Author:
Date:

A set of unit tests for our Rational ADT
'''

import sys
import unittest

from Rational import *

class RationalTest(unittest.TestCase):
       
    def testConstructorOneInt(self):
        r = Rational(-3)
        self.assertEqual(str(r), '-3/1')
       
    def testConstructorTwoInt(self):
        r = Rational(3, 4)
        self.assertEqual(str(r), '3/4')

    def testConstructorMalformed(self):
        with self.assertRaises(ValueError):
            Rational(2,0)   # note the denominator==0, this is bad
        with self.assertRaises(TypeError):
            Rational("2")       # note we are passing a string
        with self.assertRaises(TypeError):
            Rational(2.2)       # A float is also wrong
        with self.assertRaises(TypeError):
            Rational(2, 2.2)    # even in the denominator
        
    def testMul(self):
        r1 = Rational(1, 3)
        r2 = Rational(2, 5)
        r3 = r1 * r2
        self.assertEqual(str(r3), '2/15')

        with self.assertRaises(TypeError):
            r3 = r1 * 2
    def testadd(self):
        r1 = Rational(1,4)
        r2 = Rational(3,5)
        r3 = r1 + r2 
        self.assertEqual(str(r3), '17/20')
        
        with self.assertRaises(TypeError):
            r3 = r1 +
    # TODO -- add tests for the other methods in Rational.py.
    # there should be a unique test defined for each method
        
def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
