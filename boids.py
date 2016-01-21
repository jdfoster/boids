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


def update_boids(boids):
        xs, ys, xvs, yvs = boids
        boid_len = len(xs)

        for i in range(boid_len):
                for j in range(boid_len):
                        x_difference = (xs[j] - xs[i])
                        y_difference = (ys[j] - ys[i])
                        # Fly towards the middle
                        xvs[i] += x_difference * flock_attraction
                        yvs[i] += y_difference * flock_attraction

                        # Fly away from nearby boids
                        if x_difference**2 + y_difference**2 < avoid_radius:
                                xvs[i] -= x_difference
                                yvs[i] -= y_difference

                        # Try to match speed with nearby boids
                        if x_difference**2 + y_difference**2 < flock_radius:
                                xvs[i] += (xvs[j] - xvs[i]) * velocity_matching
                                yvs[i] += (yvs[j] - yvs[i]) * velocity_matching

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
