from typing import TYPE_CHECKING

from Organisms.animals.Animal import Animal


if TYPE_CHECKING:
    from World import World

EAST = 2
NORTH = 1
SOUTH = 3
WEST = 4

class Human(Animal):
    def __init__(self,x,y,world, age=None, strength=None, elixirActive=None, elixirBonus=None, roundOfActivation=None,cooldownLeft=None ):
        super().__init__(x, y, world )
        self.__currentRound = None
        self._Name = "HUMAN"
        self._Color = "pink"
        self._initiative = 5
        self._age = age if age is not None else 0
        self._strength = strength if strength is not None else 5
        self._alive = True
        self._world.setSpecialAbility(False)
        self.__elixirActive = elixirActive if elixirActive is not None else False
        self.__elixirBonus = elixirBonus if elixirBonus is not None else 0
        self.__roundOfActivation = roundOfActivation
        self.__cooldownLeft = cooldownLeft if cooldownLeft is not None else 0
        # self.strength = self._strength + self.__elixirActive


    def saveHuman(self):
        return f"{self.__elixirActive} {self.__elixirBonus} {self.__roundOfActivation} {self.__cooldownLeft}"

    def handleSpecialAbility(self):
        if(self.__elixirActive == True and self.__currentRound > self.__roundOfActivation):
            self.__elixirBonus -=1

        if self.__currentRound - self.__roundOfActivation >= 5:
            self.__elixirActive = False
            self.elixirBonus = 0
            self.__cooldownLeft = 5
            self._world.addLog("No elixir left")


    def getStrength(self):
        return (self._strength + self.__elixirBonus)


    def action(self):
        print(self.getStrength())
        self.__currentRound = self._world.getCurrentRound()

        if self.__elixirActive:
            self.handleSpecialAbility()


        if self._world.getSpecialAbility() == True and self.__cooldownLeft == 0 and self.__elixirActive == False:
            self.__elixirActive = True
            self.__elixirBonus = 5
            self._world.addLog("Human drank magic elixir")
            self.__roundOfActivation = self.__currentRound

        if self.__cooldownLeft > 0:
            self.__cooldownLeft -= 1



        self._prev_x = self._x
        self._prev_y = self._y

        new_x, new_y = self._x, self._y

        nextMove = self._world.getHumanDir()

        if nextMove == NORTH and self._y > 0:
            new_x -=1
            self._world.addLog("Human went North")
        elif nextMove == SOUTH and self._y < 19:
            new_x +=1
            self._world.addLog("Human went South")
        elif nextMove == WEST and self._x > 0:
            new_y -=1
            self._world.addLog("Human went WEST")
        elif nextMove == EAST and self._x < 19:
            new_y +=1
            self._world.addLog("Human went EAST")


        self._can_organism_move = True

        if self._world.isOccupied(new_x, new_y):

            if self._world.getCell(new_x, new_y) != self:
                self.collision(self._world.getCell(new_x, new_y))

                if self.isAlive():
                    self._x = new_x
                    self._y = new_y
                    self._world.updateGrid(self, new_x, new_y , self._prev_x, self._prev_y)


        else:
            self._x = new_x
            self._y = new_y
            self._world.updateGrid(self, new_x, new_y, self._prev_x, self._prev_y)


    def _newOrganism(self,x,y):
        self._world.addOrganism(Human(x,y,self._world))

