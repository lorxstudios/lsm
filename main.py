import colorama
from colorama import Fore, Back, Style
import requests
import os
from defs import *
def missionmaker():
    clear()
    print("Mission Maker")
    print("-----------------------")
    input("Pulsa enter para crear una misión")
    clear()
    print("Dale un titulo a esta misión:")
    title = input("->")
    clear()
    print("De que trata la misión? ESTE MENSAJE SE VERÁ LITERALMENTE CUANDO EL JUGADOR HAGA ESTA MISIÓN, ESCRIBE COMO SI FUERA UN TITULO.")
    print("Ejemplo: Consigue 20 de autoestima en solo un evento.")
    quest = input("->")
    clear()
    print("Que recompensa dará esto?")
    print("Utiliza objetos o LCoins.")
    rew = input("->")
    clear()
    print("Generando archivo de misión.")
    x = open("data/missions/mission.uwu", "x")
    x.write("{'title': '"+title+"', 'quest': '"+quest+"', 'reward': '"+rew+"'}")
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

xd.close()
print(Back.GREEN + "-> no hay actualizaciones pendientes" +  Style.RESET_ALL)
print("Bienvenido a LSMe.")
print("--------------------------------")
print("Quien eres?")
user = input("Usuario ->")
passw = input("Contraseña ->")
print("Identificando....")
print("PROGRESO ----------------------")
dat = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=1000))
for x in dat:
    lmao = lmao + x
    clear()
    print(lmao)
    time.sleep(0.000000000000001)
users = {"yzde":"uwu", "ikr":"psyraven69", "liam":"lima5evr"}
if user in users:
    if passw == users.get(user):
        print("ACCESO ACEPTADO, BIENVENIDO DE NUEVO, "+ user)
else:
    sexit("Acceso No Reconocido")
print("")
print("LSMe")
cmd = input("->")
if cmd == "storymaker":
    print("storymaker no está disponible.")
elif cmd == "missionmaker":
    print("Abriendo MissionMaker...")

