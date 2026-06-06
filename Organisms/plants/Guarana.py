from Organisms.plants.Plant import Plant


class Guarana(Plant):

    def __init__(self,x,y, world, age=None, strength=None ):
        super().__init__(x, y, world)
        self._Color = "cyan"
        self._Name = "Guarana"
        self._age = age if age is not None else 0

        self._alive = True

    def _isAttackBlocked(self, attacker):
        return False

    def _eatenPlant(self, attacker):
        attacker.increaseStrength(3)
        self._world.addLog("Guarana added 3 points of strength")

    def _newOrganism(self,x,y):
        self._world.addOrganism(Guarana(x,y,self._world))
        self._world.addLog("A Guarana just spread")