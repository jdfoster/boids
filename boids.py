from matplotlib import pyplot as plt
from matplotlib import animation
import random


class Boid(object):
        def __init__(self, x, y, xv, yv, host):
                self.x = x
                self.y = y
                self.xv = xv
                self.yv = yv
                self.host = host

        def shift_boid(self, other):
                x_delta = 0
                y_delta = 0

                x_difference = other.x - self.x
                y_difference = other.y - self.y
                sum_of_squares = x_difference**2 + y_difference**2

                # Fly towards the middle
                x_delta += x_difference * self.host.flock_attraction
                y_delta += y_difference * self.host.flock_attraction

                # Fly away from nearby boids
                if sum_of_squares < self.host.avoid_radius:
                        x_delta -= x_difference
                        y_delta -= y_difference

                # Try to match speed with nearby boids
                if sum_of_squares < self.host.flock_radius:
                        x_delta += ((other.xv - self.xv) *
                                    self.host.velocity_matching)
                        y_delta += ((other.yv - self.yv) *
                                    self.host.velocity_matching)

                return [x_delta, y_delta]


class Boids(object):
        def __init__(self, boid_count, flock_attraction, avoid_radius,
                     flock_radius, velocity_matching):
                self.count = boid_count
                self.flock_attraction = flock_attraction / self.count
                self.avoid_radius = avoid_radius
                self.flock_radius = flock_radius
                self.velocity_matching = velocity_matching / self.count

        def generate_boids(self):
                self.flock = [Boid(random.uniform(-450, 50.0),
                                   random.uniform(300.0, 600.0),
                                   random.uniform(0, 10.0),
                                   random.uniform(-20.0, 20.0),
                                   self)
                              for x in range(self.count)]

        def generate_from_file(self, file_data):
                self.flock = [Boid(x, y, xv, yv, self) for x, y, xv, yv in
                              zip(*file_data)]

        def update_boids(self):
                for protagonist in self.flock:
                        x_delta = 0
                        y_delta = 0

                        for antagonist in self.flock:
                                shift_values = protagonist.shift_boid(
                                        antagonist)
                                x_delta += shift_values[0]
                                y_delta += shift_values[1]

                        # Adjust velocities from interaction
                        protagonist.xv += x_delta
                        protagonist.yv += y_delta

                        # Move according to velocities
                        protagonist.x += protagonist.xv
                        protagonist.y += protagonist.yv


boid_count = 50
flock_attraction = 0.01
avoid_radius = 100
flock_radius = 10000
velocity_matching = 0.125
boundry_limits = [-500, 1500, -500, 1500]
boids = Boids(boid_count, flock_attraction, avoid_radius, flock_radius,
              velocity_matching)
boids.generate_boids()
figure = plt.figure()
axes = plt.axes(xlim=(boundry_limits[0], boundry_limits[1]),
                ylim=(boundry_limits[2], boundry_limits[3]))
scatter = axes.scatter([bd.x for bd in boids.flock],
                       [bd.y for bd in boids.flock])


def animate(frame):
        boids.update_boids()
        scatter.set_offsets(zip([(bd.x, bd.y) for bd in boids.flock]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)


if __name__ == "__main__":
        plt.show()
