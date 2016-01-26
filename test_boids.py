import boids as bdz
from nose.tools import assert_almost_equal, assert_equal, assert_less, assert_greater
import os
import yaml


def test_bad_boids_regression():
    boids = bdz.Boids(50, 0.01, 100, 10000, 0.125)
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boids.generate_from_file(regression_data["before"])
    boids.update_boids()
    actual_values = (boids.xs, boids.ys, boids.xvs, boids.yvs)
    for after, before in zip(regression_data["after"], actual_values):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)


def test_generate_boids():
    boids = bdz.Boids(50, 0.01, 100, 10000, 0.125)
    boids.generate_boids()
    assert_equal(len(boids.xs), 50)
    for x_value in boids.xs:
        assert_less(x_value, 50)
        assert_greater(x_value, -450)
    for y_value in boids.ys:
        assert_less(y_value, 600)
        assert_greater(y_value, 300)
    for xv_value in boids.xvs:
        assert_less(xv_value, 10)
        assert_greater(xv_value, 0)
    for yv_value in boids.yvs:
        assert_less(yv_value, 20)
        assert_greater(yv_value, -20)


def test_shift_boid_flock_centering():
    # Uses default global values for flock centring
    boids = bdz.Boids(50, 0.01, 100, 10000, 0.125)
    assert_equal(boids.shift_boid(0, 0, 0, 0, 8, 8, 50, 50), [0.1266, 0.1266])


def test_shift_boid_collision_avoidance():
    # Uses default global values for collision avoidance
    boids = bdz.Boids(50, 0.01, 100, 10000, 0.125)
    assert_equal(boids.shift_boid(0, 0, 0, 0, 4, 4, 50, 50), [-3.8742, -3.8742])


def test_shift_boid_velocity_matching():
    # Uses default global values for velocity matching
    boids = bdz.Boids(50, 0.01, 100, 10000, 0.125)
    assert_equal(boids.shift_boid(0, 0, 0, 0, 80, 80, 50, 50), [0.016, 0.016])
