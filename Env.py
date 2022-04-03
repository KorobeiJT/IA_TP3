import time
import random
import threading

from Singleton import Singleton

@Singleton
class Env:

    def init(self, level):
        #F = Feu ; D = Décombres ; P = Poussière ; C = Chaleur ; V = Victime ; R = Robot ; H = Hurlements
        self.env = [['' for i in range(level+2)] for j in range(level+2)]
        self.size = level + 2
        self.env[0][0]='R'
        for i in range(max((level**2)//3, 2)):
            if random.random()<0.5:
                self.fire_spawn()
            else:
                self.rubbles_spawn()
        self.victim_spawn()
        self.print_env()

    def fire_spawn(self):
        x=random.randrange(0,self.size)
        y=random.randrange(0,self.size)
        if self.env[x][y] == '' and [x,y] != [0,0]:
            self.env[x][y] = 'F'
            self.heat_spawn(x,y)
        else:
            self.fire_spawn()

    def rubbles_spawn(self):
        x=random.randrange(0,self.size)
        y=random.randrange(0,self.size)
        if self.env[x][y] == '' and [x,y] != [0,0]:
            self.env[x][y] = 'D'
            self.dirt_spawn(x,y)
        else:
            self.rubbles_spawn()

    def victim_spawn(self):
        x=random.randrange(0,self.size)
        y=random.randrange(0,self.size)
        if not ('F' in self.env[x][y] or 'D' in self.env[x][y]) and [x,y] != [0,0]:
            self.env[x][y] = 'V'
            self.scream_spawn(x,y)
        else:
            self.victim_spawn()

    def dirt_spawn(self, i, j) :
        self.env[min(i+1, self.size-1)][j] += 'P'
        self.env[i][min(j+1, self.size-1)] += 'P'
        self.env[max(i-1, 0)][j] += 'P'
        self.env[i][max(j-1, 0)] += 'P'
        self.env[i][j] = 'D'
    
    def heat_spawn(self, i, j) :
        self.env[min(i+1, self.size-1)][j] += 'C'
        self.env[i][min(j+1, self.size-1)] += 'C'
        self.env[max(i-1, 0)][j] += 'C'
        self.env[i][max(j-1, 0)] += 'C'
        self.env[i][j] = 'F'
    
    def scream_spawn(self, i, j) :
        self.env[min(i+1, self.size-1)][j] += 'H'
        self.env[i][min(j+1, self.size-1)] += 'H'
        self.env[max(i-1, 0)][j] += 'H'
        self.env[i][max(j-1, 0)] += 'H'
        self.env[i][j] = 'V'
    
    def print_env(self):
        for i in self.env:
            print(i)