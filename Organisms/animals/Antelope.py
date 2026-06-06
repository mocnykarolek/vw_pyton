import random

from Organisms.animals.Animal import Animal


class Antelope(Animal):
    def __init__(self,x,y,world, age=None, strength=None ):
        super().__init__(x, y, world )
        self._Color = "magenta"
        self._Name = "ANTELOPE"
        self._initiative = 4
        self._age = age if age is not None else 0
        self._strength = strength if strength is not None else 4
        self._alive = True
        self._shift_range = 2

    def _isAttackBlocked(self, attacker):
        chance = random.randint(0,1)
        if chance == 0:
            avaliable_cells = self._world.getFreeNeighbours(self._x, self._y)

            if len(avaliable_cells) > 0:
                self._world.updateGrid(self, avaliable_cells[0][1], avaliable_cells[0][0], self._x, self._y)
                self._x = avaliable_cells[0][1]
                self._y = avaliable_cells[0][0]
                self._world.addLog("Antelope escaped")
                return True
        return False

    def _newOrganism(self,x,y):
        self._world.addOrganism(Antelope(x,y,self._world))

