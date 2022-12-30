import colorama
from colorama import Fore, Back, Style
import requests
import os
from os import name,system
import string
import random
import time
def sexit(x=""):
    if os.path.exists("exit.uwu"):
        os.remove("exit.uwu")
    f = open("exit.uwu", "x")
    #print("Safe-Exiting")
    if x == "":
        #print("No reason.")
        f.write("No reason.")
    else:
        #print("Reason: "+x)
        f.write(x)
    f.close()
    exit()
def urlme(x):
    #URLpred = "https://raw.githubusercontent.com/lorxstudios/lsm/main/main.py"
    URL = x
    response = requests.get(URL)
    data = response.text
    return(data)
def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def exists(x):
    if os.path.exists(x):
        return(True)
    else:
        return(False)