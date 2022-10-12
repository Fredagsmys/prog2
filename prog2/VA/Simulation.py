import tkinter as tk
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
        pause_entry = ttk.Button(text="Play/Pause", command=lambda: self.gui.paused.set(not self.gui.paused.get()))
        start_entry = ttk.Button(text="Start/Stop", command=lambda: self.gui.started.set(not self.gui.started.get()))
        self.gui.started.set(True)
        self.gui.speed.set(1)
        self.gui.paused.set(False)
        self.gui.balls.set(5)
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


    def play(self):
        self.animate()



    def animate(self):
        if not self.gui.paused.get() and self.gui.started.get(): #if sim is not paused and started
            self.step()
            self.update()
            self.gui.canvas.after(1, self.animate)
        elif self.gui.paused.get(): #if sim is paused
            self.gui.canvas.after(1, self.play)
        else: #if sim is stopped
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


    def clear_obj(self):
        if self.balls is not None:
            for ball in self.balls:
                self.gui.canvas.delete(ball.get_obj())

    def spawn_obj(self):
        rad = 20

        self.balls = [Ball.Ball(radius=rad * (rand.random() + 1),
                                spd_x=1 + rand.random(),
                                spd_y=1 + rand.random(),
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
            # ball = self.balls.get(key)

            ball.set_pos_x(ball.get_pos_x() + self.gui.curr_speed * self.timestep * ball.get_spd_x())
            ball.set_pos_y(ball.get_pos_y() + self.gui.curr_speed * self.timestep * ball.get_spd_y())


def main():
    sim = Simulation()

    # sim.start()


if __name__ == "__main__":
    main()
