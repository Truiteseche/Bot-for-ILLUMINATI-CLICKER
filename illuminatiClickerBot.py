
import pyautogui
import time

time.sleep(1)
userInput = pyautogui.confirm("This is a bot for ILLUMINATI CLICKER© v1.19 by Nickro01 :"
                "\n1. Follow this link : https://scratch.mit.edu/projects/493520075/"
                "\n2. Put the project in fullscreen"
                "\n3. Launch the project by clicking on the green flag"
                "\n4. Press 'OK' to run the script")

if userInput == "OK":
    #pyautogui
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.moveTo(screenWidth/2, screenHeight/2)
    botRunning = True
    pyautogui.position(screenWidth/2, screenHeight/2)