# 2023-2024 Programacao 2 LTI
# Grupo 3
# 58000 Ana Rita Nicolau
# 62224 André Alexandre

import sys
import ast


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
        
        Requires: otherNode is Node object
        Ensures: A boolean value obtained from the equality comparison of
        _name attribute of both Node objects
        """
        return self.getName()==otherNode.getName()


    def __lt__(self, otherNode):
        """
        Compares two Node objects attributes.
        
        Requires: otherNode is Node object
        Ensures: A boolean value obtained from the less than comparison
        of _name attribute of both Node objects by node's name
        """
        return self.getName()<otherNode.getName()
    

    def __str__(self):
        """
        String representation
        """
        return self._name



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
        Gets the destination Node
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
        
        Requires: otherEdge is Edge object
        Ensures: A boolean value obtained from the equality comparison of
        _src, _dest and _time attribute of both Edge objects
        """
        return self.getSource()==otherEdge.getSource() and\
              self.getDestination()==otherEdge.getDestination() and\
              self.getTime()==otherEdge.getTime()


    def __lt__(self, otherEdge):
        """
        Compares two Edge objects attributes.
        
        Requires: otherEdge is Edge object
        Ensures: A boolean value obtained from the less than comparison
        of _time attribute of Edge Node objects by node's name
        """
        return self.getTime()==otherEdge.getTime()


    def __str__(self):
        """
        String representation
        """
        return self._src.getName() + '->' + self._dest.getName()



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
            raise ValueError('Duplicate node')          # TESTAR !!!
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
        getEdges[node] == dest                          TESTAR !!!
        getEdgesInfo[node] == (dest,time)               TESTAR !!!
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
        node belonging to the path (that starts in the node node)   not sure???
        """
        return self._edges[str(node)]

    
    def hasNode(self, node):
        """
        f

        Requires:

        Ensures:
        
        """
        return node in self._nodes


    def __str__(self):
        """
        String representation under the format: A->B                correto???
        """
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src + '->' + dest + '\n'
        return result



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
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

        

def printPath(path):
    """
    String representation of a path
    
    Requires:
    path a list of nodes
    Ensures:
    string whith nodes' names concatenated by '->'
    """
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result



def DFS(graph, start, end, path, shortest, acumulate, solutions):
    """
    Depth first search in a directed graph

    Requires:
    graph is a Digraph;
    start and end are nodes;
    path and shortest are lists of nodes
    acumulate is int
    solutions is dictionary
    Ensures:
    the three fastest paths from start to end in graph
    """
    path = path + [start]
    path = tuple(path)

    if len(path)>1:
        for item in graph._edgesInfo.get(path[len(path)-2]):
            if item[0]==path[len(path)-1]:
                acumulate = acumulate+int(item[1])
        
        if path[-1]==end:
            solutions[path]=acumulate

    path=list(path)
    for node in graph.childrenOf(start):

        if node not in path:

            newPath = DFS(graph, node, end, path, shortest, \
                          acumulate, solutions)[0]
                
            if newPath != None: 
                shortest = newPath

    if len(solutions) > 3:
        solutions = sorted(solutions.items(), key=lambda item: item[1])
        while len(solutions) > 3:
            del solutions[3]
        solutions=dict(solutions)
    
    print(solutions)
    return shortest, solutions



def search(graph, start, end):
    """
    Wrapper function to initialize DFS function

    Requires:
    graph  a Digraph;
    start and end are nodes
    Ensures:
    shortest path from start to end in graph
    """
    return DFS(graph, start, end, [], None, 0, {})



def testSP():
    """
    Function to test search in a graph with a specific example
    """
    
    file=open(sys.argv[1], "r")
    network=[]
    for line in file:
        id=line.rstrip().split(", ")[0]
        name=line.rstrip().split(", ")[1]
        conected=line.rstrip()
        index=conected.index("[")
        conected=conected[index:].replace("),", ");").replace("(", """('""").replace(")", """')""").replace(", ", """', '""").replace(";", ",")
        conected = ast.literal_eval(conected)
        network.append([id, name, conected])
    file.close()

    networkInfo = {}
    for elem in network:
        networkInfo[elem[1]]=elem[0]


    file=open(sys.argv[2], "r")
    connections=[]
    for line in file:
        connections.append(line.rstrip().split(" - "))
    file.close()


    nodes = []
    for id in range(len(network)):
        nodes.append(str(Node(str(network[id][0]))))
        
    g = Digraph()

    for n in nodes:
        g.addNode(n)
    
    for element in network:
        base=element[2]
        for item in base:
            g.addEdge(Edge(element[0],item[0], item[1]))

    file=open(sys.argv[3], "w")
    for element in connections:
        
        if element[0] not in networkInfo or element[1] not in networkInfo:  
            #meter as duas ou só uma?
            file.write("# " + element[0] + " - " + element[1] + "\n")
            if element[0] not in networkInfo:
                file.write(str(element[0]) + " out of the network"  + "\n")
                print(element[0], "out of the network")

            if element[1] not in networkInfo:
                file.write(str(element[1]) + " out of the network"  + "\n")
                print(element[1], "out of the network")

        else:
            sp = search(g, nodes[nodes.index(networkInfo[element[0]])], \
                         nodes[nodes.index(networkInfo[element[1]])])
            info=list(sorted(sp[1].items()))
            
            if info==[]:
                file.write("# " + element[0] + " - " + element[1] + "\n")
                file.write(str(element[0]) + " and " + str(element[1]) + \
                           " do not communicate"  + "\n")
                print(str(element[0]) + " and " + str(element[1]) + \
                      " do not communicate")

            else:
                file.write("# " + element[0] + " - " + element[1] + "\n")
                smallList=[]
                
                for elem in range(0, len(info), 1):
                    smallList.append([info[elem][1], info[elem][0]])

                smallList=sorted(smallList, key=lambda x: x[0])
                for el in range(0, len(smallList), 1):
                    for it in range(0, len(smallList[el][1]), 1):
                        smallList[el].append(smallList[el][1][it])

                    del smallList[el][1]

                    for num in range(1, len(smallList[el]), 1):
                        smallList[el][num]
                        for key, value in networkInfo.items():
                            if smallList[el][num]==value:
                                smallList[el][num]=key
        
                    for ite in range(0, len(smallList[el]),1):
                        if ite==len(smallList[el])-1:
                            file.write(str(smallList[el][ite]))
                        else:
                            file.write(str(smallList[el][ite]) + ", ")
                    file.write(str("\n"))
                
                print('Shortest path found by DFS:', smallList[0])

    file.close()

testSP()