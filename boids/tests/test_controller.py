from ..controller import ControlBoids
from mock import patch
import matplotlib


def test_ControlBoids_init():
    with patch('boids.controller.BuildBoids') as mock_build, \
         patch('boids.controller.ViewBoids') as mock_view:
        control = ControlBoids()
        assert(control.boids.update_boids.call_count == 0)
        assert(control.view.update_plt.call_count == 0)
        control.animator(1)
        assert(control.boids.update_boids.call_count == 1)
        assert(control.view.update_plt.call_count == 1)


def test_run_animation():
    with patch('boids.controller.animation.FuncAnimation') \
         as mock_anim:
        control = ControlBoids()
        anim = control.run_animation()
        test_fig, test_animator = mock_anim.call_args[0]
        assert(isinstance(test_fig, matplotlib.figure.Figure))
        assert(test_animator.__name__ == 'animate_boid')
