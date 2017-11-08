class Tag:
    __slots__ = ['__name', '__attributes', '__parent', '__previous_sibling', '__next_sibling', '__first_child',
                 '__last_child', '__children']

    def __init__(self, name):
        self.__name = name
        self.__attributes = {}
        self.__parent = None
        self.__previous_sibling = None
        self.__next_sibling = None
        self.__first_child = None
        self.__last_child = None
        self.__children = None

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value

    @parent.deleter
    def parent(self):
        del self.__parent

    @property
    def previous_sibling(self):
        return self.__previous_sibling

    @previous_sibling.setter
    def previous_sibling(self, value):
        self.__previous_sibling = value

    @previous_sibling.deleter
    def previous_sibling(self):
        del self.__previous_sibling

    @property
    def next_sibling(self):
        return self.__next_sibling

    @next_sibling.setter
    def next_sibling(self, value):
        self.__next_sibling = value

    @next_sibling.deleter
    def next_sibling(self):
        del self.__next_sibling

    @property
    def first_child(self):
        return self.__first_child

    @first_child.setter
    def first_child(self, value):
        self.__first_child = value

    @first_child.deleter
    def first_child(self):
        del self.__first_child

    @property
    def last_child(self):
        return self.__last_child

    @last_child.setter
    def last_child(self, value):
        self.__last_child = value

    @last_child.deleter
    def last_child(self):
        del self.__last_child

    @property
    def children(self):
        return self.__parent

    @children.setter
    def children(self, value):
        self.__parent = value

    @children.deleter
    def children(self):
        del self.__parent

    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            return self.__attributes.get(attr)

    def __setattr__(self, name, val):
        try:
            return super().__setattr__(name, val)
        except AttributeError:
            if not self.__attributes.get(name):
                self.__attributes[name] = val

    def __delattr__(self, name):
        try:
            return super().__delattr__(name)
        except AttributeError:
            if not self.__attributes.get(name):
                self.__attributes.pop(name)

    def __str__(self):
        result = '<' + self.__name
        for key, value in self.__attributes.items():
            result += ' ' + key + '="' + value + '"'
        result += '>'
        return result
