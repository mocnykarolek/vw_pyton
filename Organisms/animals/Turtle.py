import random

from Organisms.animals.Animal import Animal


class Turtle(Animal):
    def __init__(self,x,y,world, age=None, strength=None ):
        super().__init__(x, y, world )
        self._Color = "blue"
        self._Name = "TURTLE"
        self._initiative = 1
        self._age = age if age is not None else 0
        self._strength = strength if strength is not None else 2
        self._alive = True


    def _actionModifier(self):

        ra = random.randint(0,3)
        if ra == 3:
            return self._randomMove()
        else:
            return self._x, self._y

    def _isAttackBlocked(self, attacker):
        if attacker.getStrength() < 5:
            return True
        else:
            return False # potencjalny blad

    def _newOrganism(self,x,y):
        self._world.addOrganism(Turtle(x,y,self._world))
        self._world.addLog("A new Turtle born")

