import numpy as np
from boids.boid_exceptions import BoidExceptions


class Boid(BoidExceptions):
    @BoidExceptions._check_boid_init
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
                shift_values = protagonist.shift_boid(antagonist)
                location_delta += shift_values

            # Adjust velocities from interaction
            protagonist.velocity += location_delta

            # Move according to velocities
            protagonist.location += protagonist.velocity

    @property
    def current_locations(self):
        return np.vstack([boid.location for boid in self.flock])

    @property
    def current_velocities(self):
        return np.vstack([boid.velocity for boid in self.flock])
