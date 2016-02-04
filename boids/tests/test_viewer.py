from ..viewer import ViewBoids
from mock import patch, MagicMock
import numpy as np


def test_ViewBoids():
    mock_boids = MagicMock()
    mock_boids.boundary_x_limits = [20, 80]
    mock_boids.boundary_y_limits = [-100, -50]
    test_array = np.array([0, 1]) * np.ones(10)[:,np.newaxis]
    mock_boids.current_locations = test_array.copy()
    with patch('boids.viewer.plt') as mock_plt:
        view = ViewBoids(mock_boids)
        mock_plt.axes.assert_called_with(xlim=[20, 80], ylim=[-100, -50])
        view.update_plt()
        called_with = view.scatter.set_offsets.call_args[0][0]
        np.testing.assert_array_equal(called_with, test_array)
