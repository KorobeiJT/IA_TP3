
import threading
from Robot import Robot
from Env import Env

environment=Env.instance()
level = 1

def main():
    global level
    environment.init(level)
    robot=Robot(level)
    robot.inference_engine()
    #while 1:
        ##if robot.inference_engine() == 0:
            ##break
    t = print("Cliquer sur entrée pour passer au niveau suivant : ")
    level+=1
    # main()

main()

