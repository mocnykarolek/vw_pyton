import random

from Organisms.Organisms import Organism
from Organisms.animals.Animal import Animal


class Plant(Animal):
    def __init__(self,x,y, world):
        super().__init__(x,y, world)
        self._shift_range = 0
        self._initiative = 0
        self._strength = 0

    def isPlant(self):
        return True


    def _reproduction_attempt(self, o: Organism):
        freeCells = self._world.getFreeNeighbours(self._x, self._y)
        if len(freeCells) > 0:
            self._newOrganism(freeCells[0][1], freeCells[0][0])
        else:
            self._world.addLog("Not enough space for a new plant")
            
    def action(self):

        probability = random.randint(0,30)

        if probability == 3:
            self._reproduction_attempt(self)