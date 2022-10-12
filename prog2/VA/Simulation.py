import tkinter as tk

import numpy

import Ball
import random as rand
import tkinter.ttk as ttk


class Simulation:

    def __init__(self):

        self.gui = tk.Tk()
        self.gui.paused = tk.BooleanVar()
        self.gui.started = tk.BooleanVar()
        self.gui.balls = tk.IntVar()
        self.gui.speed = tk.IntVar()
        self.timestep = 1
        self.width = 1000
        self.height = 800
        self.time = 0

        self.gui.canvas = tk.Canvas(self.gui, width=self.width, height=self.height, borderwidth=0, highlightthickness=0,
                                    bg="black")

        speed_entry = ttk.Entry(master=self.gui, textvariable=self.gui.speed)
        balls_entry = ttk.Entry(master=self.gui, textvariable=self.gui.balls)
        pause_entry = ttk.Button(text="Pause/Unpause", command=lambda: self.gui.paused.set(not self.gui.paused.get()))
        start_entry = ttk.Button(text="Start/Stop", command=lambda: self.gui.started.set(not self.gui.started.get()))
        self.gui.started.set(True)
        self.gui.speed.set(1)
        self.gui.paused.set(False)
        self.gui.balls.set(2)
        balls_entry.pack()
        start_entry.pack()
        speed_entry.pack()
        pause_entry.pack()
        self.balls = None

        if self.gui.started.get():
            self.gui.canvas.pack()
            self.start()
        self.gui.canvas.mainloop()

    def start(self):
        if self.gui.started.get():
            self.clear_obj()
            self.spawn_obj()
            self.gui.curr_speed = self.gui.speed.get()
        self.animate()

    def animate(self):
        if not self.gui.paused.get() and self.gui.started.get():  # if sim is started and not paused
            self.update()
            self.step()
            self.gui.canvas.after(1, self.animate)
        elif self.gui.paused.get():  # if sim is paused
            self.gui.canvas.after(1, self.animate)
        else:  # if sim is stopped
            self.gui.canvas.after(1, self.start)

    def update(self):
        for ball in self.balls:
            rad = ball.radius

            self.gui.canvas.coords(ball.get_obj(), ball.get_pos_x() - rad, ball.get_pos_y() - rad,
                                   ball.get_pos_x() + rad,
                                   ball.get_pos_y() + rad)

            rad = ball.radius

            coords = self.gui.canvas.coords(ball.get_obj())

            collision = list(self.gui.canvas.find_overlapping(coords[0], coords[1], coords[2], coords[3]))
            #find which ball is the one in the current loop iteration. Then set that one to ball1. And then we update this balls speed and not the one that ball1 is colliding with.
            if len(collision) == 2:
                updates = []  # assume this will have size 2
                for coll in collision:
                    for update_ball in self.balls:
                        if update_ball.get_obj() == coll:
                            updates.append(update_ball)

                ball1 = updates[0] # change so that ball1 becomes the ball in the current iteration of for ball in self.balls
                ball2 = updates[1]
                print(len(updates))
                print(numpy.dot(numpy.dot(ball2.speed - ball1.speed, ball2.pos - ball1.pos) / (
                        numpy.absolute(ball2.pos - ball1.pos) ** 2), (ball2.pos - ball1.pos)))

                ball1.speed += (numpy.dot(ball2.speed - ball1.speed, ball2.pos - ball1.pos) / (
                        numpy.absolute(ball2.pos - ball1.pos) ** 2)) * (ball2.pos - ball1.pos)
                print("ball1", ball1.speed)
                # ball2.speed += (numpy.dot(ball1.speed - ball2.speed, ball2.pos - ball1.pos) / (
                # numpy.absolute(ball2.pos - ball1.pos) ** 2)) * (ball2.pos - ball1.pos)

            elif coords[0] <= 0:
                ball.set_spd_x(-ball.get_spd_x())

            elif coords[0] + 2 * rad >= self.width:
                ball.set_spd_x(-abs(ball.get_spd_x()))

            elif coords[1] <= 0:
                ball.set_spd_y(abs(ball.get_spd_y()))

            elif coords[1] + 2 * rad >= self.height:
                ball.set_spd_y(-abs(ball.get_spd_y()))

            #            collision.remove(ball.get_obj())
            #            if len(collision) != 0:
            #                for coll in collision:
            #                    self.gui.canvas.delete(coll)
            #                    for delball in self.balls:
            #                        if delball.get_obj() == coll:
            #                            self.balls.remove(delball)



    def clear_obj(self):
        if self.balls is not None:
            for ball in self.balls:
                self.gui.canvas.delete(ball.get_obj())

    def spawn_obj(self):
        rad = 20

        self.balls = [Ball.Ball(radius=rad * (rand.random() + 1),
                                #spd_x=(1 + 4 * rand.random() / 5),
                                #spd_y=(1 + 4 * rand.random() / 5),
                                spd_x=float(1),
                                spd_y=float(1),
                                pos_x=rand.randint(rad, self.width - rad),
                                pos_y=rand.randint(rad, self.height - rad),
                                color='blue') for _ in range(self.gui.balls.get())]
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
            ball.set_pos_x(ball.get_pos_x() + self.gui.curr_speed * self.timestep * ball.get_spd_x())
            ball.set_pos_y(ball.get_pos_y() + self.gui.curr_speed * self.timestep * ball.get_spd_y())


def main():
    sim = Simulation()
    # sim.start()


if __name__ == "__main__":
    main()
