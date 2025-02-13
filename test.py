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

# def factorial(num):
#     call_stack = []
#     if num == 1:
#         return 1
#     else:
#         call_stack.append({'input': num})
#         print('call stack:', call_stack)
#         return num * factorial(num - 1)
# factorial(5)

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

# average = 50  
# mark = input('Enter your Student mark: ')
# if int(mark) <= int(average):
#     print('You failed')

# elif int(mark) >= int(average) and int(mark) < 61:
#     print('average pass')

# elif int(mark) >= 61 and int(mark) <= 100:
#     print('You Pass')

# else:
#     print('Absent') 

# a = 1
# while a <= 50:
#     if a % 2 == 0:
#         print(a)
#     a += 1

# list = [1,5,2,3,4]
# max_num = 0
# for num in list:
#     if num > max_num:
#         max_num = num

# print(max_num)


# for num in range (51):
#     if num % 5 == 0 and num > 4:
#         print(num)
