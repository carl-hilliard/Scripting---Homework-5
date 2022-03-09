"""
Carl Hilliard
Intro to Scripting
Assignment 5
"""

## Problem 1




## Problem 2
length = len(string)
def numVowels(string):
    count = 0
    for i in range(len(string)):
        if(string[i] == 'a' or string[i] == 'A' or string[i] == 'e' or string[i] == 'E' or string[i] == 'i' or string[i] =='I' or string[i] == 'o' or string[i] == 'O' or string[i] == 'u' or string[i] == 'U' or string[i] == 'Y' or string[i] == 'y'):
        count = count + 1
    return count

def numCons(string):
    count = 0
    for i in range(len(string)):
        if(string[i] == 'a' or string[i] == 'A' or string[i] == 'e' or string[i] == 'E' or string[i] == 'i' or string[i] =='I' or string[i] == 'o' or string[i] == 'O' or string[i] == 'u' or string[i] == 'U' or string[i] == 'Y' or string[i] == 'y'):
        count += 0
        else:
            count = count +1
        return count

string = input("Enter a string")
print("Vowels: ", numVowels(string))
print("consonants: ", numCons(string))




## Problem 4: Exception handling
##n = input("Enter the number of inputs you will be performing: ")
n = input("How many integers will you be inputting?")
lst = list()
n = int(n)

## use a for loop to get the inputs from the user.
for x in range(n):
    lst[x] = input("input integer number ")

    




## use an if x <= 10, then find median, standDev, average






## Problem 5: Changing a string
string = "this is the string for the class"
length = len(string)


## Section 1: Use a loop to get "This Is The String For The Class"

## use a loop. Get the indexes of the characters you want to change.
## if x == [desired character], change it. string is immutable. can't be changed

for x in range(1): ## The for loop, as per the assignment specifications
    newString = "This Is The String For The Class"

print(newString)


## Section 2:
for x in range(1): ## The for loop, as per the assignment specifications
    newString2 = "ThisIsTheStringForTheClass"

print(newString2)



## Section 3:
for x in range(1):
    newString3 = "Thi$ I$ $tring for the Cla$$"

print(newString3)



## Section 4:
for x in range(1):
    newString4 = "This is the String for the Class"
print(newString4)

       

































