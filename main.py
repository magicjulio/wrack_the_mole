import pyautogui
from pynput import keyboard
import time

banner = """
     ____.     .__  .__              
    |    |__ __|  | |__|__ __  ______
    |    |  |  \  | |  |  |  \/  ___/
/\__|    |  |  /  |_|  |  |  /\___ \ 
\________|____/|____/__|____//____  >
                                  \/ 
Farmers Against Potatoes Idle heck by Julio
"""

print(banner)

f5_pressed = False

def on_keydown():
    x = 0
    print("[+] started")

    while True:

        pos = pyautogui.locateOnScreen("yellow.png", confidence=0.7)
        if pos:
            x += 1
            pyautogui.click(pos)

        else:
            global f5_pressed
            if f5_pressed:
                f5_pressed = False
                print(f"[-] stopped with {x} smashes")
                break




def on_press(key):
    global f5_pressed
    if key == keyboard.Key.f5:
        f5_pressed = True

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    if f5_pressed:
        f5_pressed = False
        on_keydown()
    time.sleep(0.1)
