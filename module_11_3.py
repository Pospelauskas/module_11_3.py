import inspect
from pprint import pprint


class SomeClassEdu:

    _loc_data = [1, 2, 3, 4, 5, 6, True, False, 'Вектор']

    def __init__(self, param_1, *arg2, **keys):
        self.param_1 = param_1
        self.arg2 = arg2
        self.keys = keys

    def list_data(self):

        print(self.param_1, ' ', self.arg2)

    def some_class_metod(self, value):
        self._loc_data = value
        print(self._loc_data)


def introspection_info(obj):
    obj_info_out = {'Type': type(obj).__name__, 'Module': inspect.getmodule(obj), 'DOC': inspect.getdoc(obj)}
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        obj_info_out[attr_name] = type(attr).__name__
    if inspect.isclass(obj):
        obj_info_out['fullargspec'] = inspect.getfullargspec(victum.list_data)

    return obj_info_out


if __name__ == '__main__':
    victum = SomeClassEdu(4, [23, 23, 23, 32], [True, False])
    number_info = introspection_info(42)
    pprint(number_info)

    obj_info = introspection_info(victum)
    pprint(obj_info)

