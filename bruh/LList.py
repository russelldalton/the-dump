'''LList.py - CIS120, Intro to Data Structures;  Spring 2023

 Program: LList.py
 Author:
 Date Created:

 Brief Description:
'''

from ListNode import ListNode

class LList():

    def __init__(self):
        """create an LList """

        self.head = None
        self.size = 0

    def __len__(self):

        '''post: returns number of items in the list'''

        return self.size

    def append(self, x):

        '''appends x onto end of the list
        post: x is appended onto the end of the list'''

        # create a new node containing x
        newNode = ListNode(x)

        # add it to the end of the list
        if self.head is None:
            # empty list
            self.head = newNode
        else:
            # non-empty list
            curr = self.head
            while curr.link is not None:
                curr = curr.link
            curr.link = newNode
                
        self.size += 1

    def __str__(self):

        ''' Hook method which returns the string representation of
            our linked list.   '''

        retstr = "< "
        curr = self.head
        while curr is not None:
            retstr += str(curr.item)
            if curr.link is not None:
                retstr += ", "
            curr = curr.link
        retstr +=" >"

        return retstr

    def pop(self, i=None):

        ''' Returns and remove at position i.
            If i is not specified, return last item
            Pre: the list has at least one item
            Post: the item is removed and returned'''

        assert self.size > 0 and (i is None or (0 <= i < self.size))
        
        if i is None: i = self.size-1
                            
        if i == 0:  # removing the first item
            item = self.head.item
            self.head = self.head.link
        else:
            # removing from within the list
            node = self._find(i-1)
            item = node.link.item
            node.link = node.link.link
            
        self.size -= 1
        
        return item
        
    def _find(self, position):

        '''private method that returns node that is at location position
        in the list (0 is first item, size-1 is last item)
        pre: 0 <= position < self.size
        post: returns the ListNode at the specified position in the
        list'''
        
        assert 0 <= position < self.size

        curr = self.head
        currpos = 0

        while currpos < position:
            curr = curr.link
            currpos += 1
            
        return curr

    def __getitem__(self, position):

        '''return data item at location position
        pre: 0 <= position < size
        post: returns data item at the specified position'''

        node = self._find(position)
        return node.item
    
    def __setitem__(self, position, value):

        '''set data item at location position to value
        pre: 0 <= position < self.size
        post: sets the data item at the specified position to value'''

        node = self._find(position)
        node.item = value

    def insert(self, i, x):

        '''inserts x at position i in the list
        pre: 0 <= i <= self.size
        post: x is inserted into the list at position i and 
              old elements from position i..oldsize-1 are at positions 
              i+1..newsize-1'''

        assert 0 <= i <= self.size

        if i == 0:
            # insert before position 0 requires updating self.head
            self.head = ListNode(x, self.head)
        else:
            # find item that node is to be insert after
            node = self._find(i - 1)
            node.link = ListNode(x, node.link)
        self.size += 1

    def __delitem__(self, position):

        '''delete item at location position from the list
        pre: 0 <= position < self.size
        post: the item at the specified position is removed from 
        the list'''

        assert 0 <= position < self.size

        if position == 0:
            self.head = self.head.link
        else:
            node = self._find(position-1)
            node.link = node.link.link

        self.size -= 1

    def __copy__(self):
    
        '''post: returns a new LList object that is a shallow copy of self'''
        
        a = LList()
        node = self.head
        while node is not None:
            a.append(node.item)
            node = node.link
        return a

    '''
    Spring 2023.
    
    Your work begins here. Complete these five methods, including
        -- their docstring (detail the pre & post conditions)
        -- an implementation to satisfy the design
        -- don't forget to test the preconditons!

    Have fun!    '''

    def min(self):
        ''' Find and return the minimum item in the list

            Complete this method '''
        node = self.head
        min = node.item 
        while node is not None:
            if node.item < min:
                min = node.item
                node = node.link
                
            return min
        
        #finds the minimum of the list by finding the smallest item 
    def max(self):
        ''' Find and return the maximum item in the list

            Complete this method '''
        node = self.head
        max = node.item
        while node is not None :
            if node.item > max:
                max = node.item 
                node = node.link

            return max
        #finds the maximum by finding the larger item
        
    
    def index(self, value, start=0):
        ''' Return the index of the node where node.item = value
            Start is an optional parameter, if provided, begin your
            search at the node in position start.
            If the value does not exist on the list return None

            complete this method '''
        node = start 
        value = self.start
        index = node.item
        while node is not None:
            if node.item != value:

                value == node.item
                node = node.link
        return index 
        #finds the node where the item equals the value 
        pass
    
    def count(self, value):
        ''' Return the count of the number of times value may be
            found in the list.   If the value does not exist on the
            list return 0 (zero occurences)

            complete this method '''
        node = self.head 
        value = self.size
        while node is not None: 
            if value == self.size:
                value += 1
                node = node.link

        return value
        #returns the number of times an item is on a list 
        pass
    
    def remove(self, value):
        ''' Given a value, remove the first occurence of value on the list

            complete this method '''
        node =  self.head 
        value = self.size
        delete = node.item
        while node.item:
            if value == 0:
                delete = None 
                node = node.link
        return delete
        #deletes the first item on list 
        
        pass
