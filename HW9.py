#Name:Cody
#Class: 6th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
A = {"Name" : "Sprout",
     "Role" : "Healer",
     "Stats" : [2,4,5,3,2]}
#3. Print the keys of the dictionary from #2.
print(A.keys())
#4. Print the values of the dictionary from #2
print(A.values())
#5. Print one of the three numbers from the list by itself
print(A["Stats"][0])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
A.update ({ "Hearts" : [2]})

#7. Print the entire dictionary from #2 with the updated key and value.
print(A.keys())
print(A.values())
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
Bdictionary = {
    "student_1" : {
        "Y/N" : "Jacob",
        "Age" : 14,
        "Chudness" : True,
    },
    "student_2" : {
        "Y/N" : "Misa",
        "Age" : 15,
        "Chudness" : False ,
    },
    "student_3" : {
        "Y/N" : "Jerrell",
        "Age" : 15,
        "Chudness" : True,
    }
}

#9. Print the names of all three classmates on the same line.
print(Bdictionary["student_1"]["Y/N"], Bdictionary["student_2"]["Y/N"], Bdictionary["student_3"]["Y/N"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
Bdictionary.pop("student_1")
print(Bdictionary)