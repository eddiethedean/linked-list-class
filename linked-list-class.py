class Linked_List:
    def __init__(self, *arg):
        self.nodes = set()
        if len(arg)==0:return
        self.head = self.Node(arg[0])
        self.prev = self.head
        if len(arg)>1:
            for val in arg[1:]:
                new_node = self.Node(val)
                self.nodes.add(new_node)
                if self.prev.next_node==None:
                    self.prev.next_node=new_node
                    self.prev=new_node

    def __getitem__(self, key):
        return self.get(key)

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current!=None:
            result = self.current.value
            self.current = self.current.next_node
            return result
        else:
            raise StopIteration

    def get(self, key):
        for node in self.nodes:
            if node.value == key:
                return node.value

    #TODO Methods to make
    #def add
    #def add_first
    #def add_last
    #def insert_before
    #def delete

    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node
