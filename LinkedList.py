"""
@package LinkedList.py
Defines a linked list
"""


class LinkedList(object):
    """
    Definition and methods for a linked list data structure
    """

    def __init__(self, head=None):
        """
            Initializes a linked list data structure

            Args:
                head :node:  a node pointer to the head

            Returns:
                N/A
        """

        self.head = head

    def insert(self, new_node):
        """
            Inserts a node into the linked list

            Args:
                new_node :node:  a node

            Returns:
                N/A
        """

        if self.head is None:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def size(self):
        """
            Gets the size of the linked list

            Args:
                N/A

            Returns:
                count   :int:   the number of nodes in the linked list
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, name):
        """
            Searches for a specific node in the linked list

            Args:
                name    :string:    the name of the node to find

            Returns:
                current :node:      the node being searched for;
                                    None if not found
        """

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
