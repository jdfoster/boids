from argparse import ArgumentParser, Action, RawDescriptionHelpFormatter


class ParseBoids(object):
    def __init__(self):
        self.text_main = ('') 
        self.text_epi = ('')
        self.text_movie = ('')
        self.text_config = ('')
        self.text_save = ('')

    def entry_point(self):
        parser = ArgumentParser(description = self.text_main,
                                epilog = self.text_epi)
        parser.add_argument('--movie', '-m', type = str,
                            help = self.text_movie)
        parser.add_argument('--config', '-c',  type = str,
                            help = self.text_config)
        parser.add_argument('--save', '-s', type = str,
                            help = self.text_save)
        self.arguments = parser.parse_args()


if __name__ == "__main__":
    boidpar = ParseBoids()
    boidpar.entry_point()
