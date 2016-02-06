from builder import BuildBoids
from viewer import ViewBoids
from matplotlib import animation


class ControlBoids(object):
    def __init__(self, settings):
        builder = BuildBoids()
        builder.set_boundary_limits(**settings.pop('boundary_limits'))
        builder.set_location_ranges(**settings.pop('location_range'))
        builder.set_velocity_ranges(**settings.pop('velocity_range'))
        builder.set_flock_parameters(**settings.pop('flock_parameters'))
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
