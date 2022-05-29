#Second class HOME WORK BY YOEL ARGOV

#A.
#1. Create two variables name X and Y.
#2. Print “BIG” if X is bigger than Y .
#3. Print “small” if X is smaller than Y.

x = 55
y = 60

if x > y:
    print("big")
else:
    print("small")

#B.
#1. Run a “for” loop 5 times.
#2. Print iteration number every time.

for x in range(5):
    print(x)

#C.
#1. Create a variable and initialize it with a number 1-4.
#2. Create 4 conditions (if-elif) which will check the variable.
#3. print the season name accordingly:

#- 1 = summer
#- 2 = winter
#- 3 = fall
#- 4 = spring

season = 4
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")

#D.
#1. how many times will the following loop run?
#2. what will be printed last?

count = 1
while count < 11:
    print(count)
    count = count + 1
# it will print count, 10 times

#E.
#Write a program with variables holding the following:
#1. Your age.
#2. First letter of your last name.
#3. Current shekels-dollar currency.
#4. Did you flew abroad (true/false)
#5. Your apartment number.

#● Print all variables.
#● Add the currency to your age, and check the result.

age = 50
first_letter = "y"
currency = 3.22
flew_abroad = True
apartment_number = 20

print("age: " + str(age))
print("first letter: " + first_letter )
print("currency rate :" + str(currency))
print (flew_abroad)
print("apartment number : " + str(apartment_number))
print(currency+age)


#F.
#Create a program which uses input with the following:
#1. Ask user for his phone number
#2. Print the words “phone number” and the phone number the
#user entered.

number = input("Enter your phone number: ")
print("Phone number", number)

#G.
#Write a program with the following:
#1. Method named printHello() that prints the word “hello”.
#2. Method named calculate() which adds 5+3.2 and prints the
#result.

def printHello():
    print("hello")

def calculate():
    print(5+3.2)

printHello()
calculate()


#H.
#Write a program with the following:
#1. Method that receive your name and prints it.
#2. Method that receive a number, divide it by 2, and prints the
#result.

def print_name(prompt, name):
    print(prompt, name)

def divide_number(prompt, num):
    print(prompt, num/2)

print_name("My Name Is :", "Yoel Argov")

Result = divide_number("The Result Is : " , 10)

#I.
#Write a program with the following:
#1. Method that receive two numbers, add them, and return the
#sum.
#2. Method that receive two Strings, add space between them,
#and return one spaced string.

def return_sum(x,y):
    return x+y

def add_space(word_a, word_b):
    return word_a + " " + word_b

print("The Summation Of Two Numbers Is: " + str(return_sum(10, 30)))

print("The Concatanation Of Two Strings Is: " + add_space("Hello", "World"))


#Challenges:

#K.
#Create a nested for loop (loop inside another loop) to create
#a pyramid shape:
for i in range(1,10):
    for j in range(1, i):
        print("*", end="")
    print('')

#Create a nested for loop to create 5 shape (width is 7,
#length is 7):
print('')
result_str=""
for row in range(7):
    for column in range(0,7):
        if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or \
                (column == 1 and (row == 1 or row == 2 or row == 6)) or \
                (column == 5 and (row == 0 or row == 4 or row == 5))):
            result_str += "*"
        else:
            result_str += " "
    result_str=result_str+"\n"
print(result_str)

#M.
#Write a program with the following:
#1. Method that gets a number from the user (using input).
#2. Method that receive the number from the first method, and
#computes the sum of the digits the integer (e.g. 25 = 7, 2+5=7)


def get_number(prompt):
    input_from_user = input(prompt)
    toatal_sum = sum_digits(input_from_user)
    print (" The Sum Of Digits That Were Given Is :", toatal_sum)

def sum_digits(input_from_user):
    temp_sum = 0
    for char in input_from_user:
       temp_sum = temp_sum + int(char)
    return temp_sum

print(get_number("enter your number: "))

