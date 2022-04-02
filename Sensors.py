from Env import Env

class Sensor:
    
    @classmethod
    def Sense(self):
        f= Env.instance()
        return f.house
