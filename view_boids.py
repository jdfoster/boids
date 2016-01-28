from matplotlib import pyplot as plt
from matplotlib import animation
from boids import Boid, Boids


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
