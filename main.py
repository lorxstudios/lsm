import os
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

sexit(input("->"))