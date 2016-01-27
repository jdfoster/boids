import boids as bdz
from nose.tools import assert_almost_equal, assert_equal, assert_less, assert_greater
import os
import yaml


def test_bad_boids_regression():
    boids = bdz.Boids(50, 0.01, 100, 10000, 0.125)
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boids.generate_from_file(regression_data["before"])
    boids.update_boids()
    actual_values = ([bd.x for bd in boids.flock],
                     [bd.y for bd in boids.flock],
                     [bd.xv for bd in boids.flock],
                     [bd.yv for bd in boids.flock])
    for after, before in zip(regression_data["after"], actual_values):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)


def test_generate_boids():
    boids = bdz.Boids(50, 0.01, 100, 10000, 0.125)
    boids.generate_boids()
    assert_equal(len(boids.flock), 50)
    for bd in boids.flock:
        assert_less(bd.x, 50)
        assert_greater(bd.x, -450)
    for bd in boids.flock:
        assert_less(bd.y, 600)
        assert_greater(bd.y, 300)
    for bd in boids.flock:
        assert_less(bd.xv, 10)
        assert_greater(bd.xv, 0)
    for bd in boids.flock:
        assert_less(bd.yv, 20)
        assert_greater(bd.yv, -20)


def test_shift_boid_flock_centering():
    # Uses default global values for flock centring
    boids = bdz.Boids(50, 0.01, 100, 10000, 0.125)
    protagonist = bdz.Boid(0, 0, 0, 0, boids)
    antagonist = bdz.Boid(8, 8, 50, 50, boids)
    assert_equal(protagonist.shift_boid(antagonist), [0.1266, 0.1266])


def test_shift_boid_collision_avoidance():
    # Uses default global values for collision avoidance
    boids = bdz.Boids(50, 0.01, 100, 10000, 0.125)
    protagonist = bdz.Boid(0, 0, 0, 0, boids)
    antagonist = bdz.Boid(4, 4, 50, 50, boids)
    assert_equal(protagonist.shift_boid(antagonist), [-3.8742, -3.8742])


def test_shift_boid_velocity_matching():
    # Uses default global values for velocity matching
    boids = bdz.Boids(50, 0.01, 100, 10000, 0.125)
    protagonist = bdz.Boid(0, 0, 0, 0, boids)
    antagonist = bdz.Boid(80, 80, 50, 50, boids)
    assert_equal(protagonist.shift_boid(antagonist), [0.016, 0.016])
