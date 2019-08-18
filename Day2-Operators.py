/*
Objective 
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

Task 
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

Input Format

There are  lines of numeric input: 
The first line has a double,mealcost(the cost of the meal before tax and tip). 
The second line has an integer, tippercent (the percentage of mealcost being added as tip). 
The third line has an integer, taxpercent (the percentage of mealcost being added as tax).
Output Format

Print the total meal cost, where totalcost is the rounded integer result of the entire bill (mealcost with added tax and tip).

Sample Input

12.00
20
8

Sample Output

15
*/

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = ((meal_cost)*(tip_percent))/100
    tax = ((meal_cost)*(tax_percent))/100
    totalcost=round(meal_cost+tip+tax)
    print(totalcost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
