'''
CIS 120 - Intro to Data Structures, UMA, Spring 2023

Program: MyQueueADT.py
Author:
Date Created:

Implement a linked-list variant of a queue abstract data type'''

from ListNode import ListNode

class Queue():

    def __init__(self):
        '''create an empty FIFO queue'''

    def enqueue(self, item):
        '''pre: none
        post: item is added to the queue'''

    def dequeue(self):
        '''pre: queue is not empty; IndexError is raised if empty
        post: removes and returns first item in the queue'''
       
    def front(self):
        '''pre: queue is not empty; IndexError is raised if empty
        post: returns first item in the queue without removing it'''

    def size(self):
        '''pre: none      
        post: returns number of items in the queue'''

def main():
    '''  simple test of my queue '''
    myQueue = Queue()
    print("Size:    ", myQueue.size(), "(should be 0)")
    myQueue.enqueue(2)
    myQueue.enqueue(4)
    myQueue.enqueue(6)
    myQueue.enqueue(8)
    print("Size:    ", myQueue.size(), "(should be 4)")
    print("Front:   ", myQueue.front(), "(should be 2)")
    print("DeQueue: ", myQueue.dequeue(), "(should be 2)")
    print("DeQueue: ", myQueue.dequeue(), "(should be 4)")
    print("Front:   ", myQueue.front(), "(should be 6)")
    print("Size:    ", myQueue.size(), "(should be 2)")

if __name__ == "__main__":
    main()

     
