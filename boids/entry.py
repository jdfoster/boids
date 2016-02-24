from argparse import ArgumentParser, Action, RawDescriptionHelpFormatter
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
        self.text_movie = parse_text['movie']
        self.text_config = parse_text['config']
        self.text_save = parse_text['save']

    def entry_point(self):
        parser = ArgumentParser(description=self.text_main,
                                epilog=self.text_epi)
        parser.add_argument('--movie', '-m', type=str, help=self.text_movie)
        parser.add_argument('--config', '-c',  type=str, help=self.text_config)
        parser.add_argument('--save', '-s', type=str, help=self.text_save)
        self.arguments = parser.parse_args()
        if self.arguments.save is not None:
            self.save_config()
        elif self.arguments.config is not None:
            self.open_config()
        else:
            pass

    def save_config(self):
        try:
            output_file = open(self.arguments.save, 'w')
            output_file.write(yaml.dump(self.settings))
        except IOError:
            pass
        finally:
            output_file.close()

    def open_config(self):
        try:
            expected_keys = set(self.settings.keys())
            input_file = open(self.arguments.config, 'r')
            self.settings = yaml.load(input_file)
            actual_keys = set(self.settings.keys())
            assert expected_keys.issubset(actual_keys)
        except AssertionError:
            raise KeyError('Key(s) missing form given configuration file')
        except AttributeError:
            raise IOError('Incorrectly formatted YAML file')
        except IOError:
            raise IOError('Unable to open given configuration file')
        finally:
            input_file.close()


if __name__ == "__main__":
    boidpar = ParseBoids()
    boidpar.entry_point()
