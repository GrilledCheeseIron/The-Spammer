import time
import keyboard
import pyautogui

print("  ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ ")
print(" / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|")
print(" \__ \ |_) | (_| | | | | | | | | | | |  __/ |   ")
print(" |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   ")
print("     | |                                        ")
print("     |_|                                        ")
print("")
print("Made by GrilledCheeseIron")
print("https://github.com/GrilledCheeseIron")




print("")
print("")
print("dont type the full option only type the number")
print("options: ")
print("1) info/about")
print("2) tutorial/how to use")
print("3) whatsapp/instagram")
print("4) tiktok")


optionsrun = input("on what social media app would you want to run a script or what would you like to see?: ")

if optionsrun == "1":
    print ("info:")
    print("")
    print("I made this project for fun and because i like spam bots just i dont want to have 30 difrent projects for the 30 difrent functions.")
    print("so i made this project the spammer")
    print("you can alse see it as a collection of spambots/spammers.")
    print("ignore the error that comes after this description the script works and i dont know how to get rid of it")
    print("note: the tiktok and youtube script only works with 1920 x 1080 displa in landscape mode")

if optionsrun == "2":
    print("")
    print("if you want to stop the programm simply wait for the programm to stop spamming or close the terminal")
    print("if you are going to us the whatsapp/instagram spambot")
    print("1, go to whatsapp on you're browser")
    print("2, run the script")
    print("3, go to whatsapp and wait for the script to start")
    print("")
    print("if you ar using the tiktok spambot do this")
    print("1, go to tiktok and click on a video so the screen goes into full screen")
    print("run the script and go to the tiktok page and wait for the script to start")
    print("if the script doesnt run after 20 seconds and there is an error please repot it and i wil try to fix it")
    print("note: this script currentle only works on ")

if optionsrun == "3":
    print ("scripts for whatsapp or instagram:")
    print("1, rickroll spam script (spams the lyrics of never gonna give you up) ")
    print("2, normal spam (spams a custom amount of messages and a custom message)")
    print("3, the entire bee movie script")
    print("4, the entire shrek script")
    optionsrunwhatsapp = input("what script would you like to run? ")

    if optionsrunwhatsapp == "1":
        print("go to whatsapp or instagram and wait 10 seconds")
        time.sleep(10)
        f= open("rickroll.txt", 'r')
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")


    if optionsrunwhatsapp == "2":
        wm = input("what will you're message be?: ")
        wmc = input("how much messages will you're victim receive?: ")
        print("go to whatsapp or instagram and wait 10 seconds")
        time.sleep(10)
        wmc = int(wmc)

        for i  in range (wmc):
            pyautogui.typewrite(wm)
            pyautogui.press("enter")
            i = i+1
            wmc = int(wmc)

    if optionsrunwhatsapp == "3":
        print("go to whatsapp or instagram and wait 10 seconds")
        time.sleep(10)
        f= open("beemoviescript.txt", 'r')
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")

    if optionsrunwhatsapp == "4":
        print("go to whatsapp or instagram and wait 10 seconds")
        time.sleep(10)
        f= open("shrek script.txt", 'r')
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")

if optionsrun == "4":
    print("options:")
    print("1, tiktok comment bot(goes down all videos one by one and comment a custom comment on it)")
    tikotkchoice = input("wich one do you want?: ")
    if tikotkchoice == "1":
        tiktokmessage = input("what will you're custom message be?: ")
        tiktokamount = input("how many videos wil the bot comment on?: ")
        tiktokamount = int(tiktokamount)

        print("go to tikotk click on a video and whait for the bot to start you have 15 seconds")
        time.sleep(15)
    for i in range(tiktokamount):
        pyautogui.moveTo(1184, 575)
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.moveTo(1489, 977)
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.typewrite(tiktokmessage)
        pyautogui.moveTo(1826, 979)
        pyautogui.leftClick()
        time.sleep(1)
        i = i+1
