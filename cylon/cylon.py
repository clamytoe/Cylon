from collections import MutableSequence


class Cylon(MutableSequence):
    """Provides .next() and .prev() methods

    If you need to traverse your list object in either direction,
    then this is the module to use.
    """
    def __init__(self, items=[]):
        """Initialize object with the list of items that are passed to it"""
        self.items = items
        self._index = 0

    def __getitem__(self, index):
        """Return the item at the index indicated"""
        return self.items[index]

    def __setitem__(self, index, value):
        """Set the value of the object at the specified index"""
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
        info = ''.join([
            self.__class__.__name__, 
            '(', 
            f'items={len(self)} ', 
            f'index={self._index}', 
            ')'
        ])
        return info

    def __str__(self):
        """Return currently selected item"""
        if len(self) > 0:
            return self.items[self._index]
        else:
            return 'empty'
    
    def _next(self):
        """Helper function for next"""
        next = None
        if self._index == len(self) - 1:
            next = 0
        else:
            next = self._index + 1
        return next
    
    def _prev(self):
        """Helper function for previous"""
        prev = None
        if self._index == 0:
            prev = len(self) - 1
        else:
            prev = self._index - 1
        return prev
    
    def stencil(self, count=2):
        """Return a list with the before and after elements 
        
        Count determines how many of each are displayed.
        """
        before = list(range(self._index - count, self._index))
        after = list(range(self._index, self._index + count + 1))
        indexes = before + after
        return [self.items[i] for i in indexes]

    @property
    def next(self):
        """Return the next item in the object"""
        self._index = self._next()
        return self.items[self._index]

    @property
    def prev(self):
        """Return the previous item in the object"""
        self._index = self._prev()
        return self.items[self._index]

    @property
    def current(self):
        """Return the current item"""
        return self.items[self._index] if self.items else None
    
    @property
    def show_next(self):
        """Display the next item without changing current"""
        return self.items[self._next()]
    
    @property
    def show_prev(self):
        """Display the previous item without changing current"""
        return self.items[self._prev()]
