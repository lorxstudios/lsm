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
    xd.close()
    print("hay una actualización más reciente.")
    print("--------------------")
    print("1. Instalar Actualizador")
    print("2. Actualizar Manualmente (limpieza)")
    print("--------------------")
    resp = input("->")
    if resp == "1":
        print("Instalando Actualizador, esto puede tardar unos segundos.")
        version = urlme("https://raw.githubusercontent.com/lorxstudios/lsm/main/version")
        if exists("updaterfor" + version + ".py"):
            os.remove("updaterfor" + version + ".py")
        upd = open("updaterfor" + version + ".py", "x")
        upd.write("https://raw.githubusercontent.com/lorxstudios/lsm/main/updater.py")
        upd.close()
        print("Cerrando LSMe")
        os.system("python3 "+"updaterfor" + version + ".py")
    elif resp == "2":
        print("Actualización Manual seleccionada, haciendo limpieza de archivos")
        sexit("Actualización Manual seleccionada.")

    else:
        print("Lo siento, no he reconocido lo que has dicho.")
        sexit("Por medidas de seguridad, el programa ha salido. Vuelve a entrar de nuevo si crees que ha sido un error.")
else:
    xd.close()
    print(Back.GREEN + "-> no hay actualizaciones pendientes" +  Style.RESET_ALL)
    