
import threading
from Robot import Robot
from Env import Env

robot=Robot()
environment=Env.instance()

def env_thread():
    environment.spawn()

def robot_thread():
    while 1:
        robot.analysis_cycle()



env=threading.Thread(target=env_thread)
rob=threading.Thread(target=robot_thread)
env.start()
rob.start()
