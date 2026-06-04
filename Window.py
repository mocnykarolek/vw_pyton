import tkinter as tk
from turtledemo.paint import switchupdown
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Organisms.Organisms import Organism

class Window:


    def __init__(self, world):
        self.__world = world
        self.__root = tk.Tk()
        self.__root.title("Human Move")
        self.__root.geometry("800x600")
        self.__humanMove = "null"
        self.__canvas = tk.Canvas(self.__root,width=400, height=400, bg="white", highlightthickness=0, borderwidth=0)
        self.__canvas.grid(row=0, column=0)

        self.__round_label = 0



        self.__logs = tk.Text(self.__root, width=40, height=25, bg="white", state="disabled")
        self.__logs.grid(row=0, column=1)

        self.__dolny_panel = tk.Frame(self.__root)
        self.__dolny_panel.grid(row=1, column=0, pady=10)


        self.__label_autor = tk.Label(self.__dolny_panel, text="Karol Olędzki 208226", font=("Arial", 10, "bold"))
        self.__label_autor.grid(row=0, column=0, padx=10)


        self.__label_tura = tk.Label(self.__dolny_panel, text="Round: 0", font=("Arial", 12))
        self.__label_tura.grid(row=0, column=1, padx=10)


        self.__label_czlowiek = tk.Label(self.__dolny_panel, text="Human next: null")
        self.__label_czlowiek.grid(row=0, column=2, padx=10)



    def __renderLogs(self, logs):
        pass

    def __setRoundLabel(self, number: int):

        self.__label_tura.config(text=f"Round: {number}")

    def __setHumanNextMoveLabel(self, dir: str):

        self.__label_czlowiek.config(text=f"Human next: {dir}")


    def addLog(self, log):

        self.__logs.config(state="normal")
        self.__logs.insert(tk.END, log + "\n")
        self.__logs.config(state="disabled")
        self.__logs.config(state="disabled")



    def draw_round(self, grid):

        self.__canvas.delete("all")

        size = 20

        for i in range(size):
            for j in range(size):
                x = i * size
                y = j * size
                x1 = x + size
                y1 = y + size



                if grid[i][j] != None:
                    print(i, j)
                    color = ""
                    if grid[i][j].getColor() == "pink":
                        color = "pink"
                    elif grid[i][j].getColor() == "grey":
                        color = "grey"
                        print("tset")
                    # dokonczyc koklory

                    self.__canvas.create_rectangle(x, y, x1, y1, fill=color)


                else:
                    self.__canvas.create_rectangle(x, y, x1, y1, fill="white")
        self.setHumanNextMove("null")




    def init(self):
        self.__root.bind("<Key>", self.__handleInput)

        # new round button
        new_round_button = tk.Button(self.__root, text="New Round", command=self.__new_round)
        new_round_button.grid(row=2, column=0)

        # load button
        load_button = tk.Button(self.__root, text="Load", command="")
        load_button.grid(row=1, column=1)

        # save button
        save_button = tk.Button(self.__root, text="Save", command="")
        save_button.grid(row=1, column=2)




        self.__root.mainloop()



    def __new_round(self):
        if (self.__humanMove != "null" and self.__humanMove != "special") or self.__world.isHumanAlive() == False:
            self.__world.round()
            self.__setRoundLabel(self.__round_label)

    def __handleInput(self, event):


        if event.keysym == "Up":

            self.setHumanNextMove("Up")

        elif event.keysym == "Down":

            self.setHumanNextMove("Down")

        elif event.keysym == "Left":

            self.setHumanNextMove("Left")

        elif event.keysym == "Right":

            self.setHumanNextMove("Right")

        elif event.keysym == "enter":

            self.setHumanNextMove("special")

        elif event.keysym == "space":
            self.__new_round()



    def setHumanNextMove(self, dir):
        self.__humanMove = dir
        if self.__humanMove == "null":
            self.__setHumanNextMoveLabel("")
            self.__world.setHumanDir(-1)
        elif self.__humanMove == "special":
            self.__world.setSpecialAbility(True)
        else:
            self.__setHumanNextMoveLabel(dir)
            to_set = 0
            if dir == "Left":
                to_set = 4
            elif dir == "Right":
                to_set = 2
            elif dir == "Up":
                to_set = 1
            elif dir == "Down":
                to_set = 3
            self.__world.setHumanDir(to_set)


    def setRoundNumber(self, number):
        self.__round_label = number
        pass


