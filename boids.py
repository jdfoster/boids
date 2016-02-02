from controller import ControlBoids
from matplotlib import pyplot as plt

control = ControlBoids()
boid_animation = control.run_animation()

if __name__ == "__main__":
    plt.show()
