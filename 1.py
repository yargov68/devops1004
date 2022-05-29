a = print("hello world!")
b = 4
c = False
d = ["ben","raz" , 32 , ["ski", "snowbord"]]
e = ["aviel", 32 , True]
f = {"fname": "ben", "lname": "raz", "age": 32, "hobbies": ["ski"]}
print(a)
print(b)
print(d[1])
d[3] = ["guitar"]
print(d)
e[2] = 40
print(e)
print(f["lname"])
if f["lname"] == "ben":
    print("your name is ben")