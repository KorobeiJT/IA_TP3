from Env import Env

class Effector:
    
    @classmethod
    def Vacuum(self, coordinates):
        print("Vacuumed at ", coordinates)
        f= Env.instance()
        f.house[coordinates[0]][coordinates[1]]=0
    
    @classmethod
    def PickUp(self, coordinates):
        print("Picked up a jewel at ",coordinates)
        f= Env.instance()
        f.house[coordinates[0]][coordinates[1]]=0

    