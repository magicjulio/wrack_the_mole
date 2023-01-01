import pyautogui
import time






# ==================== testing zone ======================


# ===================  end of testing zone ===============


# banner
banner = """
     ____.     .__  .__              
    |    |__ __|  | |__|__ __  ______
    |    |  |  \  | |  |  |  \/  ___/
/\__|    |  |  /  |_|  |  |  /\___ \ 
\________|____/|____/__|____//____  >
                                  \/ 
Farmers Against Potatoes Idle heck by Julio
  * Night Bot Edition *
"""
print(banner)


# switch tab
def switch():
    pyautogui.hotkey("alt", "tab")

# get position
def pos():
    while True:
        time.sleep(0.1)
        print(pyautogui.position())

# sleep for i seconds and get position of mouse than
def timeout(lenght=3):
    for i in range(lenght, 0, -1):
        print(i)
        time.sleep(1)
    print(0)


print("----------setup------------")

# screen size
print("[*] Getting Screen size")
screen_width, screen_height = pyautogui.size()
print(f"[+] Found width:{screen_width} height:{screen_height}")

# setup field of potatos
print("[!] Configure field")

# locate corners
def locate_corners():
    timeout(2)
    switch()
    timeout(3)
    xy = pyautogui.position()
    switch()
    return xy
while True and False:
    print("[!] Please move to TOP LEFT of game field")
    top_left = locate_corners()

    print("[!] Please move to TOP RIGHT of game field")
    top_right = locate_corners()

    print("[!] Please move to BOTTOM LEFT of game field")
    bottom_left = locate_corners()

    print("[!] Please move to BOTTOM RIGHT of game field")
    bottom_right = locate_corners()

    if input("Is this okay? [y/n]: ") != "n":
        break


Point(x, y)

# calculate region
region = (330, 200, 670, 650)
# ready_button_region = (300, 60, 1250, 200)




print("[*] Locating start button")
# locate start button on the bottom of screen
while True:
    timeout()
    switch()
    time.sleep(0.5)
    start_button = pyautogui.locateOnScreen("start.png", confidence=0.6)
    if start_button is None:
        print("[-] Didn't found start button try again")
    else:
        switch()
        print("[+] Got start button position")
        break



print("[+] All ready!!! You can leave the PC now")
print("[!] Go sure nothing interferes with the process else the loop might break")
time.sleep(5)
switch()
def main():
    global start_button
    global region

    while True:
        time.sleep(10)



        if pyautogui.locateOnScreen("ready.png", confidence=0.5):
            pyautogui.click(start_button)

            empty_pos = 100


            while True:

                position_potato = pyautogui.locateOnScreen("yellow.png", confidence=0.7) # , region=region)

                if position_potato:
                    empty_pos = 100
                    pyautogui.click(position_potato)
                else:

                    empty_pos -= 1
                    if empty_pos == 0:
                        switch()
                        print("5 minute pause")
                        time.sleep(3)
                        switch()
                        break

if __name__ == '__main__':
    main()
