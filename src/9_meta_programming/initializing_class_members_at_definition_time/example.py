import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields_):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields_ = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields_):
            raise ValueError("{} arguments required".format(len(cls._fields_)))
        return super().__new__(cls, args)


# Examples
class Stock(StructTuple):
    _fields_ = ["name", "shares", "price"]


class Point(StructTuple):
    _fields_ = ["x", "y"]


if __name__ == "__main__":
    s = Stock("ACME", 50, 91.1)
    print("Stock object s:", s)
    print("The first element of Stock object s (name):", s[0])
    print("The name of Stock object s:", s.name)
    print("The total value of Stock object s (shares * price):", s.shares * s.price)

    try:
        s.shares = 23
    except AttributeError as e:
        print(e)
