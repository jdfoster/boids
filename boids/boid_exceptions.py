class BoidExceptions(object):
    def _list_type_check(self, container, dat_type):
                bool_list = [isinstance(item, dat_type) for item in container]
                return all(bool_list)

    def _check_exception(self, test_list, dat_type, er_type):
        try:
            assert self._list_type_check(test_list, dat_type)

        except AssertionError:
            raise er_type

    @classmethod
    def check_xy_limits(self, funct):
        def _wrapped_funct(self, *args, **kwargs):
            er_type = TypeError('X-Y limits should be a list with two ' +
                                'floating point values')

            if len(args) == 2:
                for arg in args:
                    self._check_exception(arg, float, er_type)

            if len(kwargs) > 0:
                self._check_exception(kwargs['x_limits'], float, er_type)
                self._check_exception(kwargs['y_limits'], float, er_type)

            funct(self, *args, **kwargs)

        return _wrapped_funct

    @classmethod
    def check_flock_params(self, funct):
        def _wrapped_funct(self, *args, **kwargs):
            int_er_type = TypeError('Flock parameters boid_count, ' +
                                    'avoid_radius and flock_radius ' +
                                    'should be integer values')
            float_er_type = TypeError('Flock parameters flock_attraction ' +
                                      'and velocity_matching should be ' +
                                      'floating point values')

            if len(args) == 5:
                list_int = [args[0], args[2], args[3]]
                list_float = [args[1], args[4]]

            if len(kwargs) > 0:
                list_int = [kwargs['boid_count'],
                            kwargs['avoid_radius'],
                            kwargs['flock_radius']]
                list_float = [kwargs['flock_attraction'],
                              kwargs['velocity_matching']]

            self._check_exception(list_int, int, int_er_type)
            self._check_exception(list_float, float, float_er_type)
            funct(self, *args, **kwargs)

        return _wrapped_funct
