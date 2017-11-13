class TagException(Exception):
    pass


class ArgumentException(Exception):
    pass


class Tag(object):
    __slots__ = ['_name', '_attributes', '_parent', '_previous_sibling', '_next_sibling', '_first_child',
                 '_last_child', '_children']

    def __init__(self, name, attr=None):
        self._name = name
        if attr is None or not isinstance(attr, dict):
            self._attributes = {}
        else:
            self._attributes = attr
        self._parent = None
        self._previous_sibling = None
        self._next_sibling = None
        self._first_child = None
        self._last_child = None
        self._children = list()
    
    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @parent.deleter
    def parent(self):
        del self._parent

    @property
    def previous_sibling(self):
        return self._previous_sibling

    @previous_sibling.setter
    def previous_sibling(self, value):
        self._previous_sibling = value

    @previous_sibling.deleter
    def previous_sibling(self):
        del self._previous_sibling

    @property
    def next_sibling(self):
        return self._next_sibling

    @next_sibling.setter
    def next_sibling(self, value):
        self._next_sibling = value

    @next_sibling.deleter
    def next_sibling(self):
        del self._next_sibling

    @property
    def first_child(self):
        raise TagException('Not a container tag!')

    @property
    def last_child(self):
        raise TagException('Not a container tag!')

    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            return self._attributes.get(attr)

    def __setattr__(self, name, val):
        try:
            super().__setattr__(name, val)
        except AttributeError:
            self._attributes[name] = val

    def __delattr__(self, name):
        try:
            super().__delattr__(name)
        except AttributeError:
            if self._attributes.get(name):
                self._attributes.pop(name)

    def __str__(self):
        result = '<' + self._name
        for key, value in self._attributes.items():
            result += ' ' + key + '="' + value + '"'
        result += '>'
        return result


class ContainerTag(Tag):
    __slots__ = ['children']

    def __init__(self, name, attr=None):
        super().__init__(name, attr)
        self.children = self.generator_of_children()

    @property
    def first_child(self):
        return self._first_child

    @property
    def last_child(self):
        return self._last_child

    def generator_of_children(self):
        for child in self._children:
            yield child

    def append_child(self, tag):
        if not issubclass(type(tag), Tag):
            raise TypeError("Argument isn't subclass of Tag.")
        self._children.append(tag)
        index_of_last_child = len(self._children) - 1
        self._last_child = self._children[index_of_last_child]
        self._last_child.parent = self
        if len(self._children) == 1:
            self._first_child = self.last_child

    def insert_before(self, tag, next_sibling):
        if not issubclass(type(tag), Tag):
            raise TypeError("Argument isn't subclass of Tag.")
        if next_sibling not in self._children:
            self.append_child(tag)
            return
        index_inserted_elemnt = self._children.index(next_sibling)
        self._children.insert(index_inserted_elemnt, tag)
        index_of_last_child = len(self._children) - 1
        self._last_child = self._children[index_of_last_child]
        self._children[index_inserted_elemnt].parent = self
        if index_inserted_elemnt == 0:
            self._first_child = self._children[index_inserted_elemnt]

    def __str__(self):
        result = '<' + self._name
        for key, value in self._attributes.items():
            result += ' ' + key + '="' + value + '"'
        result += '>'
        for item in self.children:
            result += str(item)
        result += '</' + self._name + '>'
        return result


if __name__ == '__main__':
    img_1 = Tag('img')
    img_1.src = '/python-developer.svg'
    img_1.alt = 'Python Разработчик'

    img_2 = Tag('img')
    img_2.src = '/php-developer.svg'
    img_2.alt = 'PHP Разработчик'

    img_3 = Tag('img')
    img_3.src = '/java-developer.svg'
    img_3.alt = 'Java Разработчик'

    div = ContainerTag('div')
    div.append_child(img_1)
    div.append_child(img_2)
    div.insert_before(img_3, img_1)

    print(div)
