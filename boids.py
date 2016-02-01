import numpy as np


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
                self.x_location_limit = [-450.0, 50.0]  # Default values
                self.y_location_limit = [300.0, 600.0]  # Default values
                self.x_velocity_limit = [0.0, 10.0]  # Default values
                self.y_velocity_limit = [-20.0, 20.0]  # Default values
                self.model.avoid_radius = None
                self.model.boid_count = None
                self.model.flock_attraction = None
                self.model.flock_radius = None
                self.model.velocity_matching = None

        def set_inital_location_ranges(self, x_limit, y_limit):
                self.x_location_limit = x_limit
                self.y_location_limit = y_limit

        def set_inital_velocity_ranges(self, xv_limit, yv_limit):
                self.x_velocity_limit = xv_limit
                self.y_velocity_limit = yv_limit

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
                        Boid(np.random.uniform(*self.x_location_limit),
                             np.random.uniform(*self.y_location_limit),
                             np.random.uniform(*self.x_velocity_limit),
                             np.random.uniform(*self.y_velocity_limit),
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
