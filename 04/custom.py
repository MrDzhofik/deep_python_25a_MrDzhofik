class CustomMeta(type):
    def __new__(mcs, name, bases, dct):
        new_dct = {}

        for key, value in dct.items():
            if key.startswith('__') and key.endswith('__'):
                new_dct[key] = value
            else:
                new_dct[f'custom_{key}'] = value

        cls_obj = super().__new__(mcs, name, bases, new_dct)

        def custom_setattr(self, name, value):
            if name.startswith('__') and name.endswith('__'):
                real_name = name
            else:
                real_name = f'custom_{name}'
            object.__setattr__(self, real_name, value)

        def custom_getattribute(self, name):
            return object.__getattribute__(self, name)

        cls_obj.__setattr__ = custom_setattr
        cls_obj.__getattribute__ = custom_getattribute

        return cls_obj


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
