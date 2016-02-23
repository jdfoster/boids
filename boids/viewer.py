from boid_exceptions import BoidExceptions
from matplotlib import pyplot as plt


class ViewBoids(BoidExceptions):
    @BoidExceptions._check_xy_limits
    def __init__(self, model, x_limits, y_limits):
        self.model = model
        self.figure = plt.figure()
        axes = plt.axes(xlim=(x_limits), ylim=(y_limits))
        axes.tick_params(axis='both', top='off', bottom='off',
                         left='off', right='off', labelbottom='off',
                         labelleft='off')
        self.figure.tight_layout()
        self.scatter = axes.scatter(self.model.current_locations[:, 0],
                                    self.model.current_locations[:, 1])

    def update_plt(self):
        self.scatter.set_offsets(self.model.current_locations)
