import sys

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction_check = True
while direction_check:
    direction = str(input("You are at a cross road. Would you like to go left or right? "))
    if direction.upper() in ('L', 'LEFT'):
        direction_check = False
    elif direction.upper() in ('R', 'RIGHT'):
        sys.exit('You got run over. Game Over')
    else:
        print("Please enter Left or Right: ")

action_check = True
while action_check:
    action = str(input("you have come to a lake. There is an island in the middle of the lake. "
                       "Would you like to 'swim' out to the island"
                       " or 'wait' for a boat? "))
    if action.upper() in ('W', 'WAIT'):
        action_check = False
    elif action.upper() in ('S', 'SWIM'):
        sys.exit('You were attacked by an angry trout. Game Over')
    else:
        print("Please enter Swim or Wait: ")

door_check = True
while door_check:
    door = str(input("You arrive at the island unharmed and approach a house with three doors. "
                     "Would you like to enter the Red, Blue or Yellow door? "))
    if door.upper() in ('Y', 'YELLOW'):
        door_check = False
    elif door.upper() in ('B', 'BLUE', 'R', 'RED'):
        sys.exit('Game Over')
    else:
        print("Please enter Red, Blue or Yellow: ")

print('You Found the Treasure!!')
