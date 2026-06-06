from Organisms.plants.Plant import Plant

from Organisms.animals.CyberSheep import CyberSheep

class Sosnowski(Plant):

    def __init__(self,x,y, world, age=None, strength=None ):
        super().__init__(x, y, world)
        self._Color = "lightGrey"
        self._Name = "SOSNOWSKI"
        self._age = age if age is not None else 0
        self._strength = 10
        self._alive = True
    def __getNeighbouringAnimals(self):
        positions_array = []
        cx,cy = self._x, self._y

        if cy < 19:
            org = self._world.getCell(cx,cy+1)
            if org is not None and org.isPlant() == False:
                positions_array.append(org)
        if cy > 0:
            org = self._world.getCell(cx,cy-1)
            if org is not None and org.isPlant() == False:
                positions_array.append(org)
        if cx < 19:
            org = self._world.getCell(cx+1,cy)
            if org is not None and org.isPlant() == False:
                positions_array.append(org)
        if cx > 0:
            org = self._world.getCell(cx-1,cy)
            if org is not None and org.isPlant() == False:
                positions_array.append(org)


        return positions_array

    def action(self):
        neighboring_cells = self.__getNeighbouringAnimals()
        for cell in neighboring_cells:
            if not isinstance(cell,CyberSheep):
                self._world.addLog("Sonowski killed an animal")
                cell.kill()
        super().action()

    def _isAttackBlocked(self, attacker):
        return False

    def _eatenPlant(self, attacker):
        self.kill()
        if not isinstance(attacker,CyberSheep):
            self._world.addLog("A Sosnowski killed an animal")
            attacker.kill()
        else:
            self._world.addLog("CyberSheep ate Sosnowski")


    def _newOrganism(self,x,y):
        self._world.addOrganism(Sosnowski(x,y,self._world))
        self._world.addLog("A Sosnowski just spread")

