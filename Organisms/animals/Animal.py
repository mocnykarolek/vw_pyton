from Organisms.Organisms import Organism


class Animal(Organism):
    def __init__(self, x, y, world):

        super().__init__(x, y, world)
        self._shift_range = 1


    def action(self):

        self._prev_x = self._x
        self._prev_y = self._y

        prev_cords = [self._x, self._y]
        new_cords_x, new_cords_y = self._actionModifier()

        self._can_organism_move = True

        if self._world.isOccupied(new_cords_x, new_cords_y):

            if self._world.getCell(new_cords_x, new_cords_y) != self:
                self.collision(self._world.getCell(new_cords_x, new_cords_y))

                if self.isAlive() and self._can_organism_move:

                    self._x = new_cords_x
                    self._y = new_cords_y
                    self._world.updateGrid(self, new_cords_x, new_cords_y, prev_cords[0], prev_cords[1])
        else:
            self._x = new_cords_x
            self._y = new_cords_y
            self._world.updateGrid(self, new_cords_x, new_cords_y, prev_cords[0], prev_cords[1])