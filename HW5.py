#Name:
#Class: 6th Hour
#Assignment: HW5
from code import interact

#1. Print Hello World!
print ("Hello World")
#1. Create a list with 5 strings containing 5 different names in it.
List = ["Obama", "Cuphead", "Bendy", "Dandicus", "Coach Mack"]
#2. Append a new name onto the Name List.
List.append ("Watch")
#3. Print out the 4th name on the list.
print(List[3])
#4. Create a list with 4 different integers in it.
Number_list = [3, 78, 195327, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000]
#5. Insert a new integer into the 2nd spot and print the new list.
Number_list.insert (1, 2784876457754)
print(Number_list)
#6. Sort the list from lowest to highest and print the sorted list.
Number_list.sort()
print (Number_list)
#7. Add the 1st three numbers on the sorted list together and print the sum.
Var_Number_list = Number_list[0]+Number_list[1]+Number_list[2]
print(Var_Number_list)
#8. Create a list with two strings, two integers, and two boolean values.
Obama_list= ["Cups", "Mugs", 25, 72, True, False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(Obama_list[int(input("enter index value"))])