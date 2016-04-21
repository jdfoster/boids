from ..controller import ControlBoids
from boids.tests.generate_fixtures import generate_example_settings
import matplotlib
from mock import patch


def test_ControlBoids_init():
    with patch('boids.controller.BuildBoids'), \
         patch('boids.controller.ViewBoids'):
        test_data = generate_example_settings()
        control = ControlBoids(test_data)
        assert(control.boids.update_boids.call_count == 0)
        assert(control.view.update_plt.call_count == 0)
        control.animator(1)
        assert(control.boids.update_boids.call_count == 1)
        assert(control.view.update_plt.call_count == 1)


def test_run_animation():
    with patch('boids.controller.animation.FuncAnimation') \
         as mock_anim:
        test_data = generate_example_settings()
        control = ControlBoids(test_data)
        anim = control.run_animation()
        test_fig, test_animator = mock_anim.call_args[0]
        assert(isinstance(test_fig, matplotlib.figure.Figure))
        assert(test_animator.__name__ == 'animate_boid')
