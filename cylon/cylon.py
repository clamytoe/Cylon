class Cylon:
    """Provides .next() and .prev() methods

    If you need to traverse your list object in either direction,
    then this is the module to use.
    """
    def __init__(self, items):
        """Initialize object with the list of items that are passed to it"""
        self.items = items
        self._index = 0

    def __repr__(self):
        return f'<Cylon items={self.count} index={self._index}>'

    def __str__(self):
        """Return currently selected item"""
        return self.current

    def __next__(self):
        """Move index to next item and return that item"""
        if self._index < self.count - 1:
            self._index += 1
        else:
            self._index = 0
        return self.current

    def __prev__(self):
        """Move index to previous item and return that item"""
        if self._index > 0:
            self._index -= 1
        else:
            self._index = self.count - 1
        return self.current

    @property
    def current(self):
        """Return the current item"""
        return self.items[self._index]

    @property
    def count(self):
        """Return number of items the object"""
        return len(self.items)

    def next(self):
        """Return the next item in the object"""
        return self.__next__()

    def prev(self):
        """Return the previous item in the object"""
        return self.__prev__()
