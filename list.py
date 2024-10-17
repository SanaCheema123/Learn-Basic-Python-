# ....................................................Basic List Operations.................................................
#1: Creating Lists

my_list = [1, 2, 3, 4, 5]
print(my_list)
empty_list = []
print(empty_list)
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)

#2: Accessing Elements
#Indexing
my_list = [1, 2, 3, 4, 5]
first_element = my_list[0]
print(first_element)
last_element = my_list[-1]
print(last_element)

#Slicing
sublist = my_list[1:4]
print(sublist)

#3: Modifying Elements
my_list[2] = 10
print(my_list)

#4: Adding Elements

#Append
my_list.append(6)
print(my_list)

#Insert
my_list.insert(2, 7)
print(my_list)

#Extend
my_list.extend([8, 9])
print(my_list)

#5: Removing Elements

#Remove
my_list.remove(7)
print(my_list)
#Pop
last_element = my_list.pop()
index_element = my_list.pop(2)
print(last_element)
print(index_element)
#Clear
my_list.clear()
print(my_list)


#.....................................................List Operations and Methods....................................................
#1: Length
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print(length)

#2: Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)

#3: Repetition
repeated_list = list1 * 2
print(repeated_list)

#4: Membership

is_in_list = 2 in list1
# Output: True
is_not_in_list = 7 not in list1
# Output: True

#5: Sorting

#Sort in Place
unsorted_list = [3, 1, 4, 5, 2]
unsorted_list.sort()
print(unsorted_list)

#Sort and Return New List
sorted_list = sorted(unsorted_list, reverse=True)
print(sorted_list)


#6: Reversing

#Reverse in Place
my_list.reverse()
print(my_list)

#Reverse and Return New List
reversed_list = list(reversed(my_list))
print(reversed_list)

#7: Finding Elements

# Index
my_list = [1, 2, 3, 4, 5]
index_of_3 = my_list.index(3)
print(index_of_3)

#Count
my_list = [1, 2, 3, 2, 2, 4, 5]
count_of_2 = my_list.count(2)
print(count_of_2)

#8: Copying

#Shallow Copy
copied_list = my_list.copy()
print(copied_list)

#Deep Copy
import copy
deep_copied_list = copy.deepcopy(my_list)
print(deep_copied_list)

#.....................................................Advanced List Operations................................................

#1: List Comprehensions

squared_numbers = [x ** 2 for x in range(10)]
print(squared_numbers)
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)


#2: Nested Lists

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = nested_list[1][2]
print(element)

#3: List Unpacking
a, b, c = [1, 2, 3]
print(a)

#4:Filtering and Mapping

#Filter
filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(filtered_list)

#Map
mapped_list = list(map(lambda x: x * 2, my_list))
print(mapped_list)