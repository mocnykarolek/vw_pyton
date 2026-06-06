from Organisms.animals.Animal import Animal


class Wolf(Animal):
    def __init__(self,x,y,world, age=None, strength=None ):
        super().__init__(x, y, world )
        self._Color = "grey"
        self._Name = "WOLF"
        self._initiative = 5
        self._age = age if age is not None else 0
        self._strength = strength if strength is not None else 9
        self._alive = True


    def _newOrganism(self,x,y):
        self._world.addOrganism(Wolf(x,y,self._world))
        self._world.addLog("A new Wolf born")

