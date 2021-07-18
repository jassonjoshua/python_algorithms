#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 21:58:28 2021

@author: Dr. Jasson J. Hidalgo

Requirements:
1. The function shall allow the user to input an index value.
2. The function shall calculate the fibonachi numbers starting with '0'
3. The function shall notify the user when a negative index is entered.
4. The function shall wait 2 seconds between calculation.
"""
# Imports
import time

# Function Definition for fibonachi_Val(n)
def fibonachi_val(_n):
    """ This function recieves an input as an interger 'n' and calculates the
    fibonachi number from sequence associated with the 'n' number"""
    # for first and second values of the fibonachi sequence
    _n1 = 0
    _n2 = 1
    #The app shall check values passed by the user to compute and return message
    if _n == 0:
        print("The value can not be calculated!")
    elif _n == 1:
        return _n1 # it deals with first number
    elif _n == 2:
        return _n2 # it deals with second number
    elif _n < 0:
        print("Fibonahci does not have negative numbers")
    else:
        for i in range(2, _n):
            print("The letter i is ", i)
            time.sleep(2)
            sum_val = _n1 + _n2
            print("after adding n1 + n2 we get: ", sum_val)
            _n1 = _n2
            print("n1 becomes ", _n1)
            _n2 = sum_val
            print("n2 becomes ", _n2)
        return sum_val
    return "Ups! out of range"
# End of fibonachiVal(n) function
#----------------------------------------------------------------------------


# Function call
print("The Fibonachi Value is:", fibonachi_val(-6)) # Passing a value n
