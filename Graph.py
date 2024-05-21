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
                                                                POR FAZER
        """
        Digraph.addEdge(self, edge)
        #rev = Edge(edge.getDestination(), edge.getSource())
        #Digraph.addEdge(self, rev)                             #nao esta a mudar nada
