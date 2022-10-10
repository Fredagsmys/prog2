import tkinter as tk
import Ball

class Simulation:

    def __init__(self, balls):
        self.gui = tk.Tk()
        self.canvas = tk.Canvas(self.gui, width=1000, height=800, borderwidth=0, highlightthickness=0, bg="black")
        self.time = 0
        self.balls = [Ball.Ball(10, 10, 10) for _ in range(balls)]

    def __str__(self):
        pass

    def start(self):
        self.canvas.grid()

        self.draw_circle()
        self.gui.mainloop()

    def draw_circle(self):
        for ball in self.balls:
            self.canvas.create_oval(100, 100, 200, 200, fill='blue')

    def step(self):
        self.time += 1

def main():

    sim = Simulation()

    sim.start()


if __name__ == "__main__":
    main()
