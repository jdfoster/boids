from controller import ControlBoids
from argparse import ArgumentParser
from matplotlib import pyplot as plt
import os
import yaml


class ParseBoids(object):
    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__), 'parser_text.yml')) \
             as text_file, open(os.path.join(os.path.dirname(__file__),
                                             'boids_default_config.yml')) \
             as default_config:
            parse_text = yaml.load(text_file)
            self.settings = yaml.load(default_config)

        self.text_main = parse_text['main']
        self.text_epi = parse_text['epi']
        self.text_save = parse_text['save']
        self.text_config = parse_text['config']
        self.text_generate = parse_text['generate']

    def entry_point(self):
        parser = ArgumentParser(description=self.text_main,
                                epilog=self.text_epi)
        parser.add_argument('--save', '-s', type=str, help=self.text_save)
        parser.add_argument('--config', '-c',  type=str, help=self.text_config)
        parser.add_argument('--generate', '-g', type=str, help=self.text_generate)
        self.arguments = parser.parse_args()
        self.process_config()

    def process_config(self):
        if self.arguments.generate is not None:
            self.generate_config()
        elif self.arguments.config is not None:
            self.open_config()
            self.process_boids()
        else:
            self.process_boids()

    def generate_config(self):
        try:
            config_generate = open(self.arguments.generate, 'w')
            config_generate.write(yaml.dump(self.settings))
            config_generate.close()
        except IOError:
            raise IOError('Unable to write configuration file')

    def open_config(self):
        try:
            expected_keys = set(self.settings.keys())
            config_read = open(self.arguments.config, 'r')
            self.settings = yaml.load(config_read)
            actual_keys = set(self.settings.keys())
            assert expected_keys.issubset(actual_keys)
            config_read.close()
        except AssertionError:
            raise KeyError('Key(s) missing form given configuration file')
        except AttributeError:
            raise IOError('Incorrectly formatted YAML file')
        except IOError:
            raise IOError('Unable to open given configuration file')

    def process_boids(self):
        self.control = ControlBoids(self.settings)
        self.boid_anim = self.control.run_animation()
        if self.arguments.save is not None:
            self.boid_anim.save(self.arguments.save,
                                metadata={'title': 'Boids'})
        else:
            plt.show()


if __name__ == "__main__":
    parseboids = ParseBoids()
    parseboids.entry_point()
