class BoidExceptions(object):
    def _list_type_check(self, container, dat_type):
                bool_list = [isinstance(item, dat_type) for item in container]
                return all(bool_list)
