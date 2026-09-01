#Name:
#Class: 6th Hour
#Assignment: HW4

#1. Print "Hello World!"
print ("Hello world")
#2. import the 'math' library
import math
#3. Create two variables, x and y, that asks the user for a decimal (float) for x and an integer for y.
x=float(input("Give me a number"))
y=int(input("Give me a number"))
#4. Create a variable with the value that is x and y added together.
var1 = x + y
#5. Print the variable from #4.
print (var1)
#6. Create a variable with the value that is x and y added together, then divide the sum by 3.
var2 = var1/3
#7. Print the variable from #6.
print (var2)
#8. Create a variable with the value of the square root of y, then print the result.
var3 = (math.sqrt(y))
print (var3)
#9. Use the round function to round x to the nearest tenths place (EX: 1.17 rounds to 1.1). Print the result.
var4 = (round(x,1))
print (var4)
#10. Use the ceiling function to round x up to the nearest whole number. Print the result.
print(math.ceil(x))

#11. Use the floor function to round x down to the nearest whole number. Print the result.
print(math.floor(x))
