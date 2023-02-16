'''
Program: Rational.py, SPring 2023
Author:jobe odulio
Date:2/14/2023

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
        if not isinstance(other, Rational):
            raise TypeError('parameters must be Rational numbers')
        n1 = self.num*other.den
        n2 = other.num*self.den
 
        
        num = n1 + n2
        den = self.den*other.den
            
            
       
        return Rational(num,den )
        '''adds the fractions 
        pre: find the lcm to make the denominators equal  
        post: adds the fractions after lcm conversion'''

    def __sub__(self, other):
        sub = self.num - other.num
        if not isinstance(other, Rational):
            raise TypeError('parameters must be Rational numbers')
        n1 = self.num*other.den
        n2 = other.num*self.den
        sub = n1- n2
        den = self.den*other.den 
        return Rational(sub, den)
        '''subtracts the fractions 
        pre: find the lcm to make the denominators equal  
        post: subtracts the fractions after lcm conversion'''
    def __truediv__(self, other):
        divn = self.num * other.den
        divd = self.den * other.num

        return Rational(divn, divd)
        '''divides the fractions by multipying self by the recipricol of other'''

    # NOTE: These next six methods return a boolean, either True or False
    
    def __lt__(self, other):
            
        if not isinstance(other, Rational):
            raise TypeError('parameters must be Rational numbers')
        
        n1 = self.num*other.den
        n2 = other.num*self.den
        #multiply the num by the den 
        
        if n1 < n2:
            n = n1
        elif n1 > n2:
            n = n1
        d = self.den*other.den
        #finds lcm
        print ('smallest')
        return Rational(n, d)
        '''this function finds the smallest fraction by compairing both numerators '''

    def __gt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('parameters must be Rational numbers')
        n1 = self.num*other.den
        n2 = other.num*self.den

        
        if n1 > n2:
            n = n1
        elif self.num < other.num:
            n = n2
        d = self.den*other.den
        #finds lcm 
        print ('greatest')
        return Rational(n,d)
        '''this function finds the greatest fraction by compairing both numerators '''

    def __le__(self, other):
        
        if not isinstance(other, Rational):
            raise TypeError('parameters must be Rational numbers')
        n1 = self.num*other.den
        n2 = other.num*self.den
        if n1 <= n2:
            n = n1
        elif n1 >= n2:
            n = n2
        d = self.den*other.den
        print ('min')
        return Rational(n,d)


    def __ge__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('parameters must be Rational numbers')
        n1 = self.num*other.den
        n2 = other.num*self.den
        if n1 >= n2:
            n = n1
        elif n1 <= n2:
            n = n2
        d = self.den*other.den
        print ('max')
        return Rational(n,d)
    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('parameters must be Rational numbers')
        n1 = self.num*other.den
        n2 = other.num*self.den
        d = self.den*other.den
        if n1 == n2 :
            print ('they are equivelent')
            return Rational(n1, d)
        else:
            pass
    
    
    def __ne__(self, other):
        if not isinstance(other, Rational):
            raise TypeError('parameters must be Rational numbers')
        n1 = self.num*other.den
        n2 = other.num*self.den
        d = self.den*other.den
        if n1 != n2 :
            print ('they are not equivelent')
            return Rational(n1, d)
        else:
            pass
def main():
    n = Rational(3,4)
    m = Rational(4,5)
    print (Rational.__mul__(n,m))
    print (Rational.__add__(n,m))
    print (Rational.__sub__(n,m))
    print (Rational.__truediv__(n,m))
    print (Rational.__lt__(n,m))
    print (Rational.__gt__(n,m))
    print (Rational.__le__(n,m))
    print (Rational.__ge__(n,m))
    print (Rational.__eq__(n,m))
    print (Rational.__ne__(n,m))
    
    
main()


