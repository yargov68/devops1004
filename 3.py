# First Exercise By Yoel Argov

# A. Create a program with the following:
first = 7
second = 44.3
print(first + second)
print(first * second)
print(second / first)

#B.
#What will be the values of a, b, c at the end?
a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8
print("a :", a  ," b:",b ," c:" ,c)

#C.
#Is there a difference between the two lines below? Why?
#name = “john”
#name = ‘john’
#  אין הבדל , ניתן לשים מחרוזת בין גרשים ובין גרשיים

#D.
#What will be the output?
x = 5
y = 2.36
print(x+int(y))
#7

#Suggest an edit.
my_number = 5 + 5
print("result is: " , my_number)
#10


#CHALLENGE:
#Fix the following code, without changing a or b
a = 8
b = "123"
print(a+int(b))
#131

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

print("yoel")