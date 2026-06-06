from typing import TYPE_CHECKING

from Organisms.animals.Antelope import Antelope
from Organisms.animals.CyberSheep import CyberSheep
from Organisms.animals.Fox import Fox
from Organisms.animals.Human import Human
from Organisms.animals.Sheep import Sheep
from Organisms.animals.Turtle import Turtle
from Organisms.animals.Wolf import Wolf
from Organisms.plants.Belladonna import Belladonna
from Organisms.plants.Dandelion import Dandelion
from Organisms.plants.Grass import Grass
from Organisms.plants.Guarana import Guarana
from Organisms.plants.Sosnowski import Sosnowski
from Window import Window
import random
if TYPE_CHECKING:
    from Organisms.Organisms import Organism


class World:


    def __init__(self):
        self.__organisms: list['Organism'] = []
        self.__grid: list[list['Organism' | None]] = [[None for _ in range(20)] for _ in range(20)]

        self.__round_number = 0
        self.__next_human_move = 0
        self.__special_ability = False
        self.__human_reference = None
        self.__sosnowski_references = []


        self.__window = Window(self)


        self.__generate_initial_world()

        self.__window.init()




    def getSpecialAbility(self):
        return self.__special_ability

    def setSpecialAbility(self, special_ability):
        self.__special_ability = special_ability


    def getHumanReference(self):
        return self.__human_reference






    def __generate_initial_world(self):
        print("generate_initial_world")

        human = Human(10, 10, self)
        self.human_reference = human
        self.addOrganism(human)
        #
        # wolf_number = 5
        # for i in range(wolf_number):
        #     x,y = self.__randomUnoccupiedCords()
        #     self.addOrganism(Wolf(x,y,self))
        #
        # sheep_number = 6
        # for i in range(sheep_number):
        #     x, y = self.__randomUnoccupiedCords()
        #     self.addOrganism(Sheep(x, y, self))
        #
        # fox_number = 4
        # for i in range(fox_number):
        #     x, y = self.__randomUnoccupiedCords()
        #     self.addOrganism(Fox(x, y, self))
        # turtle_number = 3
        # for i in range(turtle_number):
        #     x, y = self.__randomUnoccupiedCords()
        #     self.addOrganism(Turtle(x, y, self))
        # antelope_number = 4
        # for i in range(antelope_number):
        #     x, y = self.__randomUnoccupiedCords()
        #     self.addOrganism(Antelope(x, y, self))
        cybersheep_number = 2
        for i in range(cybersheep_number):
            x, y = self.__randomUnoccupiedCords()
            self.addOrganism(CyberSheep(x, y, self))
        #
        #
        #
        # grass_number = 3
        # for i in range(grass_number):
        #     x,y = self.__randomUnoccupiedCords()
        #     self.addOrganism(Grass(x,y,self))
        #
        # dandelion_number = 3
        # for i in range(dandelion_number):
        #     x, y = self.__randomUnoccupiedCords()
        #     self.addOrganism(Dandelion(x, y, self))
        #
        # guarana_number = 5
        # for i in range(guarana_number):
        #     x, y = self.__randomUnoccupiedCords()
        #     self.addOrganism(Guarana(x, y, self))
        #
        # belladonna_number = 3
        # for i in range(belladonna_number):
        #     x, y = self.__randomUnoccupiedCords()
        #     self.addOrganism(Belladonna(x, y, self))

        barszcz_number = 3
        for i in range(barszcz_number):
            x, y = self.__randomUnoccupiedCords()
            sosnowski = Sosnowski(x, y, self)
            self.addOrganism(sosnowski)
            self.__sosnowski_references.append(sosnowski)



    def __randomUnoccupiedCords(self):

        empty_slots = [
            (x,y)
            for x in range(20)
            for y in range(20)
            if self.__grid[y][x] is None
        ]

        if not empty_slots:
            return None, None

        return random.choice(empty_slots)

    def getSosnowskiReferences(self):
        return [barszcz for barszcz in self.__sosnowski_references if barszcz.isAlive()]

    def isHumanAlive(self):
        # return self.__human_reference.isAlive()
        return True



    def getCell(self, x, y):

        return self.__grid[y][x]

    def getFreeNeighbours(self, x, y):
        position_array = []
        if y < 19 and self.__grid[y+1][x] is None:
            position_array.append([y+1,x])

        if y > 0 and self.__grid[y-1][x] is None:
            position_array.append([y-1,x])

        if x < 19 and self.__grid[y][x+1] is None:
            position_array.append([y,x+1])

        if x > 0 and self.__grid[y][x-1] is None:
            position_array.append([y,x-1])


        return position_array





    def isOccupied(self, x, y):
        if self.__grid[y][x] is None:
            return False
        return True


    def getRoundNumber(self):
        return self.__round_number


    def getHumanDir(self):
        return self.__human_reference

    def setHumanDir(self, human_dir):
        self.__human_reference = human_dir

    def round(self):
        self.__round_number += 1
        self.__window.setRoundNumber(self.__round_number)

        self.__organisms.sort(key=lambda o: (-o.getInitiative(), -o.getAge()))

        start_number = len(self.__organisms)

        for i in range(start_number):
            if self.__organisms[i].isAlive():
                self.__organisms[i].action()
                self.__organisms[i].incrementAge()









        self.__collisionHandling()


        self.__window.draw_round(self.__grid)
        self.__special_ability = False


    def getLogs(self):
        # return self.__
        pass
    def updateGrid(self, o, x,y,old_x,old_y):

        self.__grid[old_y][old_x] = None
        self.__grid[y][x] = o


    def __collisionHandling(self):
        for o in self.__organisms:
            if not o.isAlive():
                self.__removeOrganisms(o) # potencjalny problem z duchami


    def __removeOrganisms(self, o):
        if self.__grid[o.getY()][o.getX()] == o:
            self.__grid[o.getY()][o.getX()] = None
        self.__organisms.remove(o)

        if isinstance(o, Sosnowski) and o in self.__sosnowski_references:
            self.__sosnowski_references.remove(o)



    def addLog(self, log):

        self.__window.addLog(log)

    def addOrganism(self, o):

        self.__organisms.append(o)
        self.__grid[o.getY()][o.getX()] = o



    def drawOrganism(self, organisms):
        pass

    def humanSpecialAbilityActivated(self):
        if self.__special_ability:
            return self.__round_number
        else:
            return -1

    def getCurrentRound(self):
        return self.__round_number



    def SaveToFile(self):
        # with open("gamestate.txt", "w") as file:
        to_save = []
        to_save.append(f"ROUND {self.__round_number}")
        for o in self.__organisms:

            if o != self.human_reference:
                to_save.append(f"{o.getName()} {o.getX()} {o.getY()} {o.getAge()} {o.getStrength()}")
            else:
                to_save.append(f"{o.getName()} {o.getX()} {o.getY()} {o.getAge()} {o.getStrength()} {o.saveHuman()}")
        with open("gamestate.txt", "w") as file:
            for l in to_save:
                file.write(l + "\n")
        self.addLog("Saved!")


    def LoadFromFile(self):
        f = []
        self.__organisms.clear()
        self.__grid: list[list['Organism' | None]] = [[None for _ in range(20)] for _ in range(20)]
        self.__sosnowski_references.clear()
        with open("gamestate.txt", "r") as file:

            f = file.readlines()
            if len(f) != 0:
                for l in f:
                    l = l.strip("\n").split(" ")

                    if l[0] == "ROUND":
                        self.__round_number = int(l[1])
                    else:
                        x = int(l[1])
                        y = int(l[2])
                        age = int(l[3])
                        strength = int(l[4])
                        if l[0] == "HUMAN":
                            elixirActive = (l[5] == "True")

                            elixirBonus = int(l[6]) if l[6] not in ("None", "") else 0
                            roundOfActivation = int(l[7]) if l[7] not in ("None", "") else 0
                            cooldownLeft = int(l[8]) if l[8] not in  ("None", "") else 0
                            human = Human(x,y,self,age,strength,elixirActive, elixirBonus, roundOfActivation, cooldownLeft)
                            self.humanReference = human
                            self.addOrganism(human)
                        elif l[0] == "WOLF":
                            self.addOrganism(Wolf(x,y,self,age,strength))
                        elif l[0] == "SHEEP":
                            self.addOrganism(Sheep(x,y,self,age,strength))
                        elif l[0] == "FOX":
                            self.addOrganism(Fox(x,y,self,age,strength))
                        elif l[0] == "TURTLE":
                            self.addOrganism(Turtle(x,y,self,age,strength))
                        elif l[0] == "ANTELOPE":
                            self.addOrganism(Antelope(x,y,self,age,strength))
                        elif l[0] == "CYBERSHEEP":
                            self.addOrganism(CyberSheep(x,y,self,age,strength))


                        elif l[0] == "GRASS":
                            self.addOrganism(Grass(x,y,self,age,strength))
                        elif l[0] == "DANDELION":
                            self.addOrganism(Dandelion(x,y,self,age,strength))
                        elif l[0] == "GUARANA":
                            self.addOrganism(Guarana(x,y,self,age,strength))
                        elif l[0] == "BELLADONNA":
                            self.addOrganism(Belladonna(x,y,self,age,strength))
                        elif l[0] == "SOSNOWSKI":
                            sosnowski = Sosnowski(x,y,self,age,strength)
                            self.addOrganism(sosnowski)
                            self.__sosnowski_references.append(sosnowski)

                        #continue
                self.__window.setRoundNumber(self.__round_number)
                self.__window.draw_round(self.__grid)
                self.addLog("Loaded!")
            else:
                print("Gamestate file is empty")
