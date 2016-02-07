from builder import BuildBoids
from viewer import ViewBoids
from matplotlib import animation
from matplotlib import pyplot as plt


class ControlBoids(object):
    def __init__(self, settings):
        self.anim_settings = settings.pop('animation_settings')
        builder = BuildBoids()
        builder.set_location_ranges(**settings.pop('location_range'))
        builder.set_velocity_ranges(**settings.pop('velocity_range'))
        builder.set_flock_parameters(**settings.pop('flock_parameters'))
        builder.generate_boids()
        self.boids = builder.finish()
        self.view = ViewBoids(self.boids, **settings.pop('boundary_limits'))

        def animate_boid(frame_number):
            if frame_number == self.anim_settings['frames'] - 1:
                plt.close()
            else:
                self.boids.update_boids()
                self.view.update_plt()

        self.animator = animate_boid

    def run_animation(self):
        anim = animation.FuncAnimation(self.view.figure, self.animator,
                                       frames=self.anim_settings['frames'],
                                       interval=self.anim_settings['interval'])
        return anim
