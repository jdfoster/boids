from builder import BuildBoids
from viewer import ViewBoids
from matplotlib import animation


class ControlBoids(object):
    def __init__(self, settings):
        builder = BuildBoids()
        builder.set_location_ranges(**settings.pop('location_range'))
        builder.set_velocity_ranges(**settings.pop('velocity_range'))
        builder.set_flock_parameters(**settings.pop('flock_parameters'))
        builder.generate_boids()
        self.boids = builder.finish()
        self.view = ViewBoids(self.boids, **settings.pop('boundary_limits'))
        self._set_animation_settings(**settings.pop('animation_settings'))

        def animate_boid(frame_number):
            self.boids.update_boids()
            self.view.update_plt()

        self.animator = animate_boid

    def _set_animation_settings(self, frames, interval):
        anim_settings_integer = [isinstance(frames, int),
                                 isinstance(interval, int)]
        if not all(anim_settings_integer):
            raise TypeError('The animation settings frames and interval ' +
                            'need to be integers')
        self.anim_frames = frames
        self.anim_interval = interval

    def run_animation(self):
        anim = animation.FuncAnimation(self.view.figure, self.animator,
                                       frames=self.anim_frames,
                                       interval=self.anim_interval,
                                       repeat=0)
        return anim
