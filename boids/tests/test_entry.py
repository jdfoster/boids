from ..entry import ParseBoids
from contextlib import contextmanager
from mock import patch, MagicMock
from nose.tools import assert_raises
from StringIO import StringIO
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


@contextmanager
def capture_sys_output():
    capture_out, capture_err = StringIO(), StringIO()
    current_out, current_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = capture_out, capture_err
        yield capture_out, capture_err
    finally:
        sys.stdout, sys.stderr = current_out, current_err


def test_arg_check():
    fixtures = [['--save', '.mp4'], ['-s', '.mp4'], ['-s', 'boids.mp'],
                ['--config', '.yml'], ['-c', '.yml'], ['-c', 'conf.yaml'],
                ['--generate', '.yml'], ['-g', '.yml'], ['-g', 'conf.yaml']]
    for fixture in fixtures:
        test_args = ['boids_prog'] + fixture
        with patch.object(sys, 'argv', test_args), assert_raises(SystemExit), \
             capture_sys_output():
            parseboids = ParseBoids()
            parseboids.entry_point()


def test_process_config():
    fixtures = [{'given': ['conf.yml', None], 'expect': [True, False, False]},
                {'given': ['conf.yml', 'conf.yml'],
                 'expect': [True, False, False]},
                {'given': [None, 'conf.yml'], 'expect': [False, True, True]},
                {'given': [None, None], 'expect': [False, False, True]}]
    for fixture in fixtures:
        gen_config_call, open_config_call, pro_boids_call = fixture['expect']
        mock_args = MagicMock()
        mock_args.generate, mock_args.config = fixture['given']
        with patch.object(ParseBoids, 'generate_config') as gen_config, \
             patch.object(ParseBoids, 'open_config') as open_config, \
             patch.object(ParseBoids, 'process_boids') as pro_boids:
            parseboids = ParseBoids()
            parseboids.arguments = mock_args
            parseboids.process_config()
            assert gen_config.called == gen_config_call
            assert open_config.called == open_config_call
            assert pro_boids.called == pro_boids_call


def test_process_boids():
    with patch('boids.entry.ControlBoids'),  \
         patch('boids.entry.plt.show') as mock_plt_show:
        parseboids = ParseBoids()
        parseboids.arguments = MagicMock()
        parseboids.process_boids()
        assert(mock_plt_show.called is not None)
        parseboids.arguments.save = None
        parseboids.process_boids()
        assert(mock_plt_show.called)
