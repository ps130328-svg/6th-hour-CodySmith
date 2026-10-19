#Name: Cody
#Class: 6th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
List = [ random.randint(1,100), random.randint(1,100), random.randint(1,100) ]
#3. Print the list.
print(List)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if List[0] > List[1] and List[0] > List[2]:
    print(List[0],"is the biggest number")
    num = List[0]
elif List[1] > List[2] and List[1] > List[0]:
    print(List[1],"is the biggest number")
    num = List[1]
elif List[2] > List[1] and List[2] > List[1]:
    print(List[2],"is the biggest number")
    num = List[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".
#Done

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

if num >= 10:
    if num >= 20:
        print(f"{num} is greater than 20!")
    else:
        print(f"{num} is greater than 10 but less than 20!")
elif num < 10:
    if num >= 5:
        print(f"{num} is greater than 5 but less than 10!")
    else:
        print(f"{num} is less than 5!")