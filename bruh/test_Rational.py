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
        r2 = Rational(3,4)
        
        
        
        
        
        r3 = r1 + r2 
        self.assertEqual(str(r3), '4/4')
        
        with self.assertRaises(TypeError):
            r3 = r1 + 4

    def testsub(self):
        r1 = Rational(3,5)
        r2 = Rational(2,5)
        r3 = r1 -r2 

        self.assertEqual(str(r3),'1/5')
        with self.assertRaises(TypeError):
            r3 = r1 - 5

    def testdiv(self):
        r1 = Rational(2,3)
        r2 = Rational(3,5)
        
        r3 = r1 % r2 
        self.assertEqual(str(r3), '10/9')

        with self.assertRaises(TypeError):
            r3 = r1 % 3

    def testlt(self):
        r1 = Rational(1,3)
        r2 = Rational(1,2)

        if r1 < r2:
            r3 = r1 
        elif r2 < r1:
            r3 = r2 

        self.assertEqual(str(r3), '1/3')
        with self.assertRaises(TypeError):
            r3 = r2

    def testgt(self):
        r1 = Rational(1,3)
        r2 = Rational(1,2)

        if r1 > r2:
            r3 = r1 
        elif r2 > r1:
            r3 = r2 

        self.assertEqual(str(r3), '1/2')
        with self.assertRaises(TypeError):
            r3 = r2

    def testeq(self):
        r1 = Rational(1,2)
        r2 = Rational(2,4)
        if r1 == r2:
            r3 = True
        else:
            r3 = False

        self.assertEqual(str(r3), 'true')
        with self.assertRaises(TypeError):
            r3 = False
        
    
    # TODO -- add tests for the other methods in Rational.py.
    # there should be a unique test defined for each method
        
def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
