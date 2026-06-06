from Organisms.animals.Animal import Animal
import math

class CyberSheep(Animal):
    def __init__(self,x,y,world, age=None, strength=None ):
        super().__init__(x, y, world )
        self._Color = "lightPink"
        self._Name = "CYBERSHEEP"
        self._initiative = 4
        self._age = age if age is not None else 0
        self._strength = strength if strength is not None else 10
        self._alive = True


    def _actionModifier(self):

        sosnowscy = self._world.getSosnowskiReferences()

        if len(sosnowscy) > 0:
            # vector = [(0,1), (0,-1), (1,0), (-1,0)]

            sosnowscy.sort(key=lambda x:math.dist((self.getX(), self.getY()), (x.getX(), x.getY())))
            selected = sosnowscy[0]
            dx = selected.getX() - self._x
            dy = selected.getY() - self._y


            nx,ny = self._x, self._y
            if abs(dx) > abs(dy):
                if dx > 0:
                    nx +=1
                else:
                    nx -= 1
            else:
                if dy > 0:
                    ny +=1
                else:
                    ny -= 1

            return (nx,ny)


            # px, py = self._x, self._y




        return super()._actionModifier()

    def _newOrganism(self,x,y):
        self._world.addOrganism(CyberSheep(x,y,self._world))
        self._world.addLog("A new CyberSheep born")

