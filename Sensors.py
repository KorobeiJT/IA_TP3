from Env import Env

class Sensor:

    @classmethod
    def Capt(self, position):
        f= Env.instance()
        MapCapt={}
        for var in cross(position,len(f.env)):
            MapCapt[var]=f.env[var[0]][var[1]].replace("R","")
        return MapCapt

def cross(position, envLen):
    listPos = []
    listPos.append((position[0], position[1]))
    if position[0]-1 >= 0 :
        listPos.append((position[0]-1, position[1]))
    if position[0]+1<envLen:
        listPos.append((position[0]+1, position[1]))
    if position[1]-1 >= 0 :
        listPos.append((position[0], position[1]-1))
    if position[1]+1<envLen:
        listPos.append((position[0], position[1]+1))
    return listPos
