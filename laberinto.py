# constantes
import os
import random

import readchar

POS_X = 0
POS_Y = 1
map_width = 20
map_height = 15
num_of_map_objects = 15

# x = width
# y = height

my_position = [6, 3]
tail_lenght = 0
tail = []
map_objects = []

end_game = False
died = False

# Main Loop
while not end_game:
    # Generate random objects on the map

    while len(map_objects) < num_of_map_objects:
        new_position = [random.randint(0, map_width), random.randint(0, map_height)]

        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    # Draw map
    print("+" + "-" * map_width * 3 + "+")

    for coordinate_y in range(map_height):
        print("|", end="")

        for coordinate_x in range(map_width):

            char_to_draw = " "
            object_in_cell = None
            tai_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"
                    object_in_cell = map_object

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "#"
                    tai_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1

                if tai_in_cell:
                    end_game = True
                    died = True

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * map_width * 3 + "+")
    print("la cola {}".format(tail_lenght))

    # Ask user where he wants to move
    # direction = input("Donde te quieres mover? [WASD]: ")
    direction = readchar.readchar().decode()

    if direction == "w":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] -= 1
        my_position[POS_Y] %= map_height

    elif direction == "s":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] += 1
        my_position[POS_Y] %= map_height

    elif direction == "a":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] -= 1
        my_position[POS_X] %= map_width

    elif direction == "d":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] += 1
        my_position[POS_X] %= map_width

    elif direction == "q":
        end_game = True

    os.system("cls")

if died:
    print("""         _____                    _____                    _____                            _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                          /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\____\                /::\    \                        /::\    \                /::\    \                /::\____\                /::\    \        
       /::::\    \              /::::|   |               /::::\    \                      /::::\    \              /::::\    \              /::::|   |               /::::\    \       
      /::::::\    \            /:::::|   |              /::::::\    \                    /::::::\    \            /::::::\    \            /:::::|   |              /::::::\    \      
     /:::/\:::\    \          /::::::|   |             /:::/\:::\    \                  /:::/\:::\    \          /:::/\:::\    \          /::::::|   |             /:::/\:::\    \     
    /:::/__\:::\    \        /:::/|::|   |            /:::/  \:::\    \                /:::/  \:::\    \        /:::/__\:::\    \        /:::/|::|   |            /:::/__\:::\    \    
   /::::\   \:::\    \      /:::/ |::|   |           /:::/    \:::\    \              /:::/    \:::\    \      /::::\   \:::\    \      /:::/ |::|   |           /::::\   \:::\    \   
  /::::::\   \:::\    \    /:::/  |::|   | _____    /:::/    / \:::\    \            /:::/    / \:::\    \    /::::::\   \:::\    \    /:::/  |::|___|______    /::::::\   \:::\    \  
 /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \  /:::/    /   \:::\ ___\          /:::/    /   \:::\ ___\  /:::/\:::\   \:::\    \  /:::/   |::::::::\    \  /:::/\:::\   \:::\    \ 
/:::/__\:::\   \:::\____\/:: /    |::|   /::\____\/:::/____/     \:::|    |        /:::/____/  ___\:::|    |/:::/  \:::\   \:::\____\/:::/    |:::::::::\____\/:::/__\:::\   \:::\____
\:::\   \:::\   \::/    /\::/    /|::|  /:::/    /\:::\    \     /:::|____|        \:::\    \ /\  /:::|____|\::/    \:::\  /:::/    /\::/    / ~~~~~/:::/    /\:::\   \:::\   \::/    /
 \:::\   \:::\   \/____/  \/____/ |::| /:::/    /  \:::\    \   /:::/    /          \:::\    /::\ \::/    /  \/____/ \:::\/:::/    /  \/____/      /:::/    /  \:::\   \:::\   \/____/ 
  \:::\   \:::\    \              |::|/:::/    /    \:::\    \ /:::/    /            \:::\   \:::\ \/____/            \::::::/    /               /:::/    /    \:::\   \:::\    \     
   \:::\   \:::\____\             |::::::/    /      \:::\    /:::/    /              \:::\   \:::\____\               \::::/    /               /:::/    /      \:::\   \:::\____\    
    \:::\   \::/    /             |:::::/    /        \:::\  /:::/    /                \:::\  /:::/    /               /:::/    /               /:::/    /        \:::\   \::/    /    
     \:::\   \/____/              |::::/    /          \:::\/:::/    /                  \:::\/:::/    /               /:::/    /               /:::/    /          \:::\   \/____/     
      \:::\    \                  /:::/    /            \::::::/    /                    \::::::/    /               /:::/    /               /:::/    /            \:::\    \         
       \:::\____\                /:::/    /              \::::/    /                      \::::/    /               /:::/    /               /:::/    /              \:::\____\        
        \::/    /                \::/    /                \::/____/                        \::/____/                \::/    /                \::/    /                \::/    /        
         \/____/                  \/____/                  ~~                                                        \/____/                  \/____/                  \/____/         
                                                                                                                                                                                 """)

    print("Has muertooo!")
