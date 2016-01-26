from matplotlib import pyplot as plt
from matplotlib import animation
import random


def generate_boids(count):
        boids_x = [random.uniform(-450, 50.0) for x in range(count)]
        boids_y = [random.uniform(300.0, 600.0) for x in range(count)]
        boid_x_velocities = [random.uniform(0, 10.0) for x in range(count)]
        boid_y_velocities = [random.uniform(-20.0, 20.0) for x in range(count)]
        boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)
        return boids


def shift_boid(own_x, own_y, own_xv, own_yv,
               other_x, other_y, other_xv, other_yv):
        x_delta = 0
        y_delta = 0
        x_difference = other_x - own_x
        y_difference = other_y - own_y
        sum_of_squares = x_difference**2 + y_difference**2

        # Fly towards the middle
        x_delta += x_difference * flock_attraction
        y_delta += y_difference * flock_attraction

        # Fly away from nearby boids
        if sum_of_squares < avoid_radius:
                x_delta -= x_difference
                y_delta -= y_difference

        # Try to match speed with nearby boids
        if sum_of_squares < flock_radius:
                x_delta += (other_xv - own_xv) * velocity_matching
                y_delta += (other_yv - own_yv) * velocity_matching

        return [x_delta, y_delta]


def update_boids(boids):
        xs, ys, xvs, yvs = boids
        boid_len = len(xs)

        for i in range(boid_len):
                x_delta = 0
                y_delta = 0

                for j in range(boid_len):
                        shift_values = shift_boid(xs[i], ys[i], xvs[i], yvs[i],
                                                  xs[j], ys[j], xvs[j], yvs[j])
                        x_delta += shift_values[0]
                        y_delta += shift_values[1]

                # Adjust velocities from interaction
                xvs[i] += x_delta
                yvs[i] += y_delta

                # Move according to velocities
                xs[i] += xvs[i]
                ys[i] += yvs[i]


boid_count = 50
flock_attraction = 0.01 / boid_count
avoid_radius = 100
flock_radius = 10000
velocity_matching = 0.125 / boid_count
boundry_limits = [-500, 1500, -500, 1500]
boids = generate_boids(boid_count)
figure = plt.figure()
axes = plt.axes(xlim=(boundry_limits[0], boundry_limits[1]),
                ylim=(boundry_limits[2], boundry_limits[3]))
scatter = axes.scatter(boids[0], boids[1])


def animate(frame):
        update_boids(boids)
        scatter.set_offsets(zip(boids[0], boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)


if __name__ == "__main__":
        plt.show()
