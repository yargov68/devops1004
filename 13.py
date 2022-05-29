
def save_name():
    n = input("enter your name: ")
    my_file = open ("names.txt", "a")
    my_file.write(f"{n}\n")

#
def show_names():
    with open("names.txt") as my_file:
        for line in my_file.readlines():
            print(f"hello {line}", end='')

def url_caller(url):
response = request.get(url)
if response.status_code == 200:
    print(f"{url} is ok")

def call_urls():
    with open("urls.txt") as urls:
        url_caller(line.strip())

#save_name()
#show_names()
#url_caller
call_urls()