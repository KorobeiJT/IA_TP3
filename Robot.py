from Env import Env
from Sensors import Sensor
from Effectors import Effector

class Robot:

    ProbaDict={
        'D':0.1,
        'H':1,
        '':0.7,
        'P':0.6,
        'C':0.6,
        'F':0.5
    }
    sensor=Sensor()
    effector=Effector()
    dead=False
    move="haut"

    def __init__(self, level):
        self.lvl=level+2
        self.position=(0,0)
        self.explored=[]
        self.SureEnv=[['_' for i in range(self.lvl)] for j in range(self.lvl)]
        self.UnsureEnv = [['_' for i in range(self.lvl)] for j in range(self.lvl)]


    def display_env(self, env):
        for x in env:
            print(x)
        print()

    
    def Sense(self):
        Map={}
        Map = self.sensor.Capt(self.position)
        for key in Map:
            if Map[key] not in self.SureEnv[key[0]][key[1]] or Map[key]=='':
                self.SureEnv[key[0]][key[1]]=self.SureEnv[key[0]][key[1]].replace("_","") #remove the unknown status
                self.SureEnv[key[0]][key[1]]+=Map[key] #we add the value to the certain assesments
                self.UnsureEnv[key[0]][key[1]]='' #and remove whatever value we had in the unsure assesments
        
        
        
    
    def UpdateDeduction(self):
        for i in range(0, self.lvl):
            for j in range(0, self.lvl):
                for value in cross((i,j),self.lvl).values():
                    if self.SureEnv[i][j] != '_' and self.SureEnv[value[0]][value[1]]=='_':
                        self.UnsureEnv[value[0]][value[1]]=self.UnsureEnv[value[0]][value[1]].replace("_","")
                        if 'P' in self.SureEnv[i][j] and 'D' not in self.UnsureEnv[value[0]][value[1]]: #if we have dirt
                            self.UnsureEnv[value[0]][value[1]]+='D' #we assume there's rubbles close by
                        if 'C' in self.SureEnv[i][j] and 'F' not in self.UnsureEnv[value[0]][value[1]]: #if there's heat
                            self.UnsureEnv[value[0]][value[1]]+='F' #we assume there's fire somewhere around
                        if 'H' in self.SureEnv[i][j] and 'V' not in self.SureEnv and 'V' not in self.UnsureEnv[value[0]][value[1]]: #if we hear screams
                            self.UnsureEnv[value[0]][value[1]]+='V' #we assume there's a victim near
        

    
    def VictimFound(self):
        for i in self.SureEnv:
            if any('V' in j for j in i): #if a victim is registered in our certain assesments then we won
                print("Victime trouvée !")
                return True
        

    def ApplyRules(self):
        max_prob = -1
        decision = ""
        accessiblePos = cross(self.position,self.lvl)
        for key, value in accessiblePos.items(): #for each destination possible
            if key != "centre": #while avoiding the cell we're in
                sum = 0
                if self.SureEnv[value[0]][value[1]] == '': #we apply the probability of the cell
                    sum = self.ProbaDict['']
                else:
                    for i  in self.SureEnv[value[0]][value[1]]: #or do the mean of all the attributes of the cell
                        sum += self.ProbaDict[i]
                    sum /= len(self.SureEnv[value[0]][value[1]])
                
                if value in self.explored: #if we already went through that cell we divide the probability by the number of time we visited that cell (so we don't do back and forth)
                    sum /= (self.explored.count(value)+1)
                
                if sum > max_prob: #we keep the cell with the highest probability
                    max_prob = sum
                    decision = key
        
        self.execute(decision, accessiblePos)
        

    def execute(self,decision, accessiblePos):
        self.explored.append(self.position) # we add the old cell to the explored cells list 
        self.position = accessiblePos[decision] #and we move
        if 'F' in self.SureEnv[self.position[0]][self.position[1]]:

            self.effector.FireExtinguisher(self.position) #we extinguish the fire with our effectors

            self.SureEnv[self.position[0]][self.position[1]]='' #and we update our own assesments
            for var in cross(self.position, self.lvl).values():
                self.SureEnv[var[0]][var[1]]=self.SureEnv[var[0]][var[1]].replace("C","", 1)
                
        print("Le robot va : " + decision )
        
        if 'D' in self.SureEnv[self.position[0]][self.position[1]]: 
            print("Le robot se coince dans les décombres")
            self.dead= True
           
    
    def inference_engine(self):
        if self.dead: return 1
        self.Sense()
        if not self.VictimFound():
            self.UpdateDeduction()
            self.ApplyRules()
        else:
            return 0
        
    
def cross(position, envLen):
    listPos = {}
    listPos["centre"]=((position[0], position[1]))
    if position[0]-1 >= 0 :
        listPos["haut"]=((position[0]-1, position[1]))
    if position[0]+1<envLen:
        listPos["bas"]=((position[0]+1, position[1]))
    if position[1]-1 >= 0 :
        listPos["gauche"]=((position[0], position[1]-1))
    if position[1]+1<envLen:
        listPos["droite"]=((position[0], position[1]+1))

    return listPos
    

