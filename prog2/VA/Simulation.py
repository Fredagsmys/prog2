import tkinter as tk
import Ball
import random as rand


class Simulation:

    def __init__(self, balls):
        self.started = False
        self.timestep = 1
        self.speed = 1
        self.width = 1000
        self.height = 800
        self.gui = tk.Tk()
        self.canvas = tk.Canvas(self.gui, width=self.width, height=self.height, borderwidth=0, highlightthickness=0,
                                bg="black")

        self.time = 0
        rad = 20
        self.balls = [Ball.Ball(radius=rad * (rand.random() + 1),
                                spd_x=self.speed * (1+rand.random()),
                                spd_y=self.speed * (1+rand.random()),
                                pos_x=rand.randint(rad, self.width - rad),
                                pos_y=rand.randint(rad, self.height - rad),
                                color='blue') for _ in range(balls)]
        self.start()
        self.canvas.mainloop()

    def start(self):
        self.started = True
        self.canvas.grid()

        self.spawn_obj()
        self.animate()
        self.step()

    def animate(self):
        if self.started:
            self.step()
            self.update()
            self.canvas.after(1, self.animate)

    def update(self):

        for ball in self.balls:
            rad = ball.radius
            self.canvas.coords(ball.get_obj(), ball.get_pos_x() - rad, ball.get_pos_y() - rad, ball.get_pos_x() + rad,
                               ball.get_pos_y() + rad)
            coords = self.canvas.coords(ball.get_obj())
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
            ball.set_obj(self.canvas.create_oval(ball.pos[0] - ball.radius,
                                                 ball.pos[1] - ball.radius,
                                                 ball.pos[0] + ball.radius,
                                                 ball.pos[1] + ball.radius,
                                                 fill='blue'))

    def step(self):
        self.time += 1

        #     for key in self.balls.keys():
        for ball in self.balls:
            # ball = self.balls.get(key)
            ball.set_pos_x(ball.get_pos_x() + self.timestep * ball.get_spd_x())
            ball.set_pos_y(ball.get_pos_y() + self.timestep * ball.get_spd_y())


def main():
    sim = Simulation(3)

    # sim.start()


if __name__ == "__main__":
    main()
