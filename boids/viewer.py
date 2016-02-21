from matplotlib import pyplot as plt


class ViewBoids(object):
    def __init__(self, boids_model, x_limits, y_limits):
        xlim_float = self._list_type_check(x_limits, float)
        ylim_float = self._list_type_check(y_limits, float)
        if not (xlim_float & ylim_float):
            raise TypeError('Axes limit values should be a list ' +
                            'with two floating point values')
        self.boids = boids_model
        self.figure = plt.figure()
        axes = plt.axes(xlim=(x_limits), ylim=(y_limits))
        axes.tick_params(axis='both', top='off', bottom='off',
                         left='off', right='off', labelbottom='off',
                         labelleft='off')
        self.figure.tight_layout()
        self.scatter = axes.scatter(self.boids.current_locations[:, 0],
                                    self.boids.current_locations[:, 1])

    def update_plt(self):
        self.scatter.set_offsets(self.boids.current_locations)

    def _list_type_check(self, container, dat_type):
                bool_list = [isinstance(item, dat_type) for item in container]
                return all(bool_list)
