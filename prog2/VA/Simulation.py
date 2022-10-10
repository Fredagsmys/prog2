import tkinter as tk


class Simulation:

    def __init__(self):
        self.gui = tk.Tk()
        self.canvas = tk.Canvas(self.gui, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="black")
        self.time = 0
        balls = []

    def __str__(self):
        pass

    def start(self):
        self.canvas.grid()

        self.draw_circle()
        self.gui.mainloop()

    def draw_circle(self):
        self.canvas.create_oval(100,100,200,200, fill='blue')

    def step(self):
        self.time += 1

def main():

    sim = Simulation()

    sim.start()


if __name__ == "__main__":
    main()
