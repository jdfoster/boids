class BoidExceptions(object):
    def _map_isinstance(self, container, dat_type):
        def type_check(item):
            return isinstance(item, dat_type)

        bool_logic = [type_check(item) for item in container]
        return all(bool_logic)

    def _check_exception(self, test_funct, er_type):
        try:
            assert test_funct

        except AssertionError:
            raise er_type

    @classmethod
    def _check_xy_limits(self, funct):
        def _wrapped_funct(self, *args, **kwargs):
            er_type = TypeError('X-Y limits should be a list with two ' +
                                'floating point values')
            list_float = None

            if len(args) == 2:
                list_float = args

            elif len(args) == 3:
                list_float = args[1::]

            elif len(kwargs) > 0:
                list_float = [kwargs['x_limits'], kwargs['y_limits']]

            if list_float is not None:
                is_float = all([self._map_isinstance(item, float) for
                                item in list_float])
                is_four = len(sum(list_float, [])) == 4
                is_exception = is_float & is_four
                self._check_exception(is_exception, er_type)

            funct(self, *args, **kwargs)

        return _wrapped_funct

    @classmethod
    def _check_flock_params(self, funct):
        def _wrapped_funct(self, *args, **kwargs):
            int_er_type = TypeError('Flock parameters boid_count, ' +
                                    'avoid_radius and flock_radius ' +
                                    'should be integer values')
            float_er_type = TypeError('Flock parameters flock_attraction ' +
                                      'and velocity_matching should be ' +
                                      'floating point values')
            list_int = None
            list_float = None

            if len(args) == 5:
                list_int = [args[0], args[2], args[3]]
                list_float = [args[1], args[4]]

            elif len(kwargs) == 5:
                list_int = [kwargs['boid_count'],
                            kwargs['avoid_radius'],
                            kwargs['flock_radius']]
                list_float = [kwargs['flock_attraction'],
                              kwargs['velocity_matching']]

            if (list_int is not None) & (list_float is not None):
                is_int = self._map_isinstance(list_int, int)
                is_float = self._map_isinstance(list_float, float)
                self._check_exception(is_int, int_er_type)
                self._check_exception(is_float, float_er_type)

            funct(self, *args, **kwargs)

        return _wrapped_funct

    @classmethod
    def _check_boid_init(self, funct):
        def _wrapped_funct(self, *args, **kwargs):
            vector_er = TypeError('Boid vector values should be ' +
                                  'floating point values')
            host_er = TypeError('The host for the Boid class must ' +
                                'be the Boids class')
            vector_list = None
            host = None

            if len(args) == 5:
                vector_list = args[:-1]
                host = args[-1]

            elif len(kwargs) == 5:
                vector_list = [kwargs['x'], kwargs['y'], kwargs['xv'],
                               kwargs['yv']]
                host = kwargs['host']

            if vector_list is not None:
                is_float = self._map_isinstance(vector_list, float)
                self._check_exception(is_float, vector_er)

            if host is not None:
                host_is_Boids = type(host).__name__ == 'Boids'
                self._check_exception(host_is_Boids, host_er)

            funct(self, *args, **kwargs)

        return _wrapped_funct

    @classmethod
    def _check_set_animation_settings(self, funct):
        def _wrapped_funct(self, *args, **kwargs):
            int_er_type = TypeError('The animation settings frames and ' +
                                    'interval need to be integers')
            list_int = None

            if len(args) == 2:
                list_int = [arg for arg in args]

            if len(kwargs) == 2:
                list_int = [kwargs['frames'], kwargs['interval']]

            if list_int is not None:
                is_int = self._map_isinstance(list_int, int)
                self._check_exception(is_int, int_er_type)

            funct(self, *args, **kwargs)

        return _wrapped_funct
