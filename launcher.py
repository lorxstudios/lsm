from defs import *
import os
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
        exit()
    elif dat in advise:
        print("The program was exited with the next reason:")
        print(dat)
        input("Press enter to exit from launcher")
        exit()
    else:
        print("An non-known reason was given to launcher when exiting, the next reason was inputted:")
        print(dat)
        input("Press enter to exit from launcher")
        exit()
print("An error ocurred with launcher and it's far from being ok.")
print("Please update manually.")