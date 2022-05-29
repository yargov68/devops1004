a = "hello world"
print(a)
#0 to 4
#20 to -7
print(list(range(20, -10, -3)))

for i in range(1 ,6):
#    print(f"{i} hello")
    print(f"hello world #{i}")

my_names = ["adi", "ben","noam"]

for name in my_names:
#    my_names[my_names.index()]
    print(f"hello  {name}")
    if name == "yoel":
        inish_ok = False
        braek
else:
    print("printed all names")

#לפי גודל הליסט הוא מדפיס
for i in range(len(my_names)):
#    my_names[i] = "moshe"
    print(my_names[i])
a = 0

while a < 5:
    print(a)
    a = a + 1
    if a == 2:
       break
#        continue

    a = a + 1


l = []
current_input = input ("enter letter: ")
while current_input != "q":
      l.append(current_input)
      current_input = input("enter letter: ")

print(f"inputs are {l}")

n = [1, 2, 3, 4, 5]

result = [num * 2 for num in n if num > 2]
for num in n:
    if num > 2:
       result.append(num *2)

