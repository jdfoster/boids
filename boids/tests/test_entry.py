from ..entry import ParseBoids
from mock import patch
import sys


def test_parseboids_init():
    parseboids = ParseBoids()
    help_text = [parseboids.text_main, parseboids.text_epi,
                 parseboids.text_save, parseboids.text_config,
                 parseboids.text_generate]
    for string in help_text:
        assert isinstance(string, str)


def test_entry_point():
    fixtures = [['--save', 'boids.mp4'], ['-s', 'boids.mp4'],
                ['--config', 'conf.yml'], ['-c', 'conf.yml'],
                ['--generate', 'conf.yml'], ['-g', 'conf.yml'],
                ['-s', 'boids.mp4', '-c', 'conf.yml'],
                ['--save', 'boids.mp4', '--config', 'conf.yml']]
    for fixture in fixtures:
        test_args = ['boids_prog'] + fixture
        with patch.object(sys, 'argv', test_args), \
             patch.object(ParseBoids, 'process_config') as mock_process:
            parseboids = ParseBoids()
            parseboids.entry_point()
            assert mock_process.called
