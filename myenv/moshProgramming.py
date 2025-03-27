# birth_year = input('What year were you born? ')
# age = 2025 - int(birth_year)
# print(f'You are {age} years old.')

'''first = input('First number: ')
second = input('Second number: ')
sum = int(first) + int(second) 
print(sum)'''

# BMI Calculator Body Mass Index
weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'K':
    converted = int(weight) / 0.45
    print('Weight in Lbs: ' + str(converted))

else:
    converted = int(weight) * 0.45
    print('Weight in Kg: ' + str(converted))

'''i = 1 
while i <= 10:
    print(i * '*')
    i = i + 1'''

# List of names and changing the first name
'''names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Jon'
print(names[0:3])
print(names) '''

# List of numbers checking if a number is in the list
'''numbers = [1, 2, 3, 4, 5]

print(1 in numbers)'''

