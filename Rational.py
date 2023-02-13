'''
Program: Rational.py, SPring 2023
Author:
Date:

An ADT implementaion of a rational (real) number.
Demonstrates operator overloading
'''

class Rational():

    def __init__(self, num = 0, den = 1):

        '''creates a new Rational object
        pre: num and den are integers
        post: creates the Rational object num / den'''

        if not isinstance(num, int):
            raise TypeError("numerator must be an integer")
        if not isinstance(den, int):
            raise TypeError("denominator must be an integer")
        if den == 0:
            raise ValueError("denominator may not equal 0")
        
        self.num = num
        self.den = den

    def __str__(self):

        '''return string for printing
        pre: self is Rational object
        post: returns a string representation self'''
        
        return str(self.num) + '/' + str(self.den)

    def __mul__(self, other):

        '''* operator
        pre: self and other are Rational objects
        post: returns Rational product: self * other'''

        if not isinstance(other, Rational):
            raise TypeError('parameters must be Rational numbers')

        num = self.num * other.num
        den = self.den * other.den
        return Rational(num, den)

                
    #TODO - Complete the following methods, inclduing their doc string and
    #       testing of any preconditions

    def __add__(self, other):
        addn = self.num + other.num
        while other.den:
            self.den, other.den = other.den%self.den
        
       
        return Rational(addn,self.den )

    def __sub__(self, other):
        sub = self.num - other.num
        while other.den:
            self.den, other.den = other.den%self.den
        return Rational(sub, self.den)
    def __truediv__(self, other):
        divn = self.num * other.den
        divd = self.den * other.num

        return Rational(divn, divd)

    # NOTE: These next six methods return a boolean, either True or False
    
    def __lt__(self, other):
            
        while other.den:
            self.den, other.den = other.den%self.den
        if self.num < other.num:
            n = self.num 
        elif self.num > other.num:
            n = other.num
        if self.den < other.den:
            d = self.den 
        elif self.den > other.den:
            d = other.den 
        return Rational(n, d)

    def __gt__(self, other):
        while other.den:
            self.den, other.den = other.den%self.den
        if self.num > other.num:
            n = self.num 
        elif self.num < other.num:
            n = other.num
        if self.den > other.den:
            d =self.den 
        elif self.den < other.den:
            d = other.den 
        return Rational(n,d)

    def __le__(self, other):
        
        while other.den:
            self.den, other.den = other.den%self.den
        if self.num <= other.num:
            n = self.num
        elif self.num >= other.num:
            n = other.num 
        if self.den <= other.den:
            d = self.den
        elif self.den >= other.den:
            d = other.den
        return Rational(n,d)


    def __ge__(self, other):
        while other.den:
            self.den, other.den = other.den%self.den
        if self.num >= other.num:
            n = self.num
        elif self.num <= other.num:
            n = other.num 
        if self.den >= other.den:
            d = self.den
        elif self.den <= other.den:
            d = other.den
        return Rational(n,d)
    def __eq__(self, other):
        while other.den:
            self.den, other.den = other.den%self.den
        if self.num == other.num or self.den == other.den:
            return Rational(self.num, self.den)
    
    
    def __ne__(self, other):
        while other.den:
            self.den, other.den = other.den%self.den
        if self.num != other.num or self.den != other.den:
            return Rational(self.num, self.den)
def main():
    return Rational(3,4)
    
    
main()


