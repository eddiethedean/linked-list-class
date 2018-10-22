class LinkedList:
    
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    def __init__(self, *args):
        if len(args) == 0:
            self.head = None
            self.next_node = None
            return
        self.head = self.Node(args[0])
        prev = self.head
        if len(args) > 1:
            for val in args[1:]:
                new_node = self.Node(val)
                prev.next_node = new_node
                prev = new_node

    def __repr__(self):
        return 'LinkedList[' + ','.join([str(x) for x in self]) + ']'

    def __eq__(self, other):
        if len(self) == len(other):
            for s,o in zip(self, other):
                if s != o:return False
            return True
        return False
        
    def __len__(self):
        i = 0
        for _ in self:
            i += 1
        return i

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, end, step = index.start, index.stop, index.step or 1
            return LinkedList(*tuple(self[i] for i in range(start, end,
step)))
        if index < 0:
            last = len(self)
            index = last + index
        for i,value in enumerate(self):
            if i == index:
                return value
        raise IndexError('list index out of range')

    def __delitem__(self, index):
        self.delete(index)

    def __iter__(self):
        self.current = self.head
        return self

    def __reversed__(self):
        return LinkedList(*reversed([x for x in self]))

    def __next__(self):
        if self.current != None:
            result = self.current.value
            self.current = self.current.next_node
            return result
        else:
            raise StopIteration

    def __setitem__(self, index, value):
        self.get_node(index).value = value

    @property
    def nodes(self):
        node = self.head
        for _ in self:
            out = node
            node = node.next_node
            yield out

    def get(self, index, default=None):
        for i,value in enumerate(self):
            if i == index:
                return value
        return default

    def get_node(self, index):
        for i,node in enumerate(self.nodes):
            if i == index:
                return node
        raise IndexError('list index out of range')

    def append(self, value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            return
        for node in self.nodes:
            if node.next_node == None:
                node.next_node = new_node
                return

    def add_first(self, value):
        new_node = self.Node(value, self.head)
        self.head = new_node

    def insert_after(self, value, index):
        new_node = self.Node(value)
        for i,node in enumerate(self.nodes):
            if i == index or node.next_node == None:
                old_node = node.next_node
                node.next_node = new_node
                new_node.next_node = old_node
                break

    def insert_before(self, value, index):
        new_node = self.Node(value)
        if index == 0:
            self.add_first(value)
            return
        prev = self.head
        for i,node in enumerate(self.nodes):
            if i == index:
                new_node.next_node = node
                prev.next_node = new_node
                break
            prev = node

    def insert(self, index, value):
        self.insert_before(value, index)

    def delete(self, index):
        if index == 0:
            self.head = self.head.next_node
            return
        prev = self.head
        for i,node in enumerate(self.nodes):
            if i == index:
                prev.next_node = node.next_node
                return
            prev = node
        raise IndexError('list index out of range')

    def remove(self, value):
        for i,v in enumerate(self):
            if value == v:
                del self[i]
                return
        raise ValueError('LinkedList.remove(x): x not in list')

    def pop(self, index=None):
        for i,node in enumerate(self.nodes):
            if i == index or (index == None and node.next_node == None):
                out = self[i]
                del self[i]
                return out
        if len(self) == 0: raise IndexError('pop from empty list')
        raise IndexError('list index out of range')

    def clear(self):
        self.head = None

    def extend(self, iterable):
        for value in iterable:
            self.append(value)

    def index(self, value, start=0, stop=None):
        for i,v in enumerate(self):
            if i < start:continue
            if v == value:
                return i
            if i == stop:break
        raise ValueError(f'{value} is not in list')

    def count(self, value):
        c = 0
        for v in self:
            if v == value:
                c += 1
        return c

    def sort(self, key=None, reverse=False):
        l = [v for v in self]
        l.sort(key=key, reverse=reverse)
        self.head = LinkedList(*l).head

    def reverse(self):
        l = [v for v in self]
        l.reverse()
        self.head = LinkedList(*l).head

    def copy(self):
        return LinkedList(*[v for v in self])
    