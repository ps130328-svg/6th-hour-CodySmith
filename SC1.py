#Name: Cody
#Class: 6th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

Enemy =  {
    "Enemy_1" : {
        "Name" : "Crypid",
        "Hit points" : 5,
        "Speed" : 5.0,
        "Hostile" : True,
    },

    "Enemy_2" : {
        "Name" : "Hider",
        "Hit points" : 3,
        "Speed" : 6.5,
        "Hostile" : False,
    },
"Enemy_3" : {
        "Name" : "Stalker",
        "Hit points" : 6,
        "Speed" : 4.5,
        "Hostile" : True,
    },
"Enemy_4" : {
        "Name" : "SkinStealer",
        "Hit points" : 10,
        "Speed" : 0.75,
        "Hostile" : True,
    },
"Enemy_5" : {
        "Name" : "Hugger",
        "Hit points" : 1,
        "Speed" : 7.5,
        "Hostile" : False,
    }}

print(Enemy)

Enemy["Enemy_4"].update({"Hit points" : 8})

Enemy["Enemy_1"].update({"Hit points" : 4})

Enemy["Enemy_5"].update({"Hit points" : 0})


print(Enemy)


