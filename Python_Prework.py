#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    print("hello_" + user_name)
hello_name("USERNAME")

print(" ")
#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    current_number = 0
    while current_number < 100:
        if current_number % 2 == 1:
            print(current_number)
            current_number += 1
        else:
            current_number += 1
first_odds()

print(" ")
#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    a_list = [1, 2, 5, 32, 4, 12, 6]
    a_list.sort()
    print(a_list.pop())
max_num_in_list(a_list=[1, 2, 5, 32, 4, 12, 6])

print(" ")
#Question 4
#Write a function to return if the given year is a leap year.
def is_leap_year(a_year):
    if int(a_year) % 4 == 0:
        print(True)
    else:
        print(False)
is_leap_year(input("This is a leap year? "))

print(" ")
#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers
def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    range_list = list(range(min(a_list), max(a_list)+1))
    if sorted_list == range_list:
        print(True)
    else:
        print(False)
is_consecutive(a_list=[1,2,4,5])