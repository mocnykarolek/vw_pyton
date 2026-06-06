from Organisms.plants.Plant import Plant


class Belladonna(Plant):

    def __init__(self,x,y, world, age=None, strength=None ):
        super().__init__(x, y, world)
        self._Color = "darkRed"
        self._Name = "BELLADONNA"
        self._age = age if age is not None else 0
        self._strength = 99
        self._alive = True

    def _isAttackBlocked(self, attacker):
        return False

    def _eatenPlant(self, attacker):
        self.kill()
        attacker.kill()
        self._world.addLog("Belladonna killed an animal")


    def _newOrganism(self,x,y):
        self._world.addOrganism(Belladonna(x,y,self._world))
        self._world.addLog("A Grass just spread")