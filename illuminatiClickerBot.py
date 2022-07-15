
import pyautogui
import time
import keyboard

time.sleep(1)
userInput = pyautogui.confirm("Welcome to illuminatiClickerBot, a bot made for ILLUMINATI CLICKER© v1.19 by Nickro_01\nFolow the procedure :"
                "\n1. Visit this link : https://scratch.mit.edu/projects/493520075/"
                "\n2. Put the project in fullscreen"
                "\n3. Launch the project by clicking on the green flag"
                "\n4. Press 'OK' to run the script"
                "\n5. Place your mouse on the illuminati triangle"
                "\nThe bot click automatically. Press 'alt' button to pause/launch the process, press 'space' to stop the process...")

if userInput == "OK":
    #pyautogui
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth/2, screenHeight/2)
    botRunning = True
    botMustClick = True
    while botRunning:
        if botMustClick:
            pyautogui.doubleClick()
            time.sleep(1 / 25)

        try:
            if keyboard.is_pressed('alt'):
                if botMustClick:
                    botMustClick = False
                else:
                    botMustClick = True
                while keyboard.is_pressed('alt'):
                    time.sleep(0)
            if keyboard.is_pressed('space'):
                break
        except:
            break
