# 2023-2024 Programacao 2 LTI
# Grupo 3
# 58000 Ana Rita Nicolau
# 62224 André Alexandre

class Edge(object):
    """
    Class of Edges
    """
    
    def __init__(self, src, dest, time):
        """
        Constructs an Edge
        
        Requires:
        src and dst Nodes
        Ensures:
        Edge such that src == self.getSource() and dest == self.getDestination()
        and time == self.getTime() 
        """
        self._src = src
        self._dest = dest
        self._time = time

        
    def getSource(self):
        """
        Gets the source Node
        """
        return self._src

    
    def getDestination(self):
        """
        Gets the destination Node
        """
        return self._dest
    

    def getTime(self):
        """
        Gets the time associated 
        """
        return self._time
    

    def setSource(self,newSource):
        """
        Sets self._src new value.

        Requires:
        newSource is str
        Ensures:
        self.getSource() == newSource
        """
        self._src = newSource


    def setDestination(self,newDestination):
        """
        Sets self._dest new value.

        Requires:
        newDestination is str
        Ensures:
        self.getDestination() == newDestination
        """
        self._dest = newDestination


    def setTime(self,newTime):
        """
        Sets self._time new value.

        Requires:
        newTime is str
        Ensures:
        self.getTime() == newTime
        """
        self._time = newTime


    def __eq__ (self, otherEdge):
        """
        Compares two Edge objects attributes.
        
        Requires:
        otherEdge is Edge object
        Ensures:
        A boolean value obtained from the equality comparison of
        _src, _dest and _time attribute of both Edge objects
        """
        return self.getSource()==otherEdge.getSource() and\
              self.getDestination()==otherEdge.getDestination() and\
              self.getTime()==otherEdge.getTime()


    def __lt__(self, otherEdge):
        """
        Compares two Edge objects attributes.
        
        Requires:
        otherEdge is Edge object
        Ensures:
        A boolean value obtained from the less than comparison of _time
        attribute of Edge Node objects (by node's name É MESMO ??? )
        """
        return self.getTime()==otherEdge.getTime()


    def __str__(self):
        """
        String representation under the format: A->B   ???
        """
        return self._src.getName() + '->' + self._dest.getName()
