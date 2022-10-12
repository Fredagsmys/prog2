import tkinter as tk
import Ball
import random as rand
import tkinter.ttk as ttk


class Simulation:

    def __init__(self, balls):

        self.gui = tk.Tk()
        self.gui.started = tk.BooleanVar()
        self.timestep = 1
        self.gui.speed = tk.IntVar()
        self.width = 1000
        self.height = 800
        self.gui.canvas = tk.Canvas(self.gui, width=self.width, height=self.height, borderwidth=0, highlightthickness=0,
                                    bg="black")
        speed_entry = ttk.Entry(master=self.gui, textvariable=self.gui.speed)
        start_entry = ttk.Button(text="Start", command=lambda: self.gui.started.set(not self.gui.started.get()))
        self.gui.started.set(True)
        self.gui.speed.set(1)
        speed_entry.pack()
        start_entry.pack()

        self.time = 0
        rad = 20
        self.balls = [Ball.Ball(radius=rad * (rand.random() + 1),
                                spd_x=1 + rand.random(),
                                spd_y=1 + rand.random(),
                                pos_x=rand.randint(rad, self.width - rad),
                                pos_y=rand.randint(rad, self.height - rad),
                                color='blue') for _ in range(balls)]

        if self.gui.started.get():
            self.gui.canvas.pack()
            self.spawn_obj()
            self.start()
        self.gui.canvas.mainloop()

    def start(self):
        self.gui.curr_speed = self.gui.speed.get()
        self.animate()



    def animate(self):
        if self.gui.started.get():

            self.step()
            self.update()
            self.gui.canvas.after(1, self.animate)
        else:
            self.gui.canvas.after(1, self.start)


    def update(self):

        for ball in self.balls:
            rad = ball.radius
            self.gui.canvas.coords(ball.get_obj(), ball.get_pos_x() - rad, ball.get_pos_y() - rad,
                                   ball.get_pos_x() + rad,
                                   ball.get_pos_y() + rad)

            coords = self.gui.canvas.coords(ball.get_obj())
            if coords[0] <= 0:
                ball.set_spd_x(-ball.get_spd_x())

            elif coords[0] + 2 * rad >= self.width:
                ball.set_spd_x(-abs(ball.get_spd_x()))

            elif coords[1] <= 0:
                ball.set_spd_y(abs(ball.get_spd_y()))

            elif coords[1] + 2 * rad >= self.height:
                ball.set_spd_y(-abs(ball.get_spd_y()))

    def spawn_obj(self):
        for ball in self.balls:
            ball.set_obj(self.gui.canvas.create_oval(ball.pos[0] - ball.radius,
                                                     ball.pos[1] - ball.radius,
                                                     ball.pos[0] + ball.radius,
                                                     ball.pos[1] + ball.radius,
                                                     fill='blue'))

    def step(self):
        self.time += 1

        #     for key in self.balls.keys():
        for ball in self.balls:
            # ball = self.balls.get(key)

            ball.set_pos_x(ball.get_pos_x() + self.gui.curr_speed * self.timestep * ball.get_spd_x())
            ball.set_pos_y(ball.get_pos_y() + self.gui.curr_speed * self.timestep * ball.get_spd_y())


def main():
    sim = Simulation(10)

    # sim.start()


if __name__ == "__main__":
    main()
