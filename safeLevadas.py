
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
        Digraph such that [] == self.getNodes() and {} == self.getEdges() 
        """
        self._nodes = []
        self._edges = {}
        self._edgesInfo = {}

        
    def addNode(self, node):
        """
        Adds a Node
        
        Requires:
        node is Node not in the digraph yet
        Ensures:
        getNodes() == getNodes()@pre.append(node)
        getEdges[node] == [] 
        """
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(str(node))
            self._edges[str(node)] = []
            self._edgesInfo[str(node)] = []

            
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        time = edge.getTime()

        if not(src in self._nodes and dest in self._nodes):
            raise ValueError(src, dest)
        
        self._edges[src].append(dest)
        self._edgesInfo[src].append((dest, time))

        
    def childrenOf(self, node):
        return self._edges[str(node)]

    
    def hasNode(self, node):
        return node in self._nodes


    def __str__(self):
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src + '->' + dest + '\n'
        return result


class Graph(Digraph):
    def addEdge(self, edge):
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



def DFS(graph, start, end, path, shortest, acumulate, lista):
    """
    Depth first search in a directed graph

    Requires:
    graph a Digraph;
    start and end nodes;
    path and shortest lists of nodes
    Ensures:
    a shortest path from start to end in graph
    """

    path = path + [start]

    if len(path)>1:
        for item in graph._edgesInfo.get(path[len(path)-2]):
            if item[0]==path[len(path)-1]:
                acumulate = acumulate+int(item[1])
        
        if path[-1]==end:
            lista[acumulate]=path

    for node in graph.childrenOf(start):

        if node not in path:

            if shortest == None or len(path)<len(path): 
                newPath = DFS(graph, node, end, path, shortest, acumulate, lista)[0]
                
                if newPath != None: 
                    shortest = newPath

    return shortest, lista



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
        sp = search(g, nodes[nodes.index(networkInfo[element[0]])], nodes[nodes.index(networkInfo[element[1]])])
        info=list(sorted(sp[1].items()))


        count=0
        for itens in info:
            if count==0:
                minLen=100
                maxLen=0
                count=1
            elif len(itens[1])<minLen:
                minLen=len(itens[1])

            elif len(itens[1])>maxLen:
                maxLen=len(itens[1])
            

        file.write("# " + element[0] + " - " + element[1] + "\n")
        smallList=[]
        for item in range(minLen, maxLen+1, 1):
            for elem in range(0, len(info), 1):

                if len(info[elem][1])==item:
                    smallList.append([info[elem][0], info[elem][1]])
                    break
        
        smallList=sorted(smallList, key=lambda x: x[0])
        for el in range(0, len(smallList), 1):
            file.write(str(smallList[el][0]) + ", " + str(smallList[el][1]) + "\n")
            
        print('Shortest path found by DFS:', info[0])

testSP()