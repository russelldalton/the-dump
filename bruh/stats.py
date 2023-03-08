# Assignment 1, Intro to Data Strtures;  Spring 2023
#
# Program: stats.py
#
# Author:jobe odulio
# Date:1/31/2023
#
# Note: you may NOT use the built-in statistical functions
#       min, max, sum, et.   Instead, create your own code
#       to calculate the answer.
#
#       You may use math.sqrt when calculating the standard deviation
# description: completed stats progrom that finds the min/max, average, and distributes points

import math

def get_scores():
    '''Get scores interactively from the user

    pre: None
    post: returns a list of numbers obtained from user'''

    nums = [] 
    while True:
        num = input("Enter a number (<return> to Quit): ")
        if num == "":
            break
        nums.append(eval(num))
    return nums
    

def min_value(nums):
    
    min = nums[0]
    for i in range(1,len(nums)): 
        if i<0:
            print ("error not valid")
        elif nums[i] <min:
            #finds min
            min=nums[i]
            return nums[i]
            print(nums[i])
            
    #this function finds the smallest number in the list "nums"
    
    
    
    ''' find the minimum
    
    pre: nums is a list of numbers and len(nums) > 0
    post: returns smallest number in nums'''

def max_value(nums):
    
    max = nums[0]
    for j in range(1,len(nums)):
        if j <0:
            print ("error not valid")
        
        elif nums[j] > max:
            #finds max
            max = nums[j]
            return nums[j]
            print(nums[j])
    
    #this function finds the biggest number in the list 
    
    
    
    
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
            #calculates the average 
            count = count + i
            a = count/float(len(nums))
            return a
            
    #this function calculates the average by adding all values and dividing them by the number of values in the list 
            







    ''' calculate the mean

    pre: nums is a list of numbers and len(nums) > 0
    post: returns the mean (a float) of the values in nums'''

def std_deviation(nums):
    #standard deviation equation
    x = average(nums)
    sum = 0.0
    for num in nums:
        sum += (x - num)**2
    return math.sqrt(sum / (len(nums)-1))
    #this function calculates the standard deviation 
    '''calculate the standard deviation

    pre: nums is a list of numbers and len(nums) > 1
    post: returns the standard deviation (a float) of the values
          in nums'''

def distribution(nums):
    list = [0,0,0,0,0]
     
    for i in nums:
        
        if len(nums) < 0:
            print('error not valid')
        #the distribution of numbers in the list 
        elif i >= 90:
            list[0] += 1
        elif i >= 80:
            list[1] += 1
        elif i >= 70:
            list[2] += 1
        elif i >= 60:
            list[3] += 1
        elif i < 60:
            list[4] += 1
    return list 
    print (list)
    #this function distributes the numbers by making a list and adding 1 to each item in the list based on the value 

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

    
