#Name:
#Class: 5th Hour
#Assignment: HW6

print("Hello World")
print("Hello World")
print("Hello World")

#1. Create a list with 9 different numbers inside.
Yummers = [1,2, 3, 4, 5, 6, 7, 8, 9]
#2. Sort the list from highest to lowest.
Yummers.sort(reverse=True)
#3. Create an empty list.
Cup_list = []
#4. Remove the median number from the first list and add it to the second list.
Var_1= Yummers.pop(4)
Cup_list.append(Var_1)
#5. Remove the first number from the first list and add it to the second list.
Var_2= Yummers.pop(0)
Cup_list.append(Var_2)
#6. Print both lists.
print(Yummers)
print(Cup_list)
#7. Add the two numbers in the second list together and print the result.
Var_3= Cup_list [0] + Cup_list [1]
print(Var_3)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
Yummers.append (Var_3)
#9. Sort the first list from lowest to highest and print it.
Yummers.sort()
print(Yummers)