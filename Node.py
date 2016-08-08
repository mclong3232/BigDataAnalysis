"""
@package Node.py
Defines a node
"""


class Node(object):
    """
    Definition and methods for a node data structure
    """

    def __init__(self, name=None, id_=None, val=None, next_node=None):
        """
            Initializes a node data structure

            Args:
                name        :string:    a name to uniquely identify the node
                id_         :List:      a list of id numbers
                val         :List:      a list of value numbers
                next_node   :node:      a pointer to a next node

            Returns:
                N/A
        """
        self.name = name
        self.idList = id_
        self.valList = val
        self.next_node = next_node

    def get_name(self):
        """
            Returns the name of a node

            Args:
                N/A

            Returns:
                name    :string:    the name of the node
        """

        return self.name

    def get_next(self):
        """
            Returns the next node;
            None if no next node

            Args:
                N/A

            Returns:
                next_node   :node:  the next node
        """

        return self.next_node

    def set_next(self, new_next):
        """
            Sets the next node

            Args:
                new_next    :node:  the node to become the next_node of the current node

            Returns:
                N/A
        """

        self.next_node = new_next
