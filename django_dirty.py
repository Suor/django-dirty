from weakref import WeakKeyDictionary

from django.db.models import Model


ORIGINAL_VALUES = WeakKeyDictionary()
ORIGINAL_PROXIES = WeakKeyDictionary()



# def monkey(cls):
#     def decorator(value):
#         func = getattr(value, 'fget', value) # Support properties
#         name = func.__name__
#         setattr(cls, name, value)
#         return value
#     return decorator



EMPTY = object()


# @monkey(Model)
def __setattr__(self, name, value):
    if name != '_state':
        values = ORIGINAL_VALUES.setdefault(self, {})
        if name not in values:
            values[name] = getattr(self, name, EMPTY)
    return super(Model, self).__setattr__(name, value)
Model.__setattr__ = __setattr__


class OriginalProxy(object):
    def __init__(self, real):
        self.__dict__ = ORIGINAL_VALUES.get(real, {})
        self._real = real

    def __getattr__(self, name):
        return getattr(self._real, name)


def _original(self):
    return OriginalProxy(self)
Model._original = property(_original)
