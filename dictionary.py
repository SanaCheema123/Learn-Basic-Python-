#...................................................Creating dictionary..........................................
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
empty_dict = {}
print(my_dict)
print(empty_dict)

#Accessing Elements
name = my_dict['name']
print(name)
age = my_dict.get('age')
print(age)

#Modifying Elements
my_dict['age'] = 29
age = my_dict.get('age')
print(age)

#Adding Elements
my_dict['email'] = 'alice@example.com'
print(my_dict)

#Removing Elements
#1: Using del
del my_dict['city']
print(my_dict)

#2:Using pop
email = my_dict.pop('email')
print(my_dict)

#3: Using popitem (removes the last inserted key-value pair)
last_item = my_dict.popitem()
print(my_dict)


#...............................................Dictionary Methods..................................................
#1: Keys, Values, and Items
#Keys
keys = my_dict.keys()
print(keys)

#Values
values = my_dict.values()
print(values)

#Items
items = my_dict.items()
print(items)

#2: Checking Existence of Keys
is_name_in_dict = 'name' in my_dict
print(is_name_in_dict)
is_city_in_dict = 'city' in my_dict
print(is_city_in_dict)

#3: Copying

#Shallow Copy
copied_dict = my_dict.copy()
print(copied_dict)

#Deep Copy
import copy
deep_copied_dict = copy.deepcopy(my_dict)
print(deep_copied_dict)

#4: Merging Dictionaries

#Using update
my_dict.update({'city': 'New York', 'email': 'alice@example.com'})
print(my_dict)

#Using dictionary unpacking (Python 3.5+)
dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city': 'New York', 'email': 'alice@example.com'}
merged_dict = {**dict1, **dict2}
print(merged_dict)


#5: Setting Default Values

age = my_dict.setdefault('age', 30)
print(age)
country = my_dict.setdefault('country', 'USA')
print(country)

#..............................................................Dictionary Comprehensions.......................................................
#Creating a Dictionary with Comprehensions
squares = {x: x ** 2 for x in range(6)}
print(squares)

# ..........................................................Iterating Through Dictionaries....................................................
#1: Iterating Over Keys
for key in my_dict:
    print(key)

#2: Iterating Over Values
for value in my_dict.values():
    print(value)

#3: Iterating Over Key-Value Pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

#Advanced Dictionary Operations
#Dictionary from Keys
keys = ['name', 'age', 'city']
default_value = None
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

#Counting with Dictionaries
text = "hello world"
count_dict = {}
for char in text:
    count_dict[char] = count_dict.get(char, 0) + 1
print(count_dict)