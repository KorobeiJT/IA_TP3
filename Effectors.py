from Env import Env

class Effector:
    
    @classmethod
    def FireExtinguisher(self, position):
        f= Env.instance()
        f.env[position[0]][position[1]]=''
        for var in cross(position, len(f.env)):
            f.env[var[0]][var[1]]=f.env[var[0]][var[1]].replace("C","", 1)
        print("Le robot éteint le feu")


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