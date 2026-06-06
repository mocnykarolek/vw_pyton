from Organisms.plants.Plant import Plant


class Grass(Plant):

    def __init__(self,x,y, world, age=None, strength=None ):
        super().__init__(x, y, world)
        self._Color = "green"
        self._Name = "GRASS"
        self._age = age if age is not None else 0

        self._alive = True

    def _isAttackBlocked(self, attacker):
        return False

    def _newOrganism(self,x,y):
        self._world.addOrganism(Grass(x,y,self._world))
        self._world.addLog("A Grass just spread")