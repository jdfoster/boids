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
        def __init__(self, boid_count, flock_attraction, avoid_radius,
                     flock_radius, velocity_matching):
                self.count = boid_count
                self.flock_attraction = flock_attraction / self.count
                self.avoid_radius = avoid_radius
                self.flock_radius = flock_radius
                self.velocity_matching = velocity_matching / self.count

        def generate_boids(self):
                self.flock = [Boid(np.random.uniform(-450.0, 50.0),
                                   np.random.uniform(300.0, 600.0),
                                   np.random.uniform(0.0, 10.0),
                                   np.random.uniform(-20.0, 20.0),
                                   self)
                              for x in range(self.count)]

        def generate_from_file(self, file_data):
                self.flock = [Boid(x, y, xv, yv, self)
                              for x, y, xv, yv in zip(*file_data)]

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
