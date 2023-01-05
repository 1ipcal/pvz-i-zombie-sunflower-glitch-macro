# Name: Calvin Ip
# Date: 6/22/2022
# Version 1.0
# Description: A Macro that performs a Sunflower Bungee Zombie glitch in the
#              PvZ minigame: I, Zombie

import mouse
import time


def get_mouse_pos():
    # returns a tuple of the mouse position
    input("Press any key to start a 2 second delay to find mouse position\n")

    time.sleep(2)
    mouse_pos = mouse.get_position()

    print(mouse_pos)

    return mouse_pos


if __name__ == '__main__':
    print("PvZ I, Zombie Bungee Glitch Macro Ver. 1.0")
    print("By: Calvin Ip")
    print("This program will store mouse locations "
          "and perform the bungee zombie sunflower glitch\n")

    # Getting First Mouse Position (Seed Slot)
    print("Seed slot")
    pos1 = get_mouse_pos()

    # Getting Second Mouse Position (Sunflower Location)
    print("Sunflower location")
    pos2 = get_mouse_pos()

    while True:
        user_input = input("Enter y to perform macro. "
                           "Enter x to stop program\n")

        if user_input.lower() == 'y':
            print('Activating in 2 seconds')
            time.sleep(2)

            # Repeat 6 times
            for i in range(6):
                # Select bungee
                mouse.move(pos1[0], pos1[1], absolute=True, duration=0)
                mouse.click('left')
                time.sleep(0.01)

                # Click on sunflower
                mouse.move(pos2[0], pos2[1], absolute=True, duration=0)
                mouse.click('left')
                time.sleep(0.01)

            print("\n")

        elif user_input.lower() == 'x':
            print("program stopping...")
            time.sleep(1)
            break

        print("New Sunflower Location?")
        pos2 = get_mouse_pos()
        print("\n")
