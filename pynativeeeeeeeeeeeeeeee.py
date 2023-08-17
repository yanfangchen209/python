#basic exercise for beginners: exercise
'''
def calculate(num1, num2):
    product = num1 * num2
    sum = num1 + num2
    if(product <= 1000):
        return product
    else:
        return sum
        
print(calculate(20, 30))
print(calculate(40, 30))

#######################
def printsum():
    print("Printing current and previous number sum in a range(10)")
    print("Current Number 0 Previous Number 0 Sum: 0")
    for i in range(1,10):
        print(f'Current Number {i} Previous Number  {i-1}  Sum:  {2*i - 1}')
        #print('Current Number' + str(i) + 'Previous Number'+  str(i-1) + 'Sum:'  + str(2*i - 1))
        #print('Current Number', i ,'Previous Number', i - 1, 'Sum:', 2*i - 1)

printsum()

##################################
def printevenstr():
    word = input()
    print("Original String is :", word)
    print('Printing only even index chars')
    for i in range(len(word)):
        if i % 2 == 0:
            print(word[i])
        
    
printevenstr()
##############################################

#string in python is immutable like java , below is string slicing
def removestr(word, n):
    size = len(word)
    newword = word[n:]
    # newword = word[n: size]
    return newword

print(removestr('pynative', 4))
print(removestr('pynative', 2))
##############################################
def listcheck(numbers):
    if numbers[0]  == numbers[-1]:
        return True
    else:
        return False
print(listcheck([10, 20, 30, 40, 10]))
print(listcheck([75, 20, 30, 40, 10]))
##############################################

#exercise 6

def display(nums):
    print('Given list is ', nums)
    print('Divisible by 5')
    for i in nums:
        if i % 5 == 0:
            print(i)
display([10, 20, 33, 46, 55])

###################################################
#Exercise 7: Return the count of a given substring from a string
def strfrequency(sentence, word):
    count = sentence.count(word)
    print(word, 'appeared', count, 'times')
strfrequency('Emma is good developer. Emma is a writer', 'Emma')
######################################################
#Exercise 8: Print the following pattern

for i in range(5):
    for j in range(i + 1):
        print(i + 1, end=" ")
    print('\n')
 
######################################################
#Exercise 9: Check Palindrome Number

def ispalindrome(num):
    print('original number ', 121)
    str_format = str(num)
    left = 0
    right = len(str_format) - 1
    while left < right:
        if str_format[left] != str_format[right]:
            return False
        left += 1
        right -= 1
    return True
    
print(ispalindrome(121))
print(ispalindrome(125))

def palindrome(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)

#######################################
#Create a new list from a two list using the following condition
def createlist(list1, list2):
    result_list = []
    for i in list1:
        if i % 2 == 1:
            result_list.append(i)
    for j in list2:
        if j % 2 == 0:
            result_list.append(j)
    return result_list
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(createlist(list1, list2))

##############################3
#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
def reverseint(n):
    
    while n > 0:
        last_digit = n % 10
        print(last_digit, end=" ")
        n = n // 10

print(reverseint(7536))

#####################################
#  Exercise 12: Calculate income tax for the given income by adhering to the below rules
def calc_tax(income):
    
    if income <= 10000:
        tax  = 0;
    elif income <= 20000:
        tax = (income - 10000) * 0.1
    else:
        tax  = 10000 * 0.1 + (income - 20000)*0.2
    return tax 
print(calc_tax(45000))
print(calc_tax(65000))
print(calc_tax(10000))
print(calc_tax(9000))
print(calc_tax(20000))
print(calc_tax(18000))
print(calc_tax(65000))

##################################
#Exercise 13: Print multiplication table form 1 to 10

def multiplication_table():
    for i in range (1, 11):
        for j in range(1, 11):
            print(i * j, end=' ')
        print('\n')
        
multiplication_table()

################################
#Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
#range(5, 0, -1) generates a sequence of numbers starting from 6 down to 1 (inclusive) with a step of -1, which means it's counting backwards.
def print_half_pyramid_star():
    for i in range(5, 0, -1):
        for j in range(0, i):
            print('*', end=' ')
        print('\n')
print_half_pyramid_star()

######################################
#Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def calc_exponent(num, power):
    product = 1
    for i in range(0, power):
        product *= num
    return product
print(calc_exponent(2, 10))

##############################################
#Python Input and Output Exercise
#Exercise 1: Accept numbers from a user
num1 = input('enter first number:')
num2 = input('enter second number:')
product = int(num1) * int(num2)

###################################
#Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
str1 = 'Name'
str2 = 'Is'
str3 = 'James'
new_str = str1 + '**' + str2 + '**' + str3
print(new_str)
print('My', 'Name', 'Is', 'James', sep='**')

###################################
#Exercise 3: Convert Decimal number to octal using print() output formatting
num = 90
print('%o' % num)

###################################
#Exercise 4: Display float number with 2 decimal places using print()
a = 0.999
print('%.2f' %a)

###################################
#Exercise 5: Accept a list of 5 float numbers as an input from the user
new_list = []
for i in range(0,5):
    new_list.append(float(input('enter a float number:')))
    
print(new_list)

###################################
#Exercise 6: Write all content of a given file into a new file by skipping line number 5
#Use range() to generate a sequence of numbers starting from 9 to 100 divisible by 3.
for i in range(9, 100, 3):
    print(i, end=' ')
'''  
    
for char in range ('a','z'):
    print(char)