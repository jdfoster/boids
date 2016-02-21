from ..model import Boids
from copy import copy


def generate_broken_boid_data():
    test_data = {'x': 4.2, 'y': 4.2,
                 'xv': 6.2, 'yv': 6.2,
                 'host': Boids()}
    fixture_list = []
    for key in test_data:
        new_data = copy(test_data)
        replace_item = new_data.pop(key)
        if isinstance(replace_item, float):
            new_data[key] = int(replace_item)
        if type(replace_item).__name__ == 'Boids':
            new_data[key] = []
        fixture_list.append(new_data)
    return fixture_list


def generate_broken_flock_param():
    test_data = {'boid_count': 2, 'flock_attraction': 4.2,
                 'avoid_radius': 6, 'flock_radius': 8,
                 'velocity_matching': 10.2}
    fixture_list = []
    for key in test_data:
        new_data = copy(test_data)
        replace_item = new_data.pop(key)
        if isinstance(replace_item, float):
            new_data[key] = int(replace_item)
        if isinstance(replace_item, int):
            new_data[key] = float(replace_item)
        fixture_list.append(new_data)
    return fixture_list


def generate_broken_limits():
    test_data = [2.1, 2.2, 4.1, 4.2]
    fixture_list = []
    for index, item in enumerate(test_data):
        new_data = copy(test_data)
        new_data[index] = int(item)
        new_list = {'x_limits':[new_data[0], new_data[1]],
                    'y_limits':[new_data[2], new_data[3]]}
        fixture_list.append(new_list)
    return fixture_list


def generate_example_settings():
    first_nested_data = {'x_limits': [2.1, 4.1], 'y_limits': [6.1, 8.1]}
    second_nested_data = {'boid_count': 2, 'flock_attraction': 4.2,
                          'avoid_radius': 6, 'flock_radius': 8,
                          'velocity_matching': 10.2}
    third_nested_data = {'frames': 50, 'interval': 50}
    test_data = {'boundary_limits': first_nested_data,
                 'location_range': first_nested_data,
                 'velocity_range': first_nested_data,
                 'flock_parameters': second_nested_data,
                 'animation_settings': third_nested_data}
    return test_data
