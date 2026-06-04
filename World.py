from typing import TYPE_CHECKING

from Organisms.animals.Wolf import Wolf
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


        self.__window = Window(self)
        self.__window.init()

        self.__generate_initial_world()






    def getSpecialability(self):
        return self.__special_ability

    def setSpecialability(self, special_ability):
        self.__special_ability = special_ability


    def getHumanReference(self):
        return self.__human_reference






    def __generate_initial_world(self):
        print("generate_initial_world")
        wolf_number = 5
        for i in range(wolf_number):
            x,y = self.__randomUnoccupiedCords()
            self.addOrganism(Wolf(x,y,self))


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


    def isHumanAlive(self):
        # return self.__human_reference.isAlive()
        return True



    def getCell(self, x, y):

        return self.__grid[y][x]

    def getFreeNeighbours(self, x, y):
        position_array = []
        if y < 19 and self.__grid[y+1][x] is not None:
            position_array.append([y+1,x])

        if y > 0 and self.__grid[y-1][x] is not None:
            position_array.append([y-1,x])

        if x < 19 and self.__grid[y][x+1] is not None:
            position_array.append([y,x+1])

        if x > 0 and self.__grid[y][x-1] is not None:
            position_array.append([y,x-1])


        return position_array



        pass

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
        if self.__grid[o.getY()][o.getY()] == o:
            self.__grid[o.getY()][o.getY()] = None
        self.__organisms.remove(o)



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
        pass
    def LoadFromFile(self):
        pass
