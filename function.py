def square(num):
    result = num * num
    return result, num #tuple

#a = square(4)
a = square(16)
print(a)
#square(4)
#square(10

a = int(input("enter your age: "))
if 0 < a < 120:
    print("ok")
else:
    print("not ok")

b = int(input("enter amount of pets: "))
if 0 < b < 4:
    print("ok")
else:
    print("not ok")

def validate(prompt, low, high, ok, not_ok):
    input_from_user = int(input(prompt))
    if low < input_from_user < high:
        return ok
    else:
        return not_ok

print(validate("enter your age: ", 0, 120, "age is good", "age"))
print(validate("enter a number of pets ", 0, 4,"good","bad"))

#not to do if we move the function we have to move a
a = 4
def moshe ():
    print(a)

