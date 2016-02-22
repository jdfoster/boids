from ..viewer import ViewBoids
from ..builder import BuildBoids
from generate_fixtures import generate_broken_limits, \
    negative_fixture_check
from matplotlib import image as img
from mock import patch, MagicMock
from StringIO import StringIO
import numpy as np
import os
import yaml


def test_ViewBoids():
    mock_boids = MagicMock()
    x_limits = [20., 80.]
    y_limits = [-100., -50.]
    test_array = np.array([0, 1]) * np.ones(10)[:, np.newaxis]
    mock_boids.current_locations = test_array.copy()
    with patch('boids.viewer.plt') as mock_plt:
        view = ViewBoids(mock_boids, x_limits, y_limits)
        mock_plt.axes.assert_called_with(xlim=[20., 80.], ylim=[-100., -50.])
        view.update_plt()
        called_with = view.scatter.set_offsets.call_args[0][0]
        np.testing.assert_array_equal(called_with, test_array)


def compare_view_generated_plot(view_obj, test_image):
    buffer = StringIO()
    view_obj.figure.savefig(buffer)
    actual_array = img.imread(StringIO(buffer.getvalue()))
    test_array = img.imread(test_image)
    np.testing.assert_almost_equal(actual_array, test_array)


def test_plot_comparison():
    with open(os.path.join(os.path.dirname(__file__), 'fixtures',
                           'fixture.yml'), 'r') as fixture_file, \
    open(os.path.join(os.path.dirname(__file__), 'fixtures',
                      'first.png'), 'r') as first_image, \
    open(os.path.join(os.path.dirname(__file__), 'fixtures',
                      'second.png'), 'r') as second_image:
        builder = BuildBoids()
        builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
        regression_data = yaml.load(fixture_file)
        builder.generate_from_file(regression_data["before"])
        boids = builder.finish()
        view = ViewBoids(boids, [-500., 1500.], [-500., 1500.])
        for test_image in [first_image, second_image]:
            compare_view_generated_plot(view, test_image)
            boids.update_boids()
            view.update_plt()


def test_plot_limits_fail():
    mock_boids = MagicMock()
    test_array = np.array([0, 1]) * np.ones(10)[:, np.newaxis]
    mock_boids.current_locations = test_array.copy()
    fixtures = generate_broken_limits()
    for fixture in fixtures:
        fixture['model'] = mock_boids
    negative_fixture_check(ViewBoids, fixtures,
                           TypeError)
