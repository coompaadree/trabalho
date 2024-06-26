# 2023-2024 Programacao 2 LTI
# Grupo 3
# 58000 Ana Rita Nicolau
# 62224 André Alexandre

import sys
from Node import Node
from Edge import Edge
from Digraph import Digraph
from Organiser import Organiser

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


def DFS(graph, start, end, networkInfo, path, shortest, acumulate, solutions):
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
            solutions = Organiser(solutions, path, acumulate, networkInfo)
            solutions = solutions.decideAppend()

    path = list(path)
    for node in graph.childrenOf(start):

        if node not in path:

            newPath = DFS(graph, node, end, networkInfo, path, shortest, \
                          acumulate, solutions)[0]
                
            if newPath != None:
                shortest = newPath
    
    solutions = Organiser(solutions, path, acumulate, networkInfo)
    solutions = solutions.organiseFinal()

    return shortest, solutions


def search(graph, start, end, networkInfo):
    """
    Wrapper function to initialize DFS function

    Requires:
    graph  a Digraph;
    start and end are nodes
    Ensures:
    shortest path from start to end in graph
    """
    return DFS(graph, start, end, networkInfo, [], None, 0, {})


def infoFromFiles(filename, type):
    """
    Reads a .txt file

    Requires:
    fileName is str with the name of a .txt file
    type is int
    Ensures:
    2 lists (network and connections), containing other lists inside
    """
    if type == 1:
        file = open(filename, "r")
        network = []
        first = True

        for line in file:
            if first==True:
                first = False
            else:
                id = line.rstrip().split(", ")[0]
                name = line.rstrip().split(", ")[1]
                conected = line.rstrip()
                index = conected.index("[")
                conected = conected[index:].replace("),", ");").replace("(", """('""").replace(")", """')""").replace(", ", """', '""").replace(";", ",")
                conected = eval(conected)
                network.append([id, name, conected])

        file.close()

        total = {}
        totalNum = {}
        totalList = []
        totalListNum = []
        for item in network:
            for elem in item[2]:
                totalList.append(elem[0][0])
                totalListNum.append(elem)
            total[item[0]] = totalList
            totalNum[item[0]] = totalListNum
            totalList = []
            totalListNum = []
        
        for elem in total.items() and totalNum.items():
            for each in elem[1:]:
                for item in each:
                    if elem[0] not in total.get(item[0]):
                        totalNum.get(item[0]).append((elem[0], item[1]))
        
        for lineInfo in network:
            lineInfo[2] = totalNum.get(lineInfo[0])
        return network

    if type == 2:
        file = open(filename, "r")
        connections = []

        for line in file:
            connections.append(line.rstrip().split(" - "))

        file.close()
        return connections
    

def infoToFiles(filename, connections, networkInfo, nodes, g):
    """
    Writes into a .txt file

    Requires:
    filename is str of the output file
    connections is list of lists containing pairs of stations
    networkInfo is dict containing station names as keys and
    their corresponding IDs as values
    nodes is list containg nodes of the graph
    g is Digraph
    Ensures:
    new .txt file
    """
    file = open(filename, "w")
    alreadyOut=False
    for element in connections:
        
        if element[0] not in networkInfo or element[1] not in networkInfo:  
            file.write("# " + element[0] + " - " + element[1] + "\n")
            if element[0] not in networkInfo:
                if element == connections[-1]:
                    file.write(str(element[0]) + " out of the network")
                else:
                    file.write(str(element[0]) + " out of the network"  + "\n")
                alreadyOut=True

            if element[1] not in networkInfo:
                if element == connections[-1]:
                    if alreadyOut==True:
                        file.write("\n" +str(element[1])+ " out of the network")
                    else:
                        file.write(str(element[1]) + " out of the network")
                else:
                    file.write(str(element[1]) + " out of the network"  + "\n")
            alreadyOut=False
            
        else:
            sp = search(g, nodes[nodes.index(networkInfo[element[0]])], \
                    nodes[nodes.index(networkInfo[element[1]])], networkInfo)
            info = list(sp[1].items())
            
            if info==[]:
                file.write("# " + element[0] + " - " + element[1] + "\n")
                if element == connections[-1]:
                    file.write(str(element[0]) + " and " + str(element[1]) + \
                           " do not communicate")
                else:
                    file.write(str(element[0]) + " and " + str(element[1]) + \
                           " do not communicate"  + "\n")

            else:
                file.write("# " + element[0] + " - " + element[1] + "\n")
                smallList = []
                
                for indexInfo in range(0, len(info), 1):
                    smallList.append([info[indexInfo][1], info[indexInfo][0]])

                for indexSmallList in range(0, len(smallList), 1):
                    for connectedSmallList in range(0, len(smallList[indexSmallList][1]), 1):
                        smallList[indexSmallList].append(smallList[indexSmallList][1][connectedSmallList])

                    del smallList[indexSmallList][1]

                    for IDsmallList in range(1, len(smallList[indexSmallList]), 1):
                        smallList[indexSmallList][IDsmallList]
                        for key, value in networkInfo.items():
                            if smallList[indexSmallList][IDsmallList]==value:
                                smallList[indexSmallList][IDsmallList] = key

                for station in range(0, len(smallList), 1):
                    for item in range(0, len(smallList[station]),1):
                        if item==len(smallList[station])-1:
                            file.write(str(smallList[station][item]))
                        else:
                            file.write(str(smallList[station][item]) + ", ")

                    if element != connections[-1]:
                        file.write(str("\n"))
                    elif element==connections[-1] and station!=len(smallList)-1:
                        file.write(str("\n"))
             
    file.close()


def testSP():
    """
    Function to test search in a graph with a specific example
    """
    
    network = infoFromFiles(sys.argv[1], 1)
    connections = infoFromFiles(sys.argv[2], 2)

    networkInfo = {}
    for elem in network:
        networkInfo[elem[1]] = elem[0]

    nodes = []
    for id in range(len(network)):
        nodes.append(str(Node(str(network[id][0]))))
        
    g = Digraph()

    for n in nodes:
        g.addNode(n)
    
    for element in network:
        base = element[2]
        for item in base:
            g.addEdge(Edge(element[0],item[0], item[1]))

    infoToFiles(sys.argv[3], connections, networkInfo, nodes, g)
    
    
testSP()