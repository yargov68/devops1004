isTrue = False
a = 2
b = 2.5
srtOne = "one"
strThree = "Three"
c = [1, 2, 3]
d = [1, 2, 3]
if c == d:
    print("c eq d")
if a is b:
    print("a is b")
if c is d:
    print("c is d")

print(type(a))
if type(a) is int:
    print("int")


age = int(input("enter your age: "))
if 0 < age < 120:
    print("ok")
my_names = ["adi", "ben","noam"]
my_list = []
if my_list:
    print("my not empty ")

if my_names:
    print("not")

if len(strThree) > 2:
    print("i enougf")
print(len(my_names))

#if my_names [0] == "zoar":

if "zohar" not in my_names:
    print("NOT found zohar")

if a < b and not (strThree == 3 or isTrue == 4):
    print("a is less then b")
elif a == b:
    print("a is equal")
else:
    print("a is greater then b")