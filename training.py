# -*- coding: utf-8 -*-
"""Training

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uJ8L-7noby8FWK1tfjNkSxl8cm2A2ixr

Session 1

## **Mathematical Manipulations**

*   Addition
*   Subtraction
*   Multiplication
*   Division

***Variable declaration***
"""

a=10
b=8

"""adding the two numbers"""

a+b

"""subtracting the two numbers"""

a-b

"""multiplication of the two numbers"""

a*b

"""division of the two numbers"""

a/b

"""***Improved result display***"""

print('The sum of',a, 'plus', b, 'is',a+b)

"""A being 10 and b being 8 their sum will add upto 18"""

from re import T
print('the difference between',a,'and',b,'is',a-b)

"""A being 10 and b being 8 their difference is 2"""

print('The product between',a,'and',b,'is',a*b)

"""A being 10 and b being 8 their product is 80"""

print('The quotient of ',a,'and',b,'is',a/b)

"""A being 10 and b being 8 their quotient is 1.25

division with modulus remainder
"""

c=17
d=3

c/d

c//d

c%d

print('the quotient of',c,'and',b, 'is',c/b)

print('the remainder after dividing',c,'and',d,'is',c%d)

print('The quotient of',c, 'and',d,'is',c//d,'remainder',c%d)

"""***Exponents***"""

base=8
exponent=3

base**exponent

print('8 raised to power 3 is',base**exponent )

"""***Area of a rectangle***"""

width=5
height=4

width*height

print('The area of a rectangle width 5 and height 4 is',width*height)

"""***REVISION***

***Area of a rectangle***
"""

breath=6
extent=4

breath*extent

print("The area of a rectangle breath 6 and extent 4 is",breath*extent)

"""***Exponents***"""

base=6
exponent=2

base**exponent

print("6 raised to power 2 is",base**exponent)

"""6 raised to power 2 is 36

Division with modulus remainder
"""

e=5
f=3

e/f

e//f

e%f

print("The quotient of ",e, "and",f,"is",e/f)

print('The remainder after dividing',e,"and",f, "is",e%f)

print("The quotient of",e,"and",f,"is",e//f, "remainder",e%f)

"""***Area of a triangle***"""

base=4
height=2

1/2*base*height

print('The area of a triangle with base 4 and height 2 is',1/2*base*height)

"""***Simple interest***"""

rate=.1
principal=50000 # in dollars
time=2 # in years

interest=principal*rate *time

interest

print('The simple interest for an amount of 50000 dollars at a rate of 10% over a period of 2 years is',interest )

"""***Temperature conversion(celsius to fahrenheit)***"""

celsius=23

temp=(celsius *9/5) +32

print('The conversion of celsius 23 to fahrenheit',temp)

"""***Average of numbers***"""

num1=3
num2=6
num3=9

average=(num1 +num2+num3)/3
average

(num1 +num2+num3)/3

print('The average of num1 and num2 and num3 is',average)

"""***Swaping numbers***"""

a=4
b=6

a,b=b,a

a

"""Write a program that returns the largest number from a pool of 3"""

# Step 1: Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Step 2: Compare the numbers
if a >= b and a >= c:
    print("The largest number is", a)
elif b >= a and b >= c:
    print("The largest number is", b)
else:
    print("The largest number is", c)

"""Session 2

**elif else conditions**
"""

score=70

if score >=90:
   print('A')
elif score >=80:
   print('B')
elif score >=70:
   print('C')
elif score >=60:
   print('D')
else:
   print('fail')

score=90

if score >=90:
   print('A')
elif score >=80:
   print('B')
elif score >=70:
   print('C')
elif score >=60:
   print('D')
else:
   print('Fail')

"""Loops:for and while"""

for i in range(1,8):
  print('Hello',i)

"""Functions

greetings by definition
"""

def greet(name): #defining the greet function
  return f'Hello, {name}!'# calling ang applying the greet function
print(greet('Alice')) #display the results

def greet(world):
  return f'Hello, {world}!'
print(greet('world'))

fruits=['apple','banana','mango']#to list the items
fruits.append('kiwi') #to add an item to the list
fruits.sort() #to sort the items in an alphabetical order

fruits

"""***LARGEST POOL OF 3***"""

a=4
b=7
c=1

if a>=b and a>=c:
   largest=('a')
if b>=a and b>=c:
  largest=('b')
else:
 largest=('c')

largest

"""***elif if condition***"""

purchase =200 #in ksh

if purchase>=500:
  print("30% discount")
  discount=('30%')
else:
  print('0% discount')

discount=purchase*discount

weather=("g")

if weather is ("sunny"):
   print("Its really sunny today")
else:
  print("Its not sunny today")

# You are supposed to declare/define weather

age=13

if age>=18:
  print("An adult")
else:
  print("Not an adult")

"""***session three***

Creating comprehensive listn (list comprehension)
"""

# Let i,j be a sub space of intergers where both ranges from 1 to 4,
#create a table of multiplyers i by j
squares=[]
for i in range(1,4):
   for j in range(1,4):
    print(f"{i}x{j}={i*j}")

#traditional way
squares=[]
for i in range(1,6):
  squares.append(i*i)
  print(squares)

"""**Assignment**

Multiplication table for i,j where i and j is a set of numbers ranging from 1 to 15
"""

squares=[]
for i in range(1,15):
  for j in range(1,15):
    print(f"{i}x{j}={i*j}")

"""**Basic dictionary **

Used to pull information from a data base that satisfies a given condition

FUNCTIONS WITH CONDITIONS
"""

#a program that checks the eligibility of a voter
def is_eligible(age):
  if age>=18:
    return "Eligible to vote"
  else:
    return "Not eligible to vote"
print(is_eligible(14))

"""Assignment

In another field

"""

def risk_category(age,cholesterol,smoker):
  if age>60 and cholesterol>240 and smoker:
    return "High risk"
  elif age>45 and cholesterol>200:
    return "Moderate risk"
  else:
    return "Low risk" # You need to add a print function after every program to check if it works as desired. Refer to the code below.

print(risk_category(30, 250, False))

"""**Basic dictionary operations**"""

student = {"name": "Alice", "age": 20, "grade": "B"} # Supplying the demographic information of a student

print(student["name"])# Telling the python to print the name of the student
student["grade"] = "A"# Indicating the grade a specific student attained
print(student)# Printing out every information about the student

# Add new key
student["school"] = "St. Mary" # Adding  anew identifier to the list of an individual

for key, value in student.items(): # Used to display independent details/information of an individual in an independent format.
  print(key,"is",value)

"""Assignment

basic dictionary operations in another field
"""

patient={"name":"John","age":32,"medication":"injection"}

print(patient["name"])
patient["medication"]="injectons"
print(patient)

"""Read on creating a menu program using loop+input

***Password generator***
"""

import string
import random
import numpy as np
import torch


def generate_password(length=8,use_upper=True,use_lower=True,use_symbols=True,use_digits=True):
  character=''
  if use_upper:
    character+=string.ascii_uppercase
  if use_lower:
    character+=string.ascii_lowercase
  if use_symbols:
    character+=string.punctuation
  if use_digits:
    character+=string.digits

  if not character:
     raise ValueError("At least one character set must be selected!")

  #Ensure password contains at least one of each selected type
  password=[]
  if use_upper:
    password.append(random.choice(string.ascii_uppercase))
  if use_lower:
    password.append(random.choice(string.ascii_lowercase))
  if use_symbols:
    password.append(random.choice(string.punctuation))
  if use_digits:
    password.append(random.choice(string.digits))

  #Fill the rest of the password length
  password+=random.choices(character,k=length - len(password))
  random.shuffle(password)

  return ''.join(password)

random.seed(32) #is used for reproducibility
print("generated password:",generate_password(length=8))

"""***Making a calculator***"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero!"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid input.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input.")
        return

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print( f"Result: {subtract(num1, num2)}")


    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")

if __name__ == "__main__":
    calculator()

import math

def trig_calculator():
  print("Trigonometry calculator")
  print("Available functions: sin, cos , tan , cosec , sec ,cot")

  angle_deg = float(input("Enter the angles in degrees:"))
  function = input("Enter the function name(e.g., sin, cos):").strip().lower()

  angle_rad = math.radians(angle_deg)

  try:
    if function == "sin":
      result = math.sin(angle_rad)
    elif function == "cos":
      result = math.cos(angle_rad)
    elif function == "tan":
      result = math.tan(angle_rad)
    elif function == "cosec":
      # cosec(x) = 1/sin(x)
      result = 1 / math.sin(angle_rad)
    elif function == "sec":
      # sec(x) = 1/cos(x)
      result = 1 / math.cos(angle_rad)
    elif function == "cot":
      # cot(x) = 1/tan(x) or cos(x)/sin(x)
      result = 1 / math.tan(angle_rad)

    else:
      print("Invalid function.")
      return

    print(f"{function}({angle_deg}) = {result:.6f}")
  except ZeroDivisionError:
    # Handle cases where the denominator is zero for cosec, sec, or cot
    print(f"{function}({angle_deg}) is undefined (division by zero).")

trig_calculator()

import math

def trig_calculator():
  print("Trigonometry calculator")
  print("Available functions: sin, cos , tan , cosec , sec ,cot")

  angle_deg=float(input("Enter the angles in degress:"))
  function=input("Enter the function name(e.g., sin, cos):").strip().lower()

  angle_rad=math.radians(angle_deg)

  try:
    if function=="sin":
      result=math.sin(angle_rad)rt math
    elif function=="cos":
      result=math.cos(angle_rad)
    elif function=="tan":
      result=math.tan(angle_rad)
    elif function=="cosec":
      result=1 / math.sin(angle_rad)
    elif function=="sec":
      result=1 / math.cos(angle_rad)
    elif function=="cot":
      result=1 / math.tan(angle_deg)

    else:
      print("Invalid function.")
      return

    print(f"{function}({angle_deg})={result:.6f}")
  except ZeroDivisionError:
    print(f"{function}({angle_deg}) is undefined(divison by zero).")

trig_calculator()

"""combine the 2 programs and work on the user interface"""

import math

def evaluate_trig_function(expr):
    # Expected format: func(angle), e.g. sin(30), cot(45)
    try:
        func_name, rest = expr.split('(', 1)
        angle_str = rest.rstrip(')')
        angle_deg = float(angle_str)
        angle_rad = math.radians(angle_deg)

        if func_name == "sin":
            return math.sin(angle_rad)
        elif func_name == "cos":
            return math.cos(angle_rad)
        elif func_name == "tan":
            return math.tan(angle_rad)
        elif func_name == "cosec":
            return 1 / math.sin(angle_rad)
        elif func_name == "sec":
            return 1 / math.cos(angle_rad)
        elif func_name == "cot":
            return 1 / math.tan(angle_rad)
        else:
            print("Invalid trig function.")
            return None
    except Exception as e:
        print("Error in trig expression:", e)
        return None

def is_trig_expression(expr):
    # Check if expr matches trig pattern like sin(30)
    trig_funcs = ['sin', 'cos', 'tan', 'cosec', 'sec', 'cot']
    for func in trig_funcs:
        if expr.startswith(func + '(') and expr.endswith(')'):
            return True
    return False

def calculator():
    print("Simple Calculator — enter expressions like '2+3*4' or trig functions like 'sin(30)'.")
    print("Type 'clear' to reset, 'exit' to quit.")

    expression = ""

    while True:
        print("\nScreen: " + expression)
        user_input = input("Enter next input (number/operator/trig function/ = / clear / exit): ").strip()

        if user_input.lower() == 'exit':
            print("Exiting calculator. Bye!")
            break
        elif user_input.lower() == 'clear':
            expression = ""
            continue
        elif user_input == '=':
            if is_trig_expression(expression):
                result = evaluate_trig_function(expression)
                if result is not None:
                    print(f"Result: {result:.6f}")
                expression = ""
            else:
                try:
                    # Evaluate normal arithmetic
                    result = eval(expression)
                    print(f"Result: {result}")
                except Exception as e:
                    print("Error evaluating expression:", e)
                expression = ""
        else:
            # Add input to expression
            expression += user_input

if __name__ == "__main__":
    calculator()

# Program make a simple calculator that can add, subtract, multiply and divide using functions

# define functions
def add(x, y):
   """This function adds two numbers"""

   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y

def divide(x, y):
   """This function divides two numbers"""

   return x / y

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")