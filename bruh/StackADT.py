'''
CIS 120 - Intro to Data Structures, UMA, Spring 2023

Program: Stack.py
Author:
Date Created:

Implement a linked-list variant of a stack abstract data type.'''

from ListNode import ListNode

class Stack():

    def __init__(self):
        '''creates an empty LIFO stack'''

    def push(self, item):
        '''pre: none
        post: places item on top of the stack'''

    def pop(self):
        '''pre: stack is not empty; IndexError is raised if empty
        post: removes and returns the top element of the stack'''

    def top(self):
        '''pre: stack is not empty; IndexError is raised if empty
        post: returns the top element of the stack without removing it'''

    def size(self):
        '''pre: none
        post: returns the number of elements in the stack'''

def main():
    '''  simple test of my stack '''
    myStack = Stack()
    print("Size: ", myStack.size(), "(should be 0)")
    myStack.push(2)
    myStack.push(4)
    myStack.push(6)
    myStack.push(8)
    print("Size: ", myStack.size(), "(should be 4)")
    print("Top:  ", myStack.top(), "(should be 8)")
    print("Pop:  ", myStack.pop(), "(should be 8)")
    print("Pop:  ", myStack.pop(), "(should be 6)")
    print("Top:  ", myStack.top(), "(should be 4)")
    print("Size: ", myStack.size(), "(should be 2)")

if __name__ == "__main__":
    main()
