class Cylon:
    def __init__(self, items):
        self.items = items if items else []
        self.index = 0

    def __repr__(self):
        return f'<Cylon items={self.count} index={self.index}>'

    def __str__(self):
        return self.current

    def __next__(self):
        if self.index < self.count - 1:
            self.index += 1
        else:
            self.index = 0
        return self.current

    def __prev__(self):
        if self.index > 0:
            self.index -= 1
        else:
            self.index = self.count - 1
        return self.current

    @property
    def current(self):
        return self.items[self.index]

    @property
    def count(self):
        return len(self.items)

    def next(self):
        return self.__next__()

    def prev(self):
        return self.__prev__()
