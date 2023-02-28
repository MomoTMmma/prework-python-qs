#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello(user_name):
    print("Hello" + user_name.title() + "!")
hello(" Melissa")            

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100

def first_odds():
        odds = list(range(0, 100))
        print(odds)
        for number in odds:
              if number % 2 != 0:
                    print(number)
first_odds()                

# #Question 3
# #Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
      return max(a_list)
print(max_num_in_list([2,3,5,8,9, 100, 67, 45, 2]))       
                
# #Question 4
# #Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
         print(f'{a_year} is a leap year')
    else:
         a_year = False
         print(f'{a_year}')
is_leap_year(2025)       
                
# #Question 5
# #Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
     counter=a_list[2]
     for value in a_list:
          if value ==counter:
               counter += 4
          elif value != counter:
               print(False)
               print(True)
     
is_consecutive([2,3,4,5,6,])
