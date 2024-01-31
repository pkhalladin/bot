class Example:
    def __init__(self, value):
        self.read_counter = 0
        self.write_counter = 0
        self.value = value

    def __repr__(self):
        return str(self.value)

    @property
    def value(self):
        self.read_counter += 1
        return self._value

    @value.setter
    def value(self, value):
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
        self.write_counter += 1
        self._value = value


class SuperExample(Example):
    def __init__(self, value):
        Example.__init__(self, value)
        print(self._value)


if __name__ == '__main__':
    e = SuperExample(123)
