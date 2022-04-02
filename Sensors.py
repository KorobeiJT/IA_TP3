from Env import Env

class Sensor:

    @classmethod
    def CaptPoussiere(self, position):
        f= Env.instance()
        PoussiereAround=[]
        origin = False
        if 'P' in f.env[position[0]][position[1]]:
            origin=True
        for var in cross(position,len(f.env)):
            if 'P' in f.env[var[0]][var[1]] :
                PoussiereAround.append(var)
        return PoussiereAround, origin

    @classmethod
    def CaptChaleur(self, position):
        f= Env.instance()
        ChaleurAround=[]
        origin = False
        if 'C' in f.env[position[0]][position[1]]:
            origin=True
        for var in cross(position, len(f.env)):
            if 'C' in f.env[var[0]][var[1]]:
                ChaleurAround.append(var)
        return ChaleurAround, origin

    @classmethod
    def CaptHurlement(self, position):
        f= Env.instance()
        HurlementAround=[]
        origin = False
        if 'H' in f.env[position[0]][position[1]]:
            origin=True
        for var in cross(position, len(f.env)):
            if 'H' in f.env[var[0]][var[1]]:
                HurlementAround.append(var)
        return HurlementAround, origin


def cross(position, envLen):
    listPos = []
    if position[0]-1 >= 0 :
        listPos.append((position[0]-1, position[1]))
    if position[0]+1<envLen:
        listPos.append((position[0]+1, position[1]))
    if position[1]-1 >= 0 :
        listPos.append((position[0], position[1]-1))
    if position[1]+1<envLen:
        listPos.append((position[0], position[1]+1))

    return listPos
