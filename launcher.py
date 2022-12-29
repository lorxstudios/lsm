from defs import *
import os
if os.path.exists("exit.uwu"):
    os.remove("exit.uwu")
secure_endings = ["user-exit"]
advise = ["error"]
print("launching lsm")
os.system("python3 main.py")
if not os.path.exists("exit.uwu"):
    input("An unrecognised exit ocurred, returned to launcher")
else:
    xd = open("exit.uwu", "r")
    dat = xd.read()
    xd.close()
    if dat in secure_endings:
        
        if os.path.exists("exit.uwu"):
            os.remove("exit.uwu")

        exit()
    elif dat in advise:
        clear()
        print("Welcome back to LRXLauncher.")
        print("")
        print("")
        print("")
        print("--------------------------------------------")
        print("The program was exited with the next reason:")
        print("")
        print(dat)
        print("")
        input(Back.CYAN + "Press enter to exit from launcher" + Style.RESET_ALL)
        if os.path.exists("exit.uwu"):
            os.remove("exit.uwu")
        exit()
    else:
        clear()

        print("")
        print("")
        print("")
        print("Welcome back to LRXLauncher.")
        print("--------------------------------------------")
        print("An non-known reason was given to launcher when exiting, the next reason was inputted:")
        print("")
        print(dat)
        print("")
        print("The next message was sent by LRXLauncher:")
        print(Back.MAGENTA + "We believe that this is an error, if this happens too often, please, try updating the program from our GitHub, lorxstudios." + Style.RESET_ALL)
        input(Back.RED + "Press enter to exit from launcher" + Style.RESET_ALL)
        if os.path.exists("exit.uwu"):
            os.remove("exit.uwu")
        exit()
print("An error ocurred with launcher and it's far from being ok.")
print("Please update manually.")