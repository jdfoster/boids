import numpy as np
import os
import yaml


class Boid(object):
        def __init__(self, x, y, xv, yv, host):
                self.location = np.array([x, y])
                self.velocity = np.array([xv, yv])
                self.host = host

        def shift_boid(self, other):
                location_delta = np.array([0., 0.])
                location_separation = other.location - self.location
                sum_of_squares = np.sum(location_separation**2)

                # Fly towards the middle
                location_delta += (location_separation *
                                   self.host.flock_attraction)

                # Fly away from nearby boids
                if sum_of_squares < self.host.avoid_radius:
                        location_delta -= location_separation

                # Try to match speed with nearby boids
                if sum_of_squares < self.host.flock_radius:
                        location_delta += ((other.velocity - self.velocity) *
                                           self.host.velocity_matching)

                return location_delta


class Boids(object):
        def update_boids(self):
                for protagonist in self.flock:
                        location_delta = np.array([0., 0.])

                        for antagonist in self.flock:
                                shift_values = protagonist.shift_boid(
                                        antagonist)
                                location_delta += shift_values

                        # Adjust velocities from interaction
                        protagonist.velocity += location_delta

                        # Move according to velocities
                        protagonist.location += protagonist.velocity

        @property
        def current_locations(self):
                return np.vstack([boid.location for boid in self.flock])


class BoidsBuilder(object):
        def __init__(self):
                self.start_boids()

        def start_boids(self):
                self.model = Boids()
                self.x_location_limits = None
                self.y_location_limits = None
                self.x_velocity_limits = None
                self.y_velocity_limits = None
                self.model.boundary_x_limits = None
                self.model.boundary_y_limits = None
                self.model.avoid_radius = None
                self.model.boid_count = None
                self.model.flock_attraction = None
                self.model.flock_radius = None
                self.model.velocity_matching = None

        def set_defaults(self):
                with open(os.path.join(os.path.dirname(__file__),
                               'boid_config.yml')) as config_file:
                        config = yaml.load(config_file)
                        self.set_boundary_limits(**config.pop(
                                'boundary_limits'))
                        self.set_location_ranges(**config.pop(
                                'location_range'))
                        self.set_velocity_ranges(**config.pop(
                                'velocity_range'))
                        self.set_flock_parameters(**config.pop(
                                'flock_parameters'))

        def set_location_ranges(self, x_limits, y_limits):
                self.x_location_limits = x_limits
                self.y_location_limits = y_limits

        def set_velocity_ranges(self, x_limits, y_limits):
                self.x_velocity_limits = x_limits
                self.y_velocity_limits = y_limits

        def set_boundary_limits(self, x_limits, y_limits):
                self.model.boundary_x_limits = x_limits
                self.model.boundary_y_limits = y_limits

        def set_flock_parameters(self, boid_count, flock_attraction,
                                 avoid_radius, flock_radius,
                                 velocity_matching):
                self.model.boid_count = boid_count
                self.model.avoid_radius = avoid_radius
                self.model.flock_attraction = flock_attraction / boid_count
                self.model.flock_radius = flock_radius
                self.model.velocity_matching = velocity_matching / boid_count

        def generate_boids(self):
                self.model.flock = [
                        Boid(np.random.uniform(*self.x_location_limits),
                             np.random.uniform(*self.y_location_limits),
                             np.random.uniform(*self.x_velocity_limits),
                             np.random.uniform(*self.y_velocity_limits),
                             self.model)
                        for x in range(self.model.boid_count)]

        def generate_from_file(self, file_data):
                self.model.flock = [Boid(x, y, xv, yv, self.model) for
                                    x, y, xv, yv in zip(*file_data)]

        def validate(self):
                assert(len(self.model.flock) == self.model.boid_count)
                assert(self.model.boundary_x_limits is not None)
                assert(self.model.boundary_y_limits is not None)
                assert(self.model.avoid_radius is not None)
                assert(self.model.flock_attraction is not None)
                assert(self.model.flock_radius is not None)
                assert(self.model.velocity_matching is not None)

        def finish(self):
                self.validate()
                return self.model
