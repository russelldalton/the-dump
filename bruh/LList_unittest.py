'''
 CIS 120, Intro to Data Structures, Assignment 4;  Spring 2023

 Program: LList_unittest.py
 Author:
 Date Created:

 Brief Description:
'''

import sys
import unittest

import LList as ll

def _newLL(sequence=()):
    ''' private function to create a new linked list for testing'''
    theLL = ll.LList()
    for item in sequence:
        theLL.append(item)
    return theLL

class LListTest(unittest.TestCase):

    _LL1 = _newLL( (12,11,7,1,23,25,4,8,5,4,8,17) )
    _LL2 = _newLL( (2,12,11,7,23,25,4,8,5,4,8,30) )
    _LL3 = _newLL( (31,12,11,7,23,25,4,8,5,4,8,3) )
       
    def testMin(self):
        '''  Test the .min() method '''
        self.assertEqual(self._LL1.min(), 1)    # in the middle
        self.assertEqual(self._LL2.min(), 2)    # at the start
        self.assertEqual(self._LL3.min(), 3)    # at the end

    def testMax(self):
        '''  Test the .max() method '''
        self.assertEqual(self._LL1.max(), 1)    # in the middle
        self.assertEqual(self._LL2.max(), 2)    # at the start
        self.assertEqual(self._LL3.max(), 3)    # at the end
        
    
    #def testCount(self):
        ''' test the .count(value) method '''
        #self.assertEqual(self._LL1.count())    # in the middle
        #self.assertEqual(self._LL2.count())    # at the start
        #self.assertEqual(self._LL3.count())    # at the end
        

   # def testIndex(self):
        ''' Test the .index(value, <start>) method '''
        #self.assertEqual(self._LL1.index())    # in the middle
        #self.assertEqual(self._LL2.index())    # at the start
        #self.assertEqual(self._LL3.index())    # at the end
        

    #def testRemove(self):
        ''' test the .remove(value) method '''
        #self.assertEqual(self._LL1.remove())    # in the middle
        #self.assertEqual(self._LL2.remove())    # at the start
        #self.assertEqual(self._LL3.remove())    # at the end
        

       
def main(argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
