from boids import update_boids, generate_boids
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
    xs, ys, xvs, yvs = generate_boids()
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
