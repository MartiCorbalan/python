# constantes
import os
import random

import readchar

POS_X = 0
POS_Y = 1

num_of_map_objects = 4

obstacle_definition = """\
#############################
                        #####
##################       ####
####    ##########          #
#######                  ####
#####     ######    #########
#########               #####
############       ##########
###   ##########         ####
###  ##    ######       #####
###                     #####
#######    ######       #####
#############################\
"""

# x = width
# y = height

my_position = [0, 1]

map_objects = []

end_game = False
died = False

# Create obstacle map

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
map_width = len(obstacle_definition[0])
map_height = len(obstacle_definition)


# Main Loop
while not end_game:

    os.system("cls")
    # Generate random objects on the map

    while len(map_objects) < num_of_map_objects:
        new_position = [random.randint(0, map_width - 1), random.randint(0, map_height - 1)]

        if new_position not in map_objects and new_position != my_position and \
                obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            map_objects.append(new_position)

    # Draw map
    print("+" + "-" * map_width * 2 + "+")

    for coordinate_y in range(map_height):
        print("|", end="")

        for coordinate_x in range(map_width):

            char_to_draw = "  "
            object_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * map_width * 2 + "+")


    # Ask user where he wants to move
    # direction = input("Donde te quieres mover? [WASD]: ")
    direction = readchar.readchar().decode()
    new_position = None
    if direction == "w":
        new_position = [my_position[POS_X],  (my_position[POS_Y] - 1) % map_width]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % map_width]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % map_width, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % map_width, my_position[POS_Y]]

    elif direction == "q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    os.system("cls")



