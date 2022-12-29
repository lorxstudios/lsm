import colorama
from colorama import Fore, Back, Style
import requests
import os
from defs import *
print("LSMe")
print("Lorx Story Maker en español")
print("------------------------------------------------")
print("")
print("")
print("")
print("")
print("-> Buscando Actualizaciones.")
xd = open("main.py", "r")
if urlme("https://raw.githubusercontent.com/lorxstudios/lsm/main/main.py") != xd.read():
    print(xd)
    print(urlme("https://raw.githubusercontent.com/lorxstudios/lsm/main/main.py"))
    xd.close()
    print("No es lo mismo")
else:
    xd.close()
    print(Back.GREEN + "-> no hay actualizaciones pendientes" +  Style.RESET_ALL)
#sexit(input("->"))