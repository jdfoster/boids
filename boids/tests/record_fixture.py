from ..builder import BuildBoids
from ..viewer import ViewBoids
import numpy as np
import os
import yaml


def record_regression_fixture():
    with open(os.path.join(os.path.dirname(__file__), 'fixtures',
                           'fixture.yml'), 'w') as fixture_file:
        builder = BuildBoids()
        builder.set_location_ranges([-500, 1500], [-500, 1500])
        builder.set_velocity_ranges([0.0, 10.0], [-20.0, 20.0])
        builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
        builder.generate_boids()
        boids = builder.finish()
        before_array = np.hstack([boids.current_locations,
                                  boids.current_velocities])
        t_before_array = np.transpose(before_array)
        before = tuple(t_before_array.tolist())
        boids.update_boids()
        after_array = np.hstack([boids.current_locations,
                                 boids.current_velocities])
        t_after_array = np.transpose(after_array)
        after = tuple(t_after_array.tolist())
        fixture = {"before": before, "after": after}
        fixture_file.write(yaml.dump(fixture))


def generate_image_fixture():
    with open(os.path.join(os.path.dirname(__file__), 'fixtures',
                           'fixture.yml'), 'r') as fixture_file, \
    open(os.path.join(os.path.dirname(__file__), 'fixtures',
                      'first.png'), 'w') as first_image, \
    open(os.path.join(os.path.dirname(__file__), 'fixtures',
                      'second.png'), 'w') as second_image:
        builder = BuildBoids()
        builder.set_flock_parameters(50, 0.01, 100, 10000, 0.125)
        regression_data = yaml.load(fixture_file)
        builder.generate_from_file(regression_data["before"])
        boids = builder.finish()
        view = ViewBoids(boids, [-500, 1500], [-500, 1500])
        view.figure.savefig(first_image)
        boids.update_boids()
        view.update_plt()
        view.figure.savefig(second_image)
