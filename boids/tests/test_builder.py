from ..builder import BuildBoids
from ..model import Boids
from nose.tools import assert_equal, raises
from numpy.testing import assert_array_equal, assert_array_less, assert_raises
from mock import patch, MagicMock
import yaml


def test_generate_boids():
    builder = BuildBoids()
    builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
    builder.set_velocity_ranges([0.0, 10.0], [-20.0, 20.0])
    builder.set_location_ranges([-450.0, 50.0], [300.0, 600.0])
    builder.generate_boids()
    boids = builder.finish()
    assert_equal(len(boids.flock), 50)
    for bd in boids.flock:
        assert_array_less(bd.location, [50, 600])
        assert_array_less([-450, 300], bd.location)
        assert_array_less(bd.velocity, [10, 20])
        assert_array_less([0, -20], bd.velocity)


def test_generate_from_file():
    test_data = [range(4)] * 4
    builder = BuildBoids()
    builder.generate_from_file(test_data)
    assert(len(builder.model.flock) == 4)
    assert(builder.model.current_locations.cumsum()[-1] == 12)


def test_validate():
    builder = BuildBoids()

    @raises(Exception)
    def validate():
        builder.validate()

    validate()  # Fails
    builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
    builder.set_velocity_ranges([0.0, 10.0], [-20.0, 20.0])
    builder.set_location_ranges([-450.0, 50.0], [300.0, 600.0])
    validate()  # Fails
    builder.generate_boids()
    builder.validate()  # Passes


def test_set_location():
    builder = BuildBoids()
    builder.set_location_ranges([2.1, 2.2], [4.1, 4.2])
    assert(builder.location_x_limits == [2.1, 2.2])
    assert(builder.location_y_limits == [4.1, 4.2])


def test_set_velocity():
    builder = BuildBoids()
    builder.set_location_ranges([2.1, 2.2], [4.1, 4.2])
    assert(builder.location_x_limits == [2.1, 2.2])
    assert(builder.location_y_limits == [4.1, 4.2])


def test_set_boundary():
    builder = BuildBoids()
    builder.set_boundary_limits([-2.1, 2.2], [-4.1, 4.2])
    assert(builder.model.boundary_x_limits == [-2.1, 2.2])
    assert(builder.model.boundary_y_limits == [-4.1, 4.2])


def test_set_flock_parameters():
    test_data = {'boid_count': 2, 'flock_attraction': 4,
                 'avoid_radius': 6, 'flock_radius': 8,
                 'velocity_matching': 10}
    builder = BuildBoids()
    builder.set_flock_parameters(**test_data)
    assert(builder.model.boid_count == 2)
    assert(builder.model.flock_attraction == 2)
    assert(builder.model.avoid_radius == 6)
    assert(builder.model.flock_radius == 8)
    assert(builder.model.velocity_matching == 5)


def test_finish():
    builder = BuildBoids()
    builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
    builder.set_velocity_ranges([0.0, 10.0], [-20.0, 20.0])
    builder.set_location_ranges([-450.0, 50.0], [300.0, 600.0])
    builder.generate_boids()
    returned_value = builder.finish()
    assert(isinstance(returned_value, Boids))
    assert(hasattr(returned_value, 'boid_count'))
    assert(hasattr(returned_value, 'flock_attraction'))
    assert(hasattr(returned_value, 'avoid_radius'))
    assert(hasattr(returned_value, 'flock_radius'))
    assert(hasattr(returned_value, 'velocity_matching'))
    assert(hasattr(returned_value, 'flock'))
