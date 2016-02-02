from matplotlib import pyplot as plt
from matplotlib import animation
from boids import Boid, Boids, BoidsBuilder


class ViewBoids(object):
    def __init__(self, boids_model):
        self.boids = boids_model
        self.figure = plt.figure()
        axes = plt.axes(xlim=(self.boids.boundary_x_limits),
                        ylim=(self.boids.boundary_y_limits))
        self.scatter = axes.scatter(self.boids.current_locations[:,0],
                                    self.boids.current_locations[:,1])

    def update_plt(self):
        self.scatter.set_offsets(self.boids.current_locations)


class ControllerBoids(object):
    def __init__(self):
        builder = BoidsBuilder()
        builder.set_defaults()
        builder.generate_boids()
        self.boids = builder.finish()
        self.view = ViewBoids(self.boids)
        
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
