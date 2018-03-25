from collections import MutableSequence


class Cylon(MutableSequence):
    """Provides .next() and .prev() methods

    If you need to traverse your list object in either direction,
    then this is the module to use.
    """
    def __init__(self, items=[], *args, **kwargs):
        """Initialize object with the list of items that are passed to it"""
        self.items = items if items else list(*args, **kwargs)
        self._current = 0

    def __getitem__(self, index):
        """Return the item at the index indicated"""
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __delitem__(self, index):
        """Remove the item at the index indicated"""
        del self.items[index]

    def __len__(self):
        """Return the length of the object"""
        return len(self.items)

    def insert(self, index, value):
        """Insert value/object at the given index"""
        self.items.insert(index, value)

    def __repr__(self):
        return f'<Cylon items={len(self)} index={self._current}>'

    def __str__(self):
        """Return currently selected item"""
        if len(self) > 0:
            return self.items[self._current]
        else:
            return 'empty'

    @property
    def current(self):
        """Return the current item"""
        return self.items[self._current] if self.items else None

    def next(self):
        """Return the next item in the object"""
        if self._current == len(self) - 1:
            self._current = 0
        else:
            self._current += 1
        return self.items[self._current]

    def prev(self):
        """Return the previous item in the object"""
        if self._current == 0:
            self._current = len(self) - 1
        else:
            self._current -= 1
        return self.items[self._current]
