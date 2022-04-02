
from BDI import BDI
from Env import Env
from Sensors import Sensor
from Effectors import Effector
import time
import Search

class Robot:

    env=[[0, 0, 0, 0, 0], #0 empty - 1 jewel - 10 dirt - 11 dirt + jewel
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
    
    env_graph=Search.create_graph()

    position=(2,2)
    destination=(0,0)

    bdi=BDI()
    plan_action=0

    roomsVisited=0  #metric used
    jewelPickedUp=0
    jewelVacuumed=0

    sensor=Sensor()
    effector=Effector()

    @classmethod
    def display_env(self):
        for x in self.env:
            print(x)
        print()

    @classmethod
    def print_stats(self):
        print("Rooms visited = ",self.roomsVisited)
        print("Jewels vacuumed = ",self.jewelVacuumed)
        print("Jewels picked up = ",self.jewelPickedUp)
    
    @classmethod
    def observe(self):
        print("Observing Environment...")
        self.env=self.sensor.Sense()
        self.display_env()
        print("position actuelle = ",self.position)
    
    @classmethod
    def updateBDI(self):
        self.bdi.intent=0
        print("Updating BDI state...")
        if self.env[self.position[0]][self.position[1]]>=10 : #dirt or dirt + jewel where the robot is
            self.bdi.beliefs=[self.position, self.env[self.position[0]][self.position[1]]]
            self.bdi.desire=1
            self.bdi.intent=1
            self.destination=self.position

        elif self.env[self.position[0]][self.position[1]]==1: # jewel where the robot is
            self.bdi.beliefs=[self.position, self.env[self.position[0]][self.position[1]]]
            self.bdi.desire=2
            self.bdi.intent=4
            self.destination=self.position
        
        else: #nothing where the robot is
            for i in range(len(self.env)):
                for j in range(len(self.env[i])):
                    match self.env[i][j]:
                        case 1: #jewel only
                            self.destination=(i,j)
                            print("Jewel to pick up at ", self.destination)
                            if self.roomsVisited<15:
                                self.bdi.beliefs=[self.destination, self.env[i][j]]
                                self.bdi.desire=2
                                self.bdi.intent=2
                                return
                            else:
                                self.bdi.beliefs=[self.destination, self.env[i][j]]
                                self.bdi.desire=2
                                self.bdi.intent=3
                                return
                        case 11: #jewel and dirt
                            self.destination=(i,j)
                            print("Jewel and dirt to vacuum at ", self.destination)
                            if self.roomsVisited<15:
                                self.bdi.beliefs=[self.destination, self.env[i][j]]
                                self.bdi.desire=1
                                self.bdi.intent=2
                                return
                            else:
                                self.bdi.beliefs=[self.destination, self.env[i][j]]
                                self.bdi.desire=1
                                self.bdi.intent=3
                                return
                        case 10: #dirt only
                            self.destination=(i,j)
                            print("Dirt to vacuum at ", self.destination)
                            if self.roomsVisited<15:
                                self.bdi.beliefs=[self.destination, self.env[i][j]]
                                self.bdi.desire=1
                                self.bdi.intent=2
                                return
                            else:
                                self.bdi.beliefs=[self.destination, self.env[i][j]]
                                self.bdi.desire=1
                                self.bdi.intent=3
                                return
                        case _: #empty
                            continue
        
        if self.bdi.intent==0: #nothing was found anywhere, house is clean
            print("Global objective reached - No dirt or jewel")                    
    
    @classmethod
    def explore(self):
        match self.bdi.intent:
            case 1: 
                print("Building action plan...")
                print("Vacuum")
                self.plan_action=[self.position]
            case 4:
                print("Building action plan...")
                print("Pick up jewel")
                self.plan_action=[self.position]
            case 2:
                print("Building action plan...")
                print("Move - Uninformed Search")
                self.plan_action=Search.bfs(self.env_graph, self.position, self.destination)
                print("Path chosen = ", self.plan_action)
            case 3:
                print("Building action plan...")
                print("Move - Informed Search")
                self.plan_action=Search.Astar(self.env, self.position, self.destination)
                print("Path chosen = ", self.plan_action)
            case _:
                self.plan_action=[]
        return 1

    @classmethod
    def execute(self):
        if self.plan_action != []:
            print("Executing action plan...")
            envi=Env.instance()
            for i in self.plan_action:
                self.roomsVisited+=1
                match envi.house[i[0]][i[1]]:
                    case 1: #jewel only
                        self.jewelPickedUp+=1
                        self.effector.PickUp(i)
                    case 11: #jewel and dirt
                        self.jewelVacuumed+=1
                        self.effector.Vacuum(i)
                    case 10: #dirt only
                        self.effector.Vacuum(i)
                    case _: #empty
                        continue
            self.position=self.destination

    @classmethod
    def analysis_cycle(self):
        print("START ANALYSIS CYCLE")
        self.observe()
        self.updateBDI()
        self.explore()
        self.execute()
        self.print_stats()
        print("CYCLE FINISHED")
        print()
        time.sleep(3)
    
    
    

