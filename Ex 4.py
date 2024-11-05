room_description = [
    [ "A" ,  "B" , "C" , "D" , "E" ],
    [ "F" , "G" , "H" , "I" , "J" ], 
    [ "K" , "L" , "M" , "N" , "O" ],
    [ "P" , "Q" , "R" , "S" , "T" ],
    [ "U" , "V" , "W" , "X" , "Y" ]
]

position = (2,2)

while (True):

    x,y = position
    descrition = room_description[y][x]
    print(position, ":", descrition)

    print("what now?")
    command = input()

    if command == "north":
        print("You move north...")
        y == y -1
    elif command == "south":
        print("You move south...")
        y =  y +1
    elif command == "east":
        print("You move east...")
        x = x +1
    elif command == "west":
        print("You move west")
        x = x -1
    elif command == "goodbye":
        break
    else:
        print("I don't understand" + command)

    position = (x,y)