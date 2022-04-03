
# from BDI import BDI
from Env import Env
from Sensors import Sensor
# from Effectors import Effector
import time

class Robot:

    ProbaDict={
        'D':0,
        'H':1,
        '':0.9,
        'P':0.6,
        'C':0.6,
        'F':0.5
    }
    sensor=Sensor()
    position=(0,0)
    move="haut"
    def __init__(self, level):
        self.lvl=level+2
        self.SureEnv=[['_' for i in range(self.lvl)] for j in range(self.lvl)]
        self.UnsureEnv = [['_' for i in range(self.lvl)] for j in range(self.lvl)]


    def display_env(self, env):
        for x in env:
            print(x)
        print()

    
    def Sense(self):
        Map={}
        print("Observing Environment...")
        Map = self.sensor.Capt(self.position)
        for key in Map:
            if Map[key] not in self.SureEnv[key[0]][key[1]] or Map[key]=='':
                self.SureEnv[key[0]][key[1]]=self.SureEnv[key[0]][key[1]].replace("_","") #remove the unknown status
                self.SureEnv[key[0]][key[1]]+=Map[key] #we add the value to the certain assesments
                self.UnsureEnv[key[0]][key[1]]='' #and remove whatever value we had in the unsure assesments
        self.display_env(self.SureEnv)
        self.Deduct()
        print("Position now = ",self.position)
    
    def Deduct(self):
        for i in range(0, self.lvl):
            for j in range(0, self.lvl):
                for value in cross((i,j),self.lvl).values():
                    if self.SureEnv[i][j] != '_' and self.SureEnv[value[0]][value[1]]=='_':
                        if 'P' in self.SureEnv[i][j]:
                            self.UnsureEnv[value[0]][value[1]]='D'
                        if 'C' in self.SureEnv[i][j]:
                            self.UnsureEnv[value[0]][value[1]]='F'
                        if 'H' in self.SureEnv[i][j] and 'V' not in self.SureEnv:
                               self.UnsureEnv[value[0]][value[1]]='V'
        self.display_env(self.UnsureEnv)

    
    def VictimFound(self):
        if 'V' in self.SureEnv:
            print("Victim Found!")
            return 0
        
        #if robot position and at least two adjacents cells contains shouts
        #if 'H' in self.SureEnv[self.position[0]][self.position[1]] and sum('H' in self.SureEnv[x[0]][x[1]] for x in cross(self.position,self.lvl)) >= 2:
         #   return 0


    
    def execute(self):
        for key, value in cross(self.position,self.lvl).items(): #for each destination possible
            return "TO DO"
    
    def inference_engine(self):
        print("START ANALYSIS CYCLE")
        self.Sense()
        if not self.VictimFound():
            # self.UpdateWorkMemory()
            # self.ApplyRules()
            print("CYCLE FINISHED")
            print()
        else:
            return 0
        
    
def cross(position, envLen):
    listPos = {}
    listPos["centre"]=((position[0], position[1]))
    if position[0]-1 >= 0 :
        listPos["gauche"]=((position[0]-1, position[1]))
    if position[0]+1<envLen:
        listPos["droite"]=((position[0]+1, position[1]))
    if position[1]-1 >= 0 :
        listPos["bas"]=((position[0], position[1]-1))
    if position[1]+1<envLen:
        listPos["haut"]=((position[0], position[1]+1))

    return listPos
    

