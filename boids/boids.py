from controller import ControlBoids
from matplotlib import pyplot as plt
import os
import yaml


with open(os.path.join(os.path.dirname(__file__),
                       'boid_config.yml')) as config_file:
    settings = yaml.load(config_file)
    control = ControlBoids(settings)
    boid_animation = control.run_animation()

    
if __name__ == "__main__":
    plt.show()
