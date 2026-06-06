import abc

from typing import TYPE_CHECKING

import random

if TYPE_CHECKING:
    from World import World

class Organism:
        def __init__(self, x, y, world):

            self._age = 0
            self._Name = ""
            self._alive = False
            self._initiative = None
            self._shift_range = 0
            self._strength = None
            self._Color = None
            self._prev_x = None
            self._prev_y = None

            self.name = None
            self._x = x
            self._y = y
            self._world = world
            self._can_organism_move = True
            

        def incrementAge(self):
            self._age += 1

        def isAlive(self):
            return self._alive

        def kill(self):
            self._alive = False

        def isPlant(self):
            return False

        def getName(self):
            return self._Name

        def _randomMove(self):

            vector = [
                (0, -self._shift_range),
                (0, self._shift_range),
                (-self._shift_range, 0),
                (self._shift_range, 0)
            ]
            available_moves = [
                (self._x + dx, self._y + dy) for (dx, dy) in vector
            ]
            possible_moves = [
                (nx,ny) for (nx, ny) in available_moves
                if 0 <= nx < 20 and 0 <= ny < 20
            ]
            if not possible_moves:
                return self._x, self._y
            return random.choice(possible_moves)


        def _actionModifier(self):
            return self._randomMove()

        @abc.abstractmethod
        def action(self):
            pass


        def getY(self):
            return self._y
        def getX(self):
            return self._x

        def getAge(self):
            return self._age

        def setInitialCords(self, x, y):
            self._x = x
            self._y = y

        def getInitiative(self):
            return self._initiative

        def increaseStrength(self, points):
            self._strength += points

        def getStrength(self):
            return self._strength

        def getColor(self):

            return self._Color

        @abc.abstractmethod
        def _newOrganism(self,x,y):
            pass

        def _isAttackBlocked(self, attacker):
            return False

        def _eatenPlant(self, attacker):
            pass

        def collision(self, other):
            self._world.addLog("Collision")
            if self.getColor() == other.getColor(): # reproduction

                self._can_organism_move = False
                child_cords = self._world.getFreeNeighbours( self._x, self._y )
                if len(child_cords) != 0:
                    self._newOrganism(child_cords[0][1], child_cords[0][0])
                else:
                    self._world.addLog("Not enough space for reproduction")

            else: # combat


                if other._isAttackBlocked(self):
                    self._can_organism_move = False
                    self._world.addLog("Dodged")
                elif self.getStrength() >= other.getStrength():
                    other._eatenPlant(self)
                    other.kill()
                else:
                    if other.isPlant():
                        other._eatenPlant(self)
                    self.kill()

        def saveHuman(self):
            pass