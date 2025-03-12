'''score = 70 

if score >= 90:
    print("A")
elif score > 60:
    print("B")

else:
    print("F")'''
'''nums = [1,2,3,4,5]

for num in nums:
    print(num + 1)'''

'''for i in range(3):
    print(i)'''
'''teams = [['Jody','Abe'], ['Thebe', 'Nkhasi'],['Themba', 'Zoane']]
for team in teams:
    for name in team:
        print(name)'''
'''a = input("Enter a number: ")
b = input("Enter another number: ")
print(int(a) + int(b))
print(int(a) - int(b))
print(int(a) * int(b))
print(int(a) / int(b))'''
'''nums = [3, 4, 16]

print('This is an example of a for loops')

for num in nums:
    print(num ** 2)

i = 3 

print('This is an example of a while loop')

while i < 258:
    print(i)
    i = i ** 2'''

'''i = 1 
while i < 6:
    print(i)
    i += 1'''
    
"""names = ['Jody', 'Abe', 'Thebe', 'Nkhasi', 'Themba']

for name in names:
    if 'm' in name.lower():
        continue
    elif'h' in name.lower():
        pass
    elif 'a' in name.lower():
        break
    else:
        print(name)"""
# Try and except example        
'''nums = [0,1,2,3,4,5]
try:
        print(sum(nums))

except:
        print('Cannot print the sum! Your varaible are not a numbers')'''

'''nums = ['x', 'y', 'z']
try:
    print(sum(nums))

except:
    print('Cannot print the sum! Your varaible are not a numbers')'''

'''nums = ['x', 'y', 'z']
try:
    print(sum(nums))

except:
    print('Cannot print the sum! Your varaible are not a numbers')

finally:
    print('Hope you got the results you were looking for!')'''

# Write a python program that asks the user to enter two numbers and then compares them using relational operators.(== != > < >= <=). Print out the results of the comparisons. 
'''a = input('Enter a number: ')
b = input('Enter another number: ')
print( int(a) == int(b))
print (int(a) != int(b))
print(int(a) > int(b))
print(int(a) < int(b))
print(int(a) >= int(b))
print(int(a) <= int(b))
'''
# 1. Declare two boolean variables with values (True or False) and then apply logical operators (and, or, not). Show the outputs.
'''name = bool (True)
surname = bool (True)

print(name and surname)
print(name or surname)
print(not name)'''

# 1. Declare two boolean variables with values (True or False) and then apply logical operators (and, or, not). Show the outputs.
'''a = 5
b = 6
print(a < b and b > a)
print(a > b or b < a)
print(not a > b)''' 

# 2. Write a program that asks the user to enter a number. If the number is zero, print "Number is zero". If the number is even, print "Number is even". If the number is odd, print "Number is odd".
'''a = input('Enter a number: ')
if int(a) == 0:
    print('Number is zero')
elif int(a) % 2 == 0:
    print('Number is even')

else: 
    print('Number is odd')
'''

'''nums =[5,3,2,10]

try:
    avg =sum(nums) / len(nums)
    print("The average of the list is",avg)

except:
    print('Cannot print the average! make sure you enter a list of integers')

finally:
    print('Hope you got the results you were looking for!')'''

#Function Basics

'''def greetings(langauge):
    if langauge == 'Sesotho':
        greeting = 'Lumelang'

    elif langauge == 'English':
        greeting = 'Hello'

    elif langauge == 'French':
        greeting = 'bonjour'

    print(greeting)

greetings('French')
'''
'''def greetings(language):
    if language == 'Sesotho':
        greeting = 'Lumelang'
    elif language == 'English':
        greeting = 'Hello'
    elif language == 'French':
        greeting = 'Bonjour'
    else:
        greeting = 'Language not supported'
    
    return greeting

print(greetings('French'))'''  # Output: Bonjour

#Recursion

'''def factorial(num):
    call_stack = []
    if num == 1:
        return 1
    else:
        call_stack.append({'input': num})
        print('call stack:', call_stack)
        return num * factorial(num - 1)
factorial(5)'''

# how recursion works

'''def EvenNums(num):
    if num < 2:  # Ensure num is at least 2
        return []
    elif num == 2:
        return [2]
    else:
        return EvenNums(num - 2) + [num]  # Recursively build a list

print(EvenNums(8))  '''


# Loops Using if else statements

'''average = 50  
mark = input('Enter your Student mark: ')
if int(mark) <= int(average):
    print('You failed')

elif int(mark) >= int(average) and int(mark) < 61:
    print('average pass')

elif int(mark) >= 61 and int(mark) <= 100:
    print('You Pass')

else:
    print('Absent')''' 

'''a = 1
while a <= 50:
    if a % 2 == 0:
        print(a)
    a += 1'''

'''list = [1,5,2,3,4]
max_num = 0
for num in list:
    if num > max_num:
        max_num = num

print(max_num)'''

# Using range

'''for num in range (51):
    if num % 5 == 0 and num > 4:
        print(num)'''


#Lambada Function
'''greeting = lambda name: f'Hello, {name}!'
print(greeting('Jody'))'''

# Using map
'''numbers = [1,2,3,4,5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)'''

# Using filter
'''numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)'''

# Using sorted
'''students = [
    {'name': 'John', 'age': 20},
    {'name': 'Jane', 'age': 22},
    {'name': 'Bob', 'age': 19},
    {'name': 'Alice', 'age': 21},
    
]
sorted_students = sorted(students, key=lambda student: student['age'])
print(sorted_students)'''

# list of numbers

'''numbers = [1,2,3,4,5,6,7,8,9,10]'''

#Use a lamba function to filter out odd numbers

'''evens = list(filter(lambda x: x % 2 == 0, numbers))

#Use a lamba function to square numbers

squares = list(map(lambda x: x ** 2, numbers))

#Print results

print("Original numbers:", numbers)
print("Even numbers:", evens)
print("Squared numbers:", squares)'''

'''x = lambda a, b, c: a + b + c
print(x(5, 6, 2))'''

'''def multiplier(n):
    return lambda a: a * n

doubler = multiplier(3)
tripler = multiplier(4)


print(doubler(11))
print(tripler(12))'''

# Class and Objects
'''class Dog:
    #this is a blank class
    pass
pepper = Dog()
print(pepper)'''

#Function

# If we call the function without argument, it uses the default value:
'''
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
'''
'''def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)'''

'''def average(a, b, c, d):
    return (a + b + c + d) / 4

result = average(1, 2, 13, 24)
print("average:", int(result))

range(3)
'''

    
    

#Recursion

'''def tri_recursion(k):
    if(k > 0):
        a = k + tri_recursion(k - 1)'''
'''        print(a)
    else:
        a = 0
    return a

print("\n\nRecursion Example Results")
tri_recursion(6)
'''
'''class ClassSchedule:
    def __init__(self,course ):
        self.course = course

first = ClassSchedule('Chemistry')
print(first.course)'''
#Doing my notes rn
'''cars = ['Ford', 'Volvo', 'BMW', 'Toyota']
a,b,c,d = cars
print(a,b,c,d)'''

x= "awesome"

'''def myfunc():
    print('Python is ' + x)
myfunc()'''

'''x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print('Python is ' + x)
'''
'''Int_value = 4
print(Int_value)
print(type(Int_value))

print()

float_value = float(Int_value)
print(float_value)
print(type(float_value))
'''
'''x = 5
y = 2

print("arithmetic operators(x+y):", (x+y))
print("comparision operatord(x >= y) :", x >= y)
print("logical operators(x == y and x > y):", x == y and x > y)'''

'''score = 70

if score >= 50:
    print("You passed")
elif score >= 60:
    print("You passed with a distinction")
else:
    print("You failed")'''

'''nums = [1,2,3,4,5]
for nums in range(7):
    print( nums + 0)'''

'''a = 1
while a < 8:
    print(a)
    a += 2 '''

#Constructors __init__
'''class ClassSchedule:
    def __init__(self, course):  # Fixed the typo here
        self.course = course

first = ClassSchedule('Chemistry')
print(first.course)'''

# output = Chemistry

#Destructor __del__

# First example
'''class ClassSchedule:
    def __init__(self, course):
        self.course = course
    def __del__(self):
        print('You successfully deleted the course')
        
first = ClassSchedule('Chemistry')
print(first.course)
del first'''

# Second example
'''class ClassSchedule:
    def __init__(self, course):
        self.course = course
    def __del__(self):
        print('You successfully deleted the course')

sched = ClassSchedule('Mathematics')

del sched'''
# Arrays

'''cars = ['Ford', 'Volvo', 'BMW', 'Toyota']
x = cars[1]
print(x)'''

'''cars = ['Ford', 'Volvo', 'BMW', 'Toyota']
cars[0] = 'Opel'
print(cars)'''

# The length of an array

'''cars = ['Ford','BMW','Opel','Volvo']

x = len(cars)
print(x)'''

# Looping through an array

'''cars = ['Ford', 'Volvo', 'BMW', 'Toyota']
for x in cars:
    print(x)'''

# Adding an item to an array

'''cars = ['Ford', 'Volvo', 'BMW']
cars.append('Toyota')
print(cars)'''

# Removing an item from an array

'''cars = ['Ford', 'Volvo', 'BMW']
cars.pop(0)
print(cars)'''

'''cars = ['Ford', 'Volvo', 'BMW']
cars.remove('Volvo')
print(cars)'''


#Question from Sir Tsiu
#Write a python function takes input of the character,separated by commas and then sort them alphabetically 



# Handling user input correctly
# input_values = input("Enter a comma-separated list of characters: ")  # Keep it as a string
# print("Sorted Characters:", characters(input_values))




# Taking user input as a number and using match correctly
# input_prime = int(input("Enter any number between 1 and 5: "))
# match input_prime:
#     case 2:
#         print("Mohale")
#     case 3:
#         print("Bake")
#     case 4:
#         print("Toyota")
#     case 5:
#         print("Isuzu")
#     case _:
#         print("Invalid input")




# Correct function call without arguments
# print_primes_skip_7()

            

# input_str = "h, g, d, a, c, j, i, b, f, e,o,p,q,r,s,t,u,v,w,x,y,z"
# sorted_str = characters(input_str)
# print(sorted_str)

#Create a function isLongerThan(S) that returns true if the given string has more than 5 characters, otherwise false'''.
'''def isLongerThan(S):
    return len(S) > 5'''




#Create a function that prime numbers from 1 to 50. The program should skip all the multiples of 7
''''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_skip_7():
    for num in range(1, 51):
        if is_prime(num) and num % 7 != 0:
            print(num, end=" ")

print_primes_skip_7()'''


#Create a function that prime numbers from 1 to 50. The program should skip all the multiples of 7

'''for num in range(1, 51):
    if num % 7 == 0:
        print(num)
    continue
else:
    print(num)'''

#Create a function that uses a match case to print the day of the week based on the user input e.g. if the user enters 1 the program should print “ The day is monday”

'''def day_of_week(day): # function definition
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid day")
input_day = int(input("Enter any number of the day between 1 and 7: "))  
day_of_week(input_day)''' # function call

'''def top_three(cars):
    match cars:
        case 1:
            print("Ford")
        case 2:
            print("Toyota")
        case 3:
            print("Isuzu")
input_cars = int(input("Enter any number between 1 and 3 to choose a car: "))
top_three(input_cars)'''


#Create a function that arranges the given charaters in alphabetical order and returns them sorted alphabetically and check if the value is less than 5 characters long and return true if it is and false if it is not   
'''def characters(input_str):
    chars = input_str.split(",")  
    sorted_chars = sorted([char.strip() for char in chars])  
    return ", ".join(sorted_chars)


def isLongerThan(S):
    return len(S) > 5


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # Exclude other even numbers
    for i in range(3, int(n ** 0.5) + 1, 2):  # Check odd numbers up to sqrt(n)
        if n % i == 0:
            return False
    return True


def print_primes_skip_7():
    prime_numbers = [num for num in range(1, 51) if is_prime(num) and num % 7 != 0]
    print("Prime numbers skipping multiples of 7:", prime_numbers)


def my_function():
    try:
        choose = int(input("Enter any choice between 1 and 3: "))
        match choose:
            case 1:
                print(characters('c,d,f,a,b,e,g,i,h'))  # Function call
            case 2:
                print(isLongerThan('Mohale'))  # Function call to isLongerThan
            case 3:
                print(is_prime(12))  # Function call to is_prime
            case _:
                print("Invalid choice")
    except ValueError:
        print("Please enter a valid number between 1 and 3.")


# Run the function
my_function()'''

#While loop
'''a = 2
while a < 8:
    print(a)
    a += 1'''

#While loop using break

'''i = 1 
while i < 7:
    print(i)
    if i == 4:
        break
    i += 1 '''

#While loop using continue

'''num = 0 
while num < 6:
    num += 1
    if num == 4:
        continue
    print(num)'''

#While loop using else

'''m = 1 
while m < 6:
    print(m)
    m += 1
else:
    print('m is no longer less than 6')'''

#For loop

'''fruits = ['apple', 'banana', 'cherry']
for m in fruits:
    print(m)'''

#For loop using break

'''music = ['hip hop', 'jazz', 'pop', 'rock']
for m in music:
    print(m)
    if m == 'pop':
        break'''

#For loop using break

'''music = ['hip hop', 'jazz', 'pop', 'rock']
for m in music:
    if m == 'pop':
        break
    print(m)'''

#For loop using continue

'''colors = ['red', 'blue', 'green', 'yellow']
for c in colors:
    if c == 'blue': # Skip blue
        continue
    print(c)'''

#For loop using range
'''for x in range(2,30,3):
    print(x)'''

#For loop using else
'''for m in range(6): 
    print(m)
else:
    print('finally finished!')'''

#Break the loop when x is 3 using for loop and else   
'''for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print('Finally finished!')'''

# Nested loops

'''adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for m in adj:
    for n in fruits:
        print(m, n)'''

# The pass statement
'''for a in [0, 1, 2, 3, 4]:
    pass'''
#having an empty for loop  like this, would raise an error without the pass statement

#Functions
#Calling a function
'''def my_function():
    print("Hello from a function")
my_function()'''

'''def my_func(fname, lname):
    print(fname + " Refsnes " + lname)

my_func("Emil", "Line")
my_func("Tobias", "Speed")
my_func("Linus", "Doom")
'''

#Number of Arguments
'''def func(fname, lname):
    print(fname + " " + lname)

func('Emil', 'Refsnes') '''

#Arbitrary Arguments, *args

'''def func(*kids):
    print("The youngest child is " + kids[0])
func('Mohale', 'Thebe', 'Mpho')'''

#Keyword Arguments

'''def fuc(child3,child2,child1):
    print('The youngest child is ' + child3)
fuc(child1 = "Mohale", child2 = "Naleli", child3 = "Lineo")'''

#Return Values

'''def my_func(x):
    return 5 * x
    
print(my_func(3))
print(my_func(5))
print(my_func(2))'''

# Postional- Only Arguments

'''def fug(x, /):
    print(x)

fug(3)'''

# keyword - Only Arguments

'''def hub (*,x):
    print(x)
hub(x = 3)''' 
# Same as postional 

#Lambda

'''x = lambda a, b, c: a + b + c
print(x(5, 6, 5))'''

'''def myfunc(n):
    return lambda a: a * n

auro = myfunc(3)
mola = myfunc(5)

print(auro(11))
print(mola(11))
'''
#Access the Elements of an Array

'''cars = ['Ford', 'Volvo', 'BMW']

x = cars[0]

print(x)'''

#Modify the First Element of an Array

'''cars = ['Ford', 'Volvo', 'BMW']

cars[0] = 'Toyota'

print(cars)'''

#length of an array
'''cars = ['Ford', 'Volvo', 'BMW']

x = len(cars)

print(x)'''

# Looping Through an Array

'''cars = ['Ford', 'Volvo', 'BMW']

for x in cars:
    print(x)'''

#Adding an Element to an Array

'''cars = ['Ford', 'Volvo', 'BMW']

cars.append('Honda')

print(cars)'''

#Removing an Element from an Array

'''cars = ['Ford', 'Volvo', 'BMW', 'Honda']

cars.pop(1)

print(cars)'''

#Removing an Element from an Array

'''cars = ['Ford', 'Volvo', 'BMW', 'Honda']

cars.remove('Volvo')

print(cars)'''

#Sorting an Array

'''cars = ['Ford', 'Volvo', 'BMW', 'Honda']

cars.sort()

print(cars)'''

#Python Classes/Objects 

'''class MyClass:
    x = 5 

p1 = MyClass()
print(p1.x)'''

#The __init__() Function

'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("John", 25)

print(p1.name)
print(p1.age)'''

# The __str__() Function

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p2 = Person('Mohale', 20)

print(p2)'''

#Object Methods

'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person('Mohale', 20)
p1.myfunc()'''

#Class Attributes

'''class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print('Hello my name is ' + abc.name)

p1 = Person('Mohale', 20)
p1.myfunc()'''

'''topic = ['Maths', 'English', 'Sesotho']
topic.pop(2)
print(topic)'''

#Recursion

'''def factorial(num):
    call_stack = []
    if num == 1:
        print('base case reached Num is 1.')
        return 1
    else:
        call_stack.append({'input': num})
        print('call stack: ', call_stack )
        return num * factorial(num - 1)

factorial(5)'''

#Class
'''class Num: # Create a class named Num
    x = 5

p1 = Num() # Create an object named p1
print(p1.x)'''

# Class

'''class Person:
    def __init__(log, name, age):
        log.name = name
        log.age = age

p1 = Person ('Mohale', 20)

print(p1.name)
print(p1.age)

#Output (Mohale 20)'''

#Class

'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('Mohale', 20)

print(p1)'''

# __str__ method

'''class Name:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):  # the string representation of an object with the __str__ function
        return f"{self.name} ({self.age})"
    
p1 = Name('Tumelo', 23)

print(p1)'''

# class Person
'''class Name:  
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def func(self):
        print('Hello I am ' + self.name)
        print ('I am ' + str(self.age) + ' years old')

p1 = Name('Mohale', 20)
p1.func()'''

# Self Parameter

'''class Person:
    def __init__(boy, name, age):
        boy.name = name
        boy.age = age

    def fun(abc):
        print('Hello I am ' + abc.name)

p1 = Person('Mohale', 20)
p1.fun()'''

#Modify Object Properties

'''class Motho:
    def __init__(mize, name, age):
        mize.name = name
        mize.age = age

    def show(self):
        print('Hello my name is ' + self.name)

p1 = Motho('Mohale', 20)
p1.age = 21

print(p1.age)'''
'''print(p1.name)'''

#Delete Object Properties
'''def fact(num):
    call_stack = []
    if num == 1:
        print('base case reached ! Num is 1')
        return 1
    else:
        call_stack.append({'input': num})
        print('call stack: ', call_stack)
        return num * fact(num-1)
    
    
fact(5) '''

#Lambda

'''add = lambda a, b: a+b
print(add(3,5))

greeting = lambda name: f'Hello, {name}!'
print(greeting('Alice'))'''

# Using map()

'''numbers = [1,2,3,4,5,6]

squared = list(map(lambda x: x ** 2, numbers))

print(squared)'''

# Lambda filter() even numbers

'''numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)'''

# Sorted

'''students = [('Alice','A',15), ('Bob','B', 16), ('Katleho','T', 10)]

sorted_student = sorted(students, key=lambda x: x [2])

print(sorted_student)
'''

'''numbers = [1,2,3,4,5,6,7,8,9,10]

evens = list(filter(lambda x: x % 2 == 0, numbers))

squares = list(map(lambda x: x ** 2, numbers))

print('Original numbers:', numbers)
print('Even numbers:', evens)
print('Square numbers;', squares)
'''




