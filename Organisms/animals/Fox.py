import random

from Organisms.animals.Animal import Animal


class Fox(Animal):
    def __init__(self,x,y,world, age=None, strength=None ):
        super().__init__(x, y, world )
        self._Color = "orange"
        self._Name = "FOX"
        self._initiative = 7
        self._age = age if age is not None else 0
        self._strength = strength if strength is not None else 3
        self._alive = True

    def _randomMove(self):
        available_moves = []

        cx, cy = self._x, self._y

        if(cx +1 < 20):
            cell = self._world.getCell(cx+1, cy)
            if(cell is None or cell.getStrength() <= self._strength):
                available_moves.append((cx+1, cy))

        if (cx - 1 >= 0):
            cell = self._world.getCell(cx - 1, cy)
            if (cell is None or cell.getStrength() <= self._strength):
                available_moves.append((cx - 1, cy))

        if (cy + 1 < 20):
            cell = self._world.getCell(cx, cy+1)
            if (cell is None or cell.getStrength() <= self._strength):
                available_moves.append((cx, cy+1))

        if (cy - 1 >= 0):
            cell = self._world.getCell(cx, cy-1)
            if (cell is None or cell.getStrength() <= self._strength):
                available_moves.append((cx, cy-1))

        if len(available_moves) == 0:
            return self._x, self._y

        return random.choice(available_moves)


    def _newOrganism(self,x,y):
        self._world.addOrganism(Fox(x,y,self._world))
        self._world.addLog("A new Fox born")

