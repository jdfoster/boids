class BoidExceptions(object):
    def _list_type_check(self, container, dat_type):
                bool_list = [isinstance(item, dat_type) for item in container]
                return all(bool_list)

    @classmethod
    def check_xy_limits(self, funct):
        def _wrapped_funct(self, *args, **kwargs):

            def _check(self, test_arg):
                try:
                    assert self._list_type_check(test_arg, float)

                except AssertionError:
                    raise TypeError('X-Y limits should be a list with two ' +
                                    'floating point values')

            if len(args) == 2:
                for arg in args:
                    _check(self, arg)

            if len(kwargs) > 0:
                _check(self, kwargs['x_limits'])
                _check(self, kwargs['y_limits'])

            funct(self, *args, **kwargs)
        return _wrapped_funct

    @classmethod
    def check_flock_params(self, funct):
        def _wrapped_funct(self, *args, **kwargs):

            def _check(self, test_arg, dat_type):
                try:
                    assert self._list_type_check(test_arg, dat_type)

                except AssertionError:
                    raise TypeError

            if len(args) == 5:
                list_int = [args[0], args[2], args[3]]
                list_float = [args[1], args[4]]

            if len(kwargs) > 0:
                list_int = [kwargs['boid_count'],
                            kwargs['avoid_radius'],
                            kwargs['flock_radius']]
                list_float = [kwargs['flock_attraction'],
                              kwargs['velocity_matching']]

            _check(self, list_int, int)
            _check(self, list_float, float)
            funct(self, *args, **kwargs)
        return _wrapped_funct
