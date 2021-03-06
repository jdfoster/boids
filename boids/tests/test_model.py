from ..builder import BuildBoids
from ..model import Boid
from boids.tests.generate_fixtures import generate_broken_boid_data, \
    negative_fixture_check
from nose.tools import assert_almost_equal
from numpy.testing import assert_array_equal
import os
import yaml


def test_bad_boids_regression():
    builder = BuildBoids()
    builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
    regression_data = yaml.load(open(os.path.join(
        os.path.dirname(__file__), 'fixtures', 'fixture.yml')))
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


def test_shift_boid_flock_centering():
    builder = BuildBoids()
    builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
    builder.set_velocity_ranges([0.0, 10.0], [-20.0, 20.0])
    builder.set_location_ranges([-450.0, 50.0], [300.0, 600.0])
    builder.generate_boids()
    boids = builder.finish()
    protagonist = Boid(0., 0., 0., 0., boids)
    antagonist = Boid(8., 8., 50., 50., boids)
    assert_array_equal(protagonist.shift_boid(antagonist),
                       [0.1266, 0.1266])


def test_shift_boid_collision_avoidance():
    builder = BuildBoids()
    builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
    builder.set_velocity_ranges([0.0, 10.0], [-20.0, 20.0])
    builder.set_location_ranges([-450.0, 50.0], [300.0, 600.0])
    builder.generate_boids()
    boids = builder.finish()
    protagonist = Boid(0., 0., 0., 0., boids)
    antagonist = Boid(4., 4., 50., 50., boids)
    assert_array_equal(protagonist.shift_boid(antagonist),
                       [-3.8742, -3.8742])


def test_shift_boid_velocity_matching():
    builder = BuildBoids()
    builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
    builder.set_velocity_ranges([0.0, 10.0], [-20.0, 20.0])
    builder.set_location_ranges([-450.0, 50.0], [300.0, 600.0])
    builder.generate_boids()
    boids = builder.finish()
    protagonist = Boid(0., 0., 0., 0., boids)
    antagonist = Boid(80., 80., 50., 50., boids)
    assert_array_equal(protagonist.shift_boid(antagonist),
                       [0.016, 0.016])


def test_boid_init_fail():
    fixtures = generate_broken_boid_data()
    negative_fixture_check(Boid, fixtures,
                           TypeError)
