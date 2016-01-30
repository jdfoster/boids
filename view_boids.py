from matplotlib import pyplot as plt
from matplotlib import animation
from boids import Boid, Boids
import os
import yaml


with open(os.path.join(os.path.dirname(__file__), 'boid_config.yml')) \
     as config_file:
    config = yaml.load(config_file)
    boundary_limits = config.pop('boundary_limits')
    boids = Boids(**config)


boids.generate_boids()
figure = plt.figure()
axes = plt.axes(xlim=(boundary_limits[0], boundary_limits[1]),
                ylim=(boundary_limits[2], boundary_limits[3]))
scatter = axes.scatter([bd.location[0] for bd in boids.flock],
                       [bd.location[1] for bd in boids.flock])


def animate(frame):
        boids.update_boids()
        scatter.set_offsets([bd.location for bd in boids.flock])


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)


if __name__ == "__main__":
        plt.show()
