from matplotlib import pyplot as plt


class ViewBoids(object):
    def __init__(self, boids_model):
        self.boids = boids_model
        self.figure = plt.figure()
        axes = plt.axes(xlim=(self.boids.boundary_x_limits),
                        ylim=(self.boids.boundary_y_limits))
        self.scatter = axes.scatter(self.boids.current_locations[:,0],
                                    self.boids.current_locations[:,1])

    def update_plt(self):
        self.scatter.set_offsets(self.boids.current_locations)
