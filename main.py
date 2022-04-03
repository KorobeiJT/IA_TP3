
import threading
from Robot import Robot
from Env import Env

environment=Env.instance()
level = 1

def main(level):
    print()
    print("Niveau "+ str(level) + " : maison " + str(level + 2) + "x" + str(level+2))
    environment.init(level)
    robot=Robot(level)
    while 1:
        
        a = robot.inference_engine()
        if a == 0:
            nextlvl=True
            break
        elif a == 1:
            nextlvl=False
            break
    
    if nextlvl:
        print()
        t = input("Cliquez sur entrée pour passer au niveau suivant : ")
        level+=1
        main(level)
    else : print("Fin du jeu")

print("F = Feu ; D = Décombres ; P = Poussière ; C = Chaleur ;")
print("V = Victime ; R = Robot ; H = Hurlements")
main(level)

