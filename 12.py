# my_file  = open("urls.txt")
# #returns list
# for line in my_file.readlines():
#     print(line, end=' ') # .strip()

def get_name(name):
    my_file = open("names.txt", "w")
    my_file.write(f"{name}\n")
    my_file.close()

print(get_name("enter your name: "))

def add_hello(prefix):
    for line in my_file.readlines():
#     print(line, end=' ') # .strip()


#insert 5 name
# my_file  = open("names.txt", "w")
# for i in range(5):
#     current_name =input("enter your name: ")
#     my_file.write(f"{current_name}\n")
#
# my_file.close()