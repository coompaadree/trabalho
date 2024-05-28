# 2023-2024 Programacao 2 LTI
# Grupo 3
# 58000 Ana Rita Nicolau
# 62224 André Alexandre

from Digraph import Digraph

class Graph(Digraph):
    """
    Class of Graphs
    """

    def addEdge(self, edge):
        """
        Adds an Edge
        
        Requires:
        edge is Edge not in the graph yet
        Ensures:
        edge is added to the Digragh
        """
        Digraph.addEdge(self, edge)
        #rev = Edge(edge.getDestination(), edge.getSource())
        #Digraph.addEdge(self, rev)                             #nao esta a mudar nada

    def __eq__ (self, otherNode):              # é preciso ???
        """
 
        """
        return


    def __lt__(self, otherNode):              # é preciso ???
        """
        """
        return
    
    def __str__(self):                        # é preciso ???
        """
        """
        return
