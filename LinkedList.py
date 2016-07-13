# Module:  LinkedList.py


class LinkedList(object):
    """ Definition and methods for a linked list data structure"""

    def __init__(self, head=None):
        self.head = head

    def insert(self, new_node):

        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, name):
        current = self.head
        found = False
        while current and found is False:
            if current.get_name() == name:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list!")
        return current

    @staticmethod
    def list(data_sets):
        # Traversing a particular data set
        target_string = raw_input('Enter the name of the data set you want:  ')

        try:
            target_set = data_sets.search(target_string)
        except ValueError:
            print "Data set not found!"
        else:
            target_set.list()
