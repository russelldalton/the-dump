# ListNode.py - CIS120, Intro to Data Structures;  Spring 2023

class ListNode(object):
    
    def __init__(self, item = None, link = None):

        '''creates a ListNode with the specified data value and link
        pre: none enforced, default values provided
        post: a new instance of ListNode() is returned'''
        
        self.item = item
        self.link = link
