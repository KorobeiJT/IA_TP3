
# from BDI import BDI
from Env import Env
from Sensors import Sensor
# from Effectors import Effector
import time

class Robot:

    sensor=Sensor()
    position=(0,0)

    def __init__(self, level):
        self.env=[['' for i in range(level+2)] for j in range(level+2)]


    def display_env(self):
        for x in self.env:
            print(x)
        print()

    
    def Sense(self):
        print("Observing Environment...")
        ListDirt,HasDirt= self.sensor.CaptPoussiere(self.position)
        ListHot,HasHot= self.sensor.CaptChaleur(self.position)
        ListShout,HasShout= self.sensor.CaptHurlement(self.position)

        #updates the env the robot knows and will keep
        if HasDirt : self.env[self.position[0]][self.position[1]]+='P'
        if HasHot : self.env[self.position[0]][self.position[1]]+='C'
        if HasShout : self.env[self.position[0]][self.position[1]]+='H'

        #updates the temporary env with all the adjacent rooms
        for var in ListDirt: self.env[var[0]][var[1]]+='P'
        for var in ListHot: self.env[var[0]][var[1]]+='C'
        for var in ListShout: self.env[var[0]][var[1]]+='H'

        self.display_env()
        print("Position now = ",self.position)
    

    
    def VictimFound(self):
        # if 'V' in self.env[self.position[0]][self.position[1]]:
        #     return 0
        
        #if robot position and at least two adjacents cells contains shouts
        if 'H' in self.env[self.position[0]][self.position[1]] and sum('H' in self.env[x[0]][x[1]] for x in cross(self.position)) >= 2:
            return 0


    
    def execute(self):
        if self.plan_action != []:
            print("Executing action plan...")
            envi=Env.instance()
            for i in self.plan_action:
                self.roomsVisited+=1
                
            self.position=self.destination

    
    def inference_engine(self):
        print("START ANALYSIS CYCLE")
        self.Sense()
        if not self.VictimFound():
            # self.UpdateWorkMemory()
            # self.ApplyRules()
            print("CYCLE FINISHED")
            print()
            time.sleep(3)
        else:
            return 0
        
    
def cross(position):
    listPos=[(position[0],position[1]),(position[0]+1,position[1]),(position[0],position[1]+1),(position[0]-1,position[1]),(position[0],position[1]-1)]
    return listPos
    

