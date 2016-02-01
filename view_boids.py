from matplotlib import pyplot as plt
from matplotlib import animation
from boids import Boid, Boids, BoidsBuilder
import os
import yaml


class ViewBoids(object):
    def __init__(self, boids_model, boundary_limits):
        self.boids = boids_model
        self.boundary_limits = boundary_limits
        self.figure = plt.figure()
        axes = plt.axes(xlim=(self.boundary_limits[0],
                              self.boundary_limits[1]),
                        ylim=(self.boundary_limits[2],
                              self.boundary_limits[3]))
        self.scatter = axes.scatter(self.boids.current_locations[:,0],
                                    self.boids.current_locations[:,1])

    def update_plt(self):
        self.scatter.set_offsets(self.boids.current_locations)


class ControllerBoids(object):
    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__),
                               'boid_config.yml')) as config_file:
            config = yaml.load(config_file)
            boundary_limits = config.pop('boundary_limits')
            builder = BoidsBuilder()
            builder.set_flock_parameters(**config)
            builder.generate_boids()
            self.boids = builder.finish()
            self.view = ViewBoids(self.boids, boundary_limits)
        
        def animate_boid(frame_number):
            self.boids.update_boids()
            self.view.update_plt()

        self.animator = animate_boid

    def run_animation(self):
        anim = animation.FuncAnimation(self.view.figure, self.animator,
                                       frames=50, interval=50)
        return anim

    
controller = ControllerBoids()
boid_animation = controller.run_animation()


if __name__ == "__main__":
    plt.show()
