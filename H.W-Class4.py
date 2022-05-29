import requests

# API Testing

# 1. Testing Github API - Create a program in python that goes to the following API and
# checks that at least 5 git repositories exists - https://api.github.com/users/avielb/repos

repository_list = requests.get("https://api.github.com/users/avielb/repos")
print("repos.status_code " + str(repository_list.status_code))
assert len(repository_list.json()) >= 5
repository_list = repository_list.json()
print(repository_list[4].keys())
print(len(repository_list))

# 2. Testing agify API - Create a program in python that generates 3 random names and
# checks that the age from the reply in this link: https://api.agify.io/?name=<name> is
# between 0 - 120

import names
my_names = []
for i in range(3):
   if not 0 <= requests.get(f"https://api.agify.io/?name={names.get_first_name()}"
     ).json()["age"] <= 120:
     my_names.append(i)
   assert len(my_names) == 0


# 3. Testing universities API - Go to http://universities.hipolabs.com/search?country=Israel
# and make sure that israel has at least 5 universities

universities_list = requests.get("http://universities.hipolabs.com/search?country=Israel")
print("iniver.status_code " + str(universities_list.status_code))
assert len(universities_list.json()) >= 5
universities_list = universities_list.json()
print(universities_list[4].keys())
print(len(universities_list))


# UI Testing

from selenium import webdriver
my_driver = webdriver.Chrome(executable_path="C:/Users/yargo/Downloads/chromedriver")
my_driver2 = webdriver.Chrome(executable_path="C:/Users/yargo/Downloads/chromedriver")

my_driver.get("https://www.ycombinator.com/")
my_driver2.get("https://hub.docker.com")

# 4. Using Selenium go to https://www.ycombinator.com/ and test that the title is “Y
# Combinator”
assert my_driver.title == "Y Combinator"


# 5. Using selenium go to https://hub.docker.com and test the the title is “Docker Hub
# Container Image Library | App Containerization”
assert my_driver2.title == "Docker Hub Container Image Library |App Containerization"
