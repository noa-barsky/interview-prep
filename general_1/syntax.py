#Basic Python3 syntax:
print ("hello world")

#Comments: 
'''
multiline comment
'''
# single line

#Variables: 
name = "Noa"
print (name)

#operations
#/, // (integer), **, *, % (remainder), +, -
#order of operation matters

#String contatenation
new_str = "hey" + " Noa"

print ("The string is %s", new_str) #automatically prints a new line, to not go ,end=""

#Lists:

grocery_list = ["noa", True, 123 ]
print (grocery_list)
list_o_list = [["cool", 12], [3,4]]
print (list_o_list[0][0])

#List functions
samp_lst = [4,6,1225,12,51,2,2]

samp_lst.append(6)
samp_lst.insert(5,5)
samp_lst.remove(4)
samp_lst.sort()
samp_lst.reverse()
samp_lst.pop(0)
samp_lst.append(900)
# these all work for tuples as well
len(samp_lst)
min(samp_lst)
max(samp_lst)
print(samp_lst)

#tuples
#tuples are immutable
tup = (2,3,4,5)

#dictionaries
grades = {"Bob": 90, "Sarah": 70, "Bobert": 40}

print(grades["Bobert"])
print(grades.keys())
print(grades.values())

#Conditionals

age = 20

if age > 16:
    print ("dope")
elif age>40:
    print ("t")
else:
    print ("nope")

#logic
if (age > 16) and not (name == "noa"):
    print ("dope")
elif (age>40) or (name == "noa"):
    print ("t")
else:
    print ("nope")

for i in range(0,10): #exlcusive of 10
    print(i)
    continue

while age == 20:
    print("Hey")
    break


#generate random number
import random
print(random.randint(0,11))

#functions
def addNums(a,b):
    return a+b

print(addNums(2,3))

#name = input("What is your name")
print(name)

#strings

long_str = "This is a sentence"
print(long_str[0:5])
new_str = "new str"
print(long_str+new_str)

#useful string function
print(long_str.upper())
print(long_str.lower())
print(long_str.isalpha())
print(long_str.isalnum())
print(long_str.strip())
print(long_str.split(" ")) #string to list, split on whitespace

#I/O file handling
test_file = open("text.txt", "w") #w being write to r being read
test_file.write("hey")
test_file = open("text.txt", "r")
print(test_file.read())
print(type(test_file))
#OO
class Animal:
    __name = "" #all private values
    __height = 0
    __weight = 0
    __sound = ""

    def __init__(self,name,height,weight,sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound



    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

cat = Animal ("whiskers", 33, 10,"sound" )
cat.set_name("bob")
print(cat.get_name())

class Dog(Animal):
    __owner = ""
    def __init__ (self,name,height,weight,sound, owner):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
        self.__owner = owner
    def set_owner(self,owner):
        self.__owner=owner
    def get_owner(self):
        return self.__owner

dog = Dog("bob",100,100,"bark","Noa")
print(dog.get_owner())