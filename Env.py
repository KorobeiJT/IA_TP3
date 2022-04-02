import time
import random
import threading

from Singleton import Singleton

@Singleton
class Env:

    house=[[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

    @classmethod
    def jewel_spawn(self) :
        x=random.randrange(0,5)
        y=random.randrange(0,5)
        if self.house[x][y]%10!=1:
            self.house[x][y]+=1
       
    @classmethod
    def dirt_spawn(self) :
        x=random.randrange(0,5)
        y=random.randrange(0,5)
        if self.house[x][y]%100<10:
            self.house[x][y]+=10
    
    @classmethod
    def spawn(self):
        iter=0
        while 1:
            iter+=1
            freq= random.randrange(2,6,1)
            self.dirt_spawn()
            if iter>4:
                self.jewel_spawn()
                iter=0
            time.sleep(freq)