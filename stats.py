# Assignment 1, Intro to Data Strtures;  Spring 2023
#
# Program: stats.py
#
# Author:
# Date:
#
# Note: you may NOT use the built-in statistical functions
#       min, max, sum, et.   Instead, create your own code
#       to calculate the answer.
#
#       You may use math.sqrt when calculating the standard deviation

import math

def get_scores():
    '''Get scores interactively from the user

    pre: None
    post: returns a list of numbers obtained from user'''

    nums = []
    while True:
        num = input("Enter a number (<return> to Quit): ")
        if num == "": break
        nums.append(eval(num))
    return nums

def min_value(nums):
    distribution(nums)
    for i in len(nums): 
        if i<0:
            print ("error not valid")
        else: 
            print (nums[0])

    
    
    
    
    ''' find the minimum
    
    pre: nums is a list of numbers and len(nums) > 0
    post: returns smallest number in nums'''

def max_value(nums):
    distribution(nums)
    for i in len(nums):
        if i <0:
            print ("error not valid")
        else:
            print (nums[2])

    
    
    
    
    
    
    ''' find the maximum

    pre: nums is a list of numbers and len(nums) > 0
    post: returns largest number in nums
    '''

def average(nums):
    count = 0
    for i in nums:
        if i<0:
            print ("error not valid")
        else:
            count = count + i
            a = count/float(len(nums))
             
            print (a) 

            







    ''' calculate the mean

    pre: nums is a list of numbers and len(nums) > 0
    post: returns the mean (a float) of the values in nums'''

def std_deviation(nums):

    x = average(nums)
    sum = 0.0
    for num in nums:
        sum += (x - num)**2
    return math.sqrt(sum / (len(nums)-1))

    '''calculate the standard deviation

    pre: nums is a list of numbers and len(nums) > 1
    post: returns the standard deviation (a float) of the values
          in nums'''

def distribution(nums):

    for i in len(nums):
        
        

    '''calculate the distribution of scores in the ranges:
    90 and above, 80-89, 70-79, 60-69, below 60

    pre: nums is a list of numbers and len(nums) > 1
    post: return five integers reflecting the distribution of scores'''

def main():
    nums = get_scores()
    print(min_value(nums))
    print(max_value(nums))
    print(average(nums))
    print(std_deviation(nums))
    print(distribution(nums))
    
if __name__ == '__main__':
    main()

    
