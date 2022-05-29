try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print(a / b)
    r = open("file_not_exists")
except ZeroDivisionError:
#except Exception as e:
    print("divide by zero")
except FileNotFoundError:
    print("not found")
except Exception as e:
    print(e.args)
#print("bla")


# import requests
# requests.get("ht5p://www.google.com")