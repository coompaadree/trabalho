# 2023-2024 Programacao 2 LTI
# Grupo 3
# 58000 Ana Rita Nicolau
# 62224 André Alexandre

class Digraph(object):
    """
    Class of Directed Graphs
    """

    def __init__(self):
        """
        Constructs a Directed Graph
        
        Ensures:
        empty Digraph, i.e.
        Digraph such that [] == self.getNodes() and {} == self.getEdges() and
        {} == self.getEdgesInfo()
        """
        self._nodes = []
        self._edges = {}
        self._edgesInfo = {}


    def getNodes(self):
        """
        Gets the list of Nodes objects
        """
        return self._nodes
    

    def getEdges(self):
        """
        Gets the dictionary of Edges objects
        """
        return self._edges
    

    def getEdgesInfo(self):
        """
        Gets the dictionary of EdgesInfo
        """
        return self._edgesInfo


    def setNodes(self,newNodes):
        """
        Sets self._nodes new value.

        Requires:
        newNodes is list
        Ensures:
        self.getNodes() == newNodes
        """
        self._nodes = newNodes


    def setEdges(self,newEdges):
        """
        Sets self._edges new value.

        Requires:
        newEdges is dictionary
        Ensures:
        self.getEdges() == newEdges
        """
        self._edges = newEdges


    def setEdgesInfo(self,newEdgesInfo):
        """
        Sets self._edgesInfo new value.

        Requires:
        newEdgesInfo is dictionary
        Ensures:
        self.getEdgesInfo() == newEdgesInfo
        """
        self._edgesInfo = newEdgesInfo


    def addNode(self, node):
        """
        Adds a Node
        
        Requires:
        node is Node not in the digraph yet
        Ensures:
        getNodes() == getNodes()@pre.append(node)
        getEdges[node] == []
        getEdgesInfo[node] == []
        """
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(str(node))
            self._edges[str(node)] = []
            self._edgesInfo[str(node)] = []


    def addEdge(self, edge):
        """
        Adds an Edge and its time
        
        Requires:
        edge is Edge not in the digraph yet
        Ensures:
        getEdges[node] == dest                   a alterar !!! Porquê ?
        getEdgesInfo[node] == (dest,time)        a alterar !!!
        """
        src = edge.getSource()
        dest = edge.getDestination()
        time = edge.getTime()

        if not(src in self._nodes and dest in self._nodes):
            raise ValueError(src, dest)
        
        self._edges[src].append(dest)
        self._edgesInfo[src].append((dest, time))

        
    def childrenOf(self, node):
        """
        Children nodes of node

        Requires:
        node is Node object
        Ensures:
        node belonging to the path (that starts in the node "node")  melhorar ?
        """
        return self._edges[str(node)]


    def __eq__ (self):              # é preciso ???
        """
 
        """
        return


    def __lt__(self):              # é preciso ???
        """
        """
        return


    def __str__(self):
        """
        String representation under the format: A->B  ???  # qt mt acrescentávamos o tempo entre estações
        """
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src + '->' + dest + '\n'
        return result
