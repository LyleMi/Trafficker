class layer(object):
    """docstring for layer"""
    def __init__(self):
        pass

    def pack(self):
        return ''

    def __div__(self, other):
        return self.pack() + other.pack()