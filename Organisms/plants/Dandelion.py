import random

from Organisms.plants.Plant import Plant


class Dandelion(Plant):

    def __init__(self,x,y, world, age=None, strength=None ):
        super().__init__(x, y, world)
        self._Color = "yellow"
        self._Name = "DANDELION"
        self._age = age if age is not None else 0

        self._alive = True

    def _isAttackBlocked(self, attacker):
        return False


    def action(self):
        attempts = 3
        for i in range(attempts):
            probability = random.randint(0,43)

            if probability == 3:
                self._reproduction_attempt(self)

    def _newOrganism(self,x,y):
        self._world.addOrganism(Dandelion(x,y,self._world))
        self._world.addLog("A Dandelion just spread")