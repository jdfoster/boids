from boids import update_boids, generate_boids, shift_boid
from nose.tools import assert_almost_equal, assert_equal, assert_less, assert_greater
import os
import yaml


def test_bad_boids_regression():
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boid_data = regression_data["before"]
    update_boids(boid_data)
    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)


def test_generate_boids():
    xs, ys, xvs, yvs = generate_boids(50)
    assert_equal(len(xs), 50)
    for x_value in xs:
        assert_less(x_value, 50)
        assert_greater(x_value, -450)
    for y_value in ys:
        assert_less(y_value, 600)
        assert_greater(y_value, 300)
    for xv_value in xvs:
        assert_less(xv_value, 10)
        assert_greater(xv_value, 0)
    for yv_value in yvs:
        assert_less(yv_value, 20)
        assert_greater(yv_value, -20)


def test_shift_boid_flock_centering():
    # Uses default global values for flock centring
    assert_equal(shift_boid(0, 0, 0, 0, 8, 8, 50, 50), [0.1266, 0.1266])


def test_shift_boid_collision_avoidance():
    # Uses default global values for collision avoidance
    assert_equal(shift_boid(0, 0, 0, 0, 4, 4, 50, 50), [-3.8742, -3.8742])


def test_shift_boid_velocity_matching():
    # Uses default global values for velocity matching
    assert_equal(shift_boid(0, 0, 0, 0, 80, 80, 50, 50), [0.016, 0.016])
