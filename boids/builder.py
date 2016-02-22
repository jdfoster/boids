from model import Boid, Boids
from boid_exceptions import BoidExceptions
import numpy as np


class BuildBoids(BoidExceptions):
        def __init__(self):
                self.start_boids()

        def start_boids(self):
                self.model = Boids()
                self.location_x_limits = None
                self.location_y_limits = None
                self.velocity_x_limits = None
                self.velocity_y_limits = None
                self.model.avoid_radius = None
                self.model.boid_count = None
                self.model.flock_attraction = None
                self.model.flock_radius = None
                self.model.velocity_matching = None
                self.model.flock = None

        @BoidExceptions.check_xy_limits
        def set_location_ranges(self, x_limits, y_limits):
                self.location_x_limits = x_limits
                self.location_y_limits = y_limits

        @BoidExceptions.check_xy_limits
        def set_velocity_ranges(self, x_limits, y_limits):
                self.velocity_x_limits = x_limits
                self.velocity_y_limits = y_limits

        def set_flock_parameters(self, boid_count, flock_attraction,
                                 avoid_radius, flock_radius,
                                 velocity_matching):
                list_int = [boid_count, avoid_radius, flock_radius]
                list_float = [flock_attraction, velocity_matching]
                param_int = self._list_type_check(list_int, int)
                param_float = self._list_type_check(list_float, float)
                if not param_int:
                        raise TypeError('Flock parameters boid_count, ' +
                                        'avoid_radius and flock_radius ' +
                                        'should be integer values')
                if not param_float:
                        raise TypeError('Flock parameters flock_attraction ' +
                                        'and velocity_matching should be ' +
                                        'floating point values')
                self.model.boid_count = boid_count
                self.model.avoid_radius = avoid_radius
                self.model.flock_attraction = flock_attraction / boid_count
                self.model.flock_radius = flock_radius
                self.model.velocity_matching = velocity_matching / boid_count

        def generate_boids(self):
                self.model.flock = [
                        Boid(np.random.uniform(*self.location_x_limits),
                             np.random.uniform(*self.location_y_limits),
                             np.random.uniform(*self.velocity_x_limits),
                             np.random.uniform(*self.velocity_y_limits),
                             self.model)
                        for x in range(self.model.boid_count)]

        def generate_from_file(self, file_data):
                self.model.flock = [Boid(x, y, xv, yv, self.model) for
                                    x, y, xv, yv in zip(*file_data)]

        def validate(self):
                assert(len(self.model.flock) == self.model.boid_count)
                assert(self.model.avoid_radius is not None)
                assert(self.model.flock_attraction is not None)
                assert(self.model.flock_radius is not None)
                assert(self.model.velocity_matching is not None)

        def finish(self):
                self.validate()
                return self.model
