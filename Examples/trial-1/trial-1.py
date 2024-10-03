import os
import math
import re
import getpass
from datetime import date
import pickle
import sys

# Function to filter valid float input
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid numeric value.")

# Function to filter valid string input
def get_string_input(prompt):
    return input(prompt).strip()

# Initial greetings
print("Hello World.")
name = get_string_input("My name is: ")
print("My name is " + name)

# Comparison of two numbers
a = 1
b = 3
if a > b:
    print("a is Greater") 
else:
    print("b is Greater")

# String concatenation
string1 = "Linux"
string2 = "Hint"
joined_string = string1 + string2
print(joined_string)

# Use of String Formatting
float1 = 563.78453
print("{:5.2f}".format(float1))

# Use of String Interpolation
float2 = 563.78453
print("%5.2f" % float2)

# Power calculations
x = 4
n = 3
power = x ** n
print("%d to the power %d is %d" % (x, n, power))
power = pow(x, n)
print("%d to the power %d is %d" % (x, n, power))
power = math.pow(2, 6.5)
print("%d to the power %d is %5.2f" % (x, n, power))

# Boolean value
val1 = True
print(val1)

# Numeric values to Boolean
for number in [10, -5, 0]:
    print(f"Boolean of {number} is {bool(number)}")

# Comparison operator example
val1, val2 = 6, 3
print(val1 < val2)

# Passing condition
number = get_float_input("Enter a number to check if it's more than or equal to 70: ")
if number >= 70:
    print("You have passed")
else:
    print("You have not passed")

# Take MCQ and Theory marks
mcq_marks = get_float_input("Enter the MCQ marks: ")
theory_marks = get_float_input("Enter the Theory marks: ")

# Check passing condition
if (mcq_marks >= 40 and theory_marks >= 30) or (mcq_marks + theory_marks) >= 70:
    print("\nYou have passed")
else:
    print("\nYou have failed")

# Switch case implementation
def employee_details(ID):
    switcher = {
        "1004": "Employee Name: MD. Mehrab",
        "1009": "Employee Name: Mita Rahman",  
        "1010": "Employee Name: Sakib Al Hasan",
    }
    return switcher.get(ID, "nothing")

# Employee ID input
ID = get_string_input("Enter the employee ID: ")
print(employee_details(ID))

# Counter loop
for counter in range(1, 6):
    print("The current counter value: %d" % counter)

# Weekdays iteration
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("Seven Weekdays are:\n")
for day in weekdays:
    print(day)

# Command-line arguments
print('Total arguments:', len(sys.argv))
print("Argument values are:")
for i in sys.argv:
    print(i)

# Regular expression matching
string = get_string_input("Enter a string value: ")
pattern = '^[A-Z]'
found = re.match(pattern, string)
if found:
    print("The input value starts with a capital letter")
else:
    print("You have to type a string starting with a capital letter")

# Password input using getpass
passwd = getpass.getpass('Password: ')
if passwd == "fahmida":
    print("You are authenticated")
else:
    print("You are not authenticated")

# Date example
current_date = date.today()
print("Today is :%d-%d-%d" % (current_date.day, current_date.month, current_date.year))
custom_date = date(2020, 12, 16)
print("The date is:", custom_date)

# Fruit list manipulation
fruits = ["Mango", "Orange", "Guava", "Banana"]
fruits.insert(1, "Grape")
print("The fruit list after insert:")
print(fruits)
fruits.remove("Guava")
print("The fruit list after delete:")
print(fruits)

# List comprehension examples
char_list = [char for char in "linuxhint"]
print(char_list)
websites = ("google.com", "yahoo.com", "ask.com", "bing.com")
site_list = [site for site in websites]
print(site_list)

# String slicing
text = "Learn Python Programming"
print(text[:5])    # Slice using one parameter
print(text[6:12])  # Slice using two parameters
print(text[6:25:5])  # Slice using three parameters

# Dictionary example
customers = {'06753': 'Mehzabin Afroze', '02457': 'Md. Ali', '02834': 'Mosarof Ahmed', '05623': 'Mila Hasan', '07895': 'Yaqub Ali'}
customers['05634'] = 'Mehboba Ferdous'
print("The customer names are:")
for customer in customers.values():
    print(customer)
name = get_string_input("Enter customer ID: ")
print(customers.get(name, "Customer ID not found."))

# Set example
numbers = {23, 90, 56, 78, 12, 34, 67}
numbers.add(50)
print(numbers)
search_number = int(get_float_input("Enter a number to search in the set: "))
message = "Number is not found"
if search_number in numbers:
    message = "Number is found"
print(message)

# Count occurrences of a string
string = 'Python Bash Java Python PHP PERL'
search = 'Python'
count = string.count(search)
print("%s appears %d times" % (search, count))

# Function examples
def addition(number1, number2):
    result = number1 + number2
    print("Addition result:", result)

def area(radius):
    return 3.14 * radius * radius

# Call functions
addition(400, 300)
print("Area of the circle is", area(4))

# Try-except block for even or odd
try:
    number = int(get_float_input("Enter a number to check if it's even or odd: "))
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
except ValueError:
    print("Enter a numeric value")

# File handling
filename = "languages.txt"
with open(filename, "w") as fileHandler:
    fileHandler.write("Bash\n")
    fileHandler.write("Python\n")
    fileHandler.write("PHP\n")

with open(filename, "r") as fileHandler:
    for line in fileHandler:
        print(line.strip())

# Read directory contents
path = './'
files = os.listdir(path)
print("Files in the directory:")
for file in files:
    print(file)

# Pickle example
dataObject = []
for num in range(10, 15):
    dataObject.append(num)

with open('languages', 'wb') as file_handler:
    pickle.dump(dataObject, file_handler)

with open('languages', 'rb') as file_handler:
    dataObject = pickle.load(file_handler)
    for val in dataObject:
        print('The data value:', val)

# Class example
class Employee:
    name = "Mostak Mahmud"
    def details(self):
        print("Post: Marketing Officer")
        print("Department: Sales")
        print("Salary: $1000")

# Create the employee object    
emp = Employee()
print("Name:", emp.name)
emp.details()

# Range examples
for val in range(6):
    print(val, end='  ')
print('\n')

for val in range(5, 10):
    print(val, end='  ')
print('\n')

for val in range(0, 8, 2):
    print(val, end='  ')

# Calculate power using map
def cal_power(n):
    return x ** n

x = int(get_float_input("Enter the value of x for power calculation: "))
numbers = [2, 3, 4]
result = map(cal_power, numbers)
print(list(result))

# Participant selection
participant = ['Monalisa', 'Akbar Hossain', 'Jakir Hasan', 'Zahadur Rahman', 'Zenifer Lopez']
def SelectedPerson(participant):
    selected = ['Akbar Hossain', 'Zillur Rahman', 'Monalisa']
    return participant in selected

selectedList = filter(SelectedPerson, participant)
print('The selected candidates are:')
for candidate in selectedList:
    print(candidate)
