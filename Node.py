# 2023-2024 Programacao 2 LTI
# Grupo 3
# 58000 Ana Rita Nicolau
# 62224 André Alexandre

class Node(object):
    """
    Class of Nodes
    """
    
    def __init__(self, name):
        """
        Constructs a Node
        
        Requires:
        name is a string
        Ensures:
        node such that name == self.getName()
        """
        self._name = name

        
    def getName(self):
        """
        Gets the name
        """
        return self._name


    def setName(self,newName):
        """
        Sets self._name new value.

        Requires:
        newName is str
        Ensures:
        self.getName() == newName
        """
        self._name = newName


    def __eq__ (self, otherNode):
        """
        Compares two Node objects attributes.
        
        Requires:
        otherNode is Node object
        Ensures:
        A boolean value obtained from the equality comparison of _name
        attribute of both Node objects
        """
        return self.getName()==otherNode.getName()


    def __lt__(self, otherNode):
        """
        Compares two Node objects attributes.
        
        Requires:
        otherNode is Node object
        Ensures:
        A boolean value obtained from the less than comparison of _name
        attribute of both Node objects by node's name
        """
        return self.getName()<otherNode.getName()
    

    def __str__(self):
        """
        String representation
        """
        return self._name