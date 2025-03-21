#Menu List
# empty list
'''import time


new_menu_Mohales = []

#dishes for the new menu
dish1 = "Pasta"
dish2 = "Pizza"
dish3 = "Burger"

#function definition
def add_to_menu(menu, dish):
    menu.append(dish)

#adding dish 1
add_to_menu(new_menu_Mohales, dish1)
print(new_menu_Mohales)

time.sleep(4)

#adding dish 2
add_to_menu(new_menu_Mohales, dish2)
print(new_menu_Mohales)

time.sleep(4)

#adding dish 3
add_to_menu(new_menu_Mohales, dish3)
print(new_menu_Mohales)'''

'''cart = []

def add_to_cart(cart):
    try:
        product = input("Enter product (or Type 'Exit'to quit): ")
        if product.lower() == 'exit':
            print('Exiting...')
            return
        cart.append(product)
    except KeyboardInterrupt:
        print('\nProcess interrupted by user.')
        exit() 

cart = []
add_to_cart(cart)
'''
'''
delivery = True

def to_deliver(delivery):
    if delivery == True:
        print('Enter your address')

to_deliver(delivery)'''

'''books = ['1984','War and Peace', 'The Great Gatsby']
book = 'Animal Farm'
def book_in_Library(books, book):
    return book in books
print(book_in_Library(books, book))'''

'''products = ['pen', 'pencil', 'ruler']
print(len(products))'''

#Sum of the numbers in a list
'''prices = [33, 49, 55,14]
total = sum(prices)
print(total)'''

'''values = ['1', '2', '3']
print(sum(values))'''

#Average, count and total

'''prices = [ 33,49,55,14]

total = sum(prices)
print('Total:', total)

number_of_products = len(prices)
print('Count:', number_of_products)

avg_price = total/number_of_products
print('Average:', avg_price)'''

#Sorting them in order starting with the smallest

'''ages = [22, 19, 24, 25, 26, 24, 25, 24]
sorted_ages = sorted(ages)
print(sorted_ages)
'''

'''prices = [503.9,199.9, 254.5, 39.9]
srt_prices = sorted(prices)
print(srt_prices[1])'''

#From GEEk of GEEKS
'''a = [1,2,3,4,5]

b = [ 'apple', 'banana', 'cherry']

c = [1, 'hello', 3.14, True]

print(a)
print(b)
print(c)'''

'''a = list ((1,2,3, 'apple', 4,5,6))

print(a)'''

'''a = [10,20,30,40,50] 

print(a[0])
print(a[-1])'''

'''a = []

a.append(10)
print('After append(10):', a)

a.insert(0, 5)
print('After insert(0, 5):', a)

a.extend([15,20,25])
print('After extent([15,20,25])', a) 
'''

# Replacing a number
'''a = [ 10,20,30,40,50]

a[1] = 25

print(a)
'''
# Removing Elements from the list

'''a = [10,20,30,40,50]

a.remove(30)
print('After remove(30):', a)

popped_val = a.pop(1)
print('Popped element:', popped_val)
print('After pop(1):', a)

del a[0]
print('After del a[0]:', a)
'''

# Iterating Over a list

'''a = ['apple', 'banana', 'cherry']

for fruit in a:
    print(fruit)'''

'''matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
# Access element at row 2,column 3
print(matrix[1][2])'''

#Tuple
'''birthday_day = (1981,"May", 12)
tuple_to_list = list(birthday_day)
print(birthday_day)
print(tuple_to_list)'''

'''sizes = [15,44,5]
print(sizes[2])'''
# to count() function to calculate the number of occurences of an item in a tuple
'''scores = (10,20,30,40,30,10,30,30)

print ('# of 10 :', scores.count(10))
print ('# of 30:', scores.count(30))
print('# of 3:', scores.count(3))'''

'''points = (12, 14, 9, 10, 9)
for point in points:
    print(point, ':passed')'''

'''points = (12, 14, 9, 10, 9)
for point in points:
    if point >= 14:
        print(point)'''

#Data type

'''t = (1,2,3,4,5)
print(t)
print(type(t))'''

#Tuples

'''list1= (1,2,3,4,5)
list2 = (6,7,8,9,10)
list3 = list1 + list2
print(list3)
print(type(list3))
print(len(list3))
print(list3[0])'''

'''sizes = (15,44,5)
print(sizes[2])'''

'''points = (12, 14, 9, 10, 9)
for point in points:
    if point >= 14:
        print(point)'''

'''birthday_day = (1981,"May", 12)
day, month, year = birthday_day
print(day)
print(month)
print(year)'''

# Reorder to get the correct output

'''years = [2002,2008,1999]
years[1] = 2007
for year in years:
    print(year)'''

'''dishes = ['pizza', 'pasta', 'burger']
guests = ['John', 'David', 'Lucy']

print(dishes[0])
print(guests[0])
'''

'''car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964

}
print(car['brand'])
print(car['model'])
print(car['year'])'''

'''contact = {
    'name': 'John',
    'company': 'Google'
}

print(contact['company'])'''

'''contact = {
    'name': 'John',
    'company': 'Google'
}
info_keys = contact.keys()
info_values = contact.values()

print(info_keys)
print(info_values)'''

'''car = {
    'brand': 'Ford',
    'model': 'Mustang',
}
info = car.items()
print(info)'''

user = {
    'name': 'John',
    'age': 25,
}
user['age'] = 26

print(user['age'])
print(user.items())