# Module:  Node.py


class Node(object):
    """ Definition and methods for a node data structure"""

    def __init__(self, name=None, next_node=None):
        self.name = name
        self.idList = []
        self.valList = []
        self.next_node = next_node

    def get_name(self):
        return self.name

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def list(self):
        j = 0

        while j < len(self.idList):
            print self.idList[j], "     ", self.valList[j]
            j += 1
