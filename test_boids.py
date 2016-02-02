import boids as bdz
from nose.tools import assert_almost_equal, assert_equal
from numpy.testing import assert_array_equal, assert_array_less
import os
import yaml


def test_bad_boids_regression():
    builder = bdz.BoidsBuilder()
    builder.set_defaults()
    builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
    builder.generate_boids
    regression_data = yaml.load(open(os.path.join(
        os.path.dirname(__file__), 'fixture.yml')))
    builder.generate_from_file(regression_data["before"])
    boids = builder.finish()
    boids.update_boids()
    actual_values = ([bd.location[0] for bd in boids.flock],
                     [bd.location[1] for bd in boids.flock],
                     [bd.velocity[0] for bd in boids.flock],
                     [bd.velocity[1] for bd in boids.flock])
    for after, before in zip(regression_data["after"], actual_values):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)


def test_generate_boids():
    builder = bdz.BoidsBuilder()
    builder.set_defaults()
    builder.set_location_ranges([-450.0, 50.0], [300.0, 600.0])
    builder.set_velocity_ranges([0.0, 10.0], [-20.0, 20.0])
    builder.generate_boids()
    boids = builder.finish()
    assert_equal(len(boids.flock), 50)
    for bd in boids.flock:
        assert_array_less(bd.location, [50, 600])
        assert_array_less([-450, 300], bd.location)
        assert_array_less(bd.velocity, [10, 20])
        assert_array_less([0, -20], bd.velocity)


def test_shift_boid_flock_centering():
    # Uses default global values for flock centring
    builder = bdz.BoidsBuilder()
    builder.set_defaults()
    builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
    builder.generate_boids()
    boids = builder.finish()
    protagonist = bdz.Boid(0, 0, 0, 0, boids)
    antagonist = bdz.Boid(8, 8, 50, 50, boids)
    assert_array_equal(protagonist.shift_boid(antagonist),
                       [0.1266, 0.1266])


def test_shift_boid_collision_avoidance():
    # Uses default global values for collision avoidance
    builder = bdz.BoidsBuilder()
    builder.set_defaults()
    builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
    builder.generate_boids()
    boids = builder.finish()
    protagonist = bdz.Boid(0, 0, 0, 0, boids)
    antagonist = bdz.Boid(4, 4, 50, 50, boids)
    assert_array_equal(protagonist.shift_boid(antagonist),
                       [-3.8742, -3.8742])


def test_shift_boid_velocity_matching():
    # Uses default global values for velocity matching
    builder = bdz.BoidsBuilder()
    builder.set_defaults()
    builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
    builder.generate_boids()
    boids = builder.finish()
    protagonist = bdz.Boid(0, 0, 0, 0, boids)
    antagonist = bdz.Boid(80, 80, 50, 50, boids)
    assert_array_equal(protagonist.shift_boid(antagonist),
                       [0.016, 0.016])
