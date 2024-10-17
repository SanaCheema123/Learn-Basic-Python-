#ssignment: Exploring Python String Methods
#Tasks:

#1: Concatenation and Repetition

#Create two strings, str1 and str2, with the values "Hello" and "World" respectively.
#Concatenate these strings with a space in between and print the result.
str1="Hello"
str2="World"
print(str1 + " " +str2)

#Repeat the concatenated string 3 times and print the result.
str1="Hello"
str2="World"
result=" " +str1 + " " +str2
print(result*3)

#2: Indexing and Slicing

#Use the string "Hello, World!" for this task.
#Print the first character.
var3="Hello, World!"
print(var3[0])
#Print the last character.
var3="Hello, World!"
print(var3[-1])
#Print the substring from index 7 to the end of the string.
var3="Hello, World!"
print(var3[0:7])
#Print the substring from the start of the string to index 5.
var3="Hello, World!"
print(var3[0:5])


#3: String Case Conversion

#Convert the string "python programming" to all uppercase and print the result.
str4="python programming"
print(str4.upper())
#Convert the string "PYTHON PROGRAMMING" to all lowercase and print the result.
str4="python programming"
print(str4.lower())
#Convert the string "python programming" to title case and print the result.
str4="python programming"
print(str4.title())


#4:Trimming Whitespaces

#Use the string " Welcome to Python! " for this task.
#Trim the leading and trailing whitespaces and print the result.
org_str = "         Welcome to Python!             "
# Trimming the whitespaces
trim_string = org_str.strip()
# Printing the trimmed string
print(trim_string)


#5: String Replacement

#Replace the word "World" with "Python" in the string "Hello, World!" and print the result.
var5="Hello, World!"
result=var5.replace("World!", "Python")
print(result)


#6: Splitting and Joining Strings

#Split the string "apple, banana, cherry" by the comma , and print the resulting list.
fruits_str = "apple, banana, cherry"
fruits_list = fruits_str.split(", ")
print(fruits_list)

#Join the list ["apple", "banana", "cherry"] into a single string with commas separating the items and print the result.
fruits_list = ["apple", "banana", "cherry"]
join_string = ", ".join(fruits_list)
print(join_string)

#7: Finding Substrings
text = "Hello, World! Hello, everyone!"
#Find and print the index of the first occurrence of the substring "World" in the string "Hello, World! Hello, everyone!".
index_world = text.find("World")
print("Index of 'World':", index_world)

#Count and print the number of times the substring "Hello" appears in the same string
count_hello = text.count("Hello")
print("Number of times 'Hello' appears:", count_hello)

#8: String Checking Methods

string_alnum = "Python123"
is_alnum = string_alnum.isalnum()
print("Is 'Python123' alphanumeric?", is_alnum)

# Checking if the string contains only digits
string_digits = "12345"
is_digits = string_digits.isdigit()
print("Does '12345' contain only digits?", is_digits)

# Checking if the string contains only whitespace
string_space = " "
is_space = string_space.isspace()


#9: String Formatting
name = "Sana Cheema"
age = 26
#Use the variables name and age with values "Alice" and 30 respectively.
formatted_string = "My name is {0} and I am {1} years old.".format(name, age)
print(formatted_string)

#Print the string "My name is Alice and I am 30 years old." using the format() method.
f_string = f"My name is {name} and I am {age} years old."
print(f_string)
