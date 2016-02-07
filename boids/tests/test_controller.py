from ..controller import ControlBoids
from mock import patch
import matplotlib
from copy import copy


first_nested_data = {'x_limits': [2, 4], 'y_limits': [6, 8]}
second_nested_data = {'boid_count': 2, 'flock_attraction': 4,
                      'avoid_radius': 6, 'flock_radius': 8,
                      'velocity_matching': 10}
third_nested_data = {'frames': 50, 'interval': 50}
test_data = {'boundary_limits': first_nested_data,
             'location_range': first_nested_data,
             'velocity_range': first_nested_data,
             'flock_parameters': second_nested_data,
             'animation_settings': third_nested_data}


def test_ControlBoids_init():
    with patch('boids.controller.BuildBoids') as mock_build, \
         patch('boids.controller.ViewBoids') as mock_view, \
         patch('boids.controller.plt') as mock_plt:
        control = ControlBoids(copy(test_data))
        assert(control.boids.update_boids.call_count == 0)
        assert(control.view.update_plt.call_count == 0)
        control.animator(1)
        assert(control.boids.update_boids.call_count == 1)
        assert(control.view.update_plt.call_count == 1)
        assert(mock_plt.close.call_count == 0)
        control.animator(49)
        assert(control.boids.update_boids.call_count == 1)
        assert(control.view.update_plt.call_count == 1)
        assert(mock_plt.close.call_count == 1)


def test_run_animation():
    with patch('boids.controller.animation.FuncAnimation') \
         as mock_anim:
        control = ControlBoids(copy(test_data))
        anim = control.run_animation()
        test_fig, test_animator = mock_anim.call_args[0]
        assert(isinstance(test_fig, matplotlib.figure.Figure))
        assert(test_animator.__name__ == 'animate_boid')
