from Organisms.animals.Animal import Animal


class Sheep(Animal):
    def __init__(self,x,y,world, age=None, strength=None ):
        super().__init__(x, y, world )
        self._Color = "sheepy"
        self._Name = "SHEEP"
        self._initiative = 4
        self._age = age if age is not None else 0
        self._strength = strength if strength is not None else 4
        self._alive = True


    def _newOrganism(self,x,y):
        self._world.addOrganism(Sheep(x,y,self._world))
        self._world.addLog("A new Sheep born")
