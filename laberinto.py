#constantes
import os

import readchar

POS_X = 0
POS_Y = 1
map_width = 20
map_height = 15

my_position = [3, 1]

while True:
    # Draw map
    print("+" + "-" * map_width * 3 + "+")

    for coordinate_y in range(map_height):
        print("|", end="")
        for coordinate_x in range(map_width):

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")

    print("+" + "-" * map_width * 3 + "+")

    # Ask user where he wants to move
    #direction = input("Donde te quieres mover? [WASD]: ")
    direction = readchar.readchar().decode()

    if direction == "w":
        my_position[POS_Y] -= 1
    elif direction == "s":
        my_position[POS_Y] += 1
    elif direction == "a":
        my_position[POS_X] -= 1
    elif direction == "d":
        my_position[POS_X] += 1
    elif direction == "q":
        break

    os.system("cls")


