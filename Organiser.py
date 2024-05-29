# 2023-2024 Programacao 2 LTI
# Grupo 3
# 58000 Ana Rita Nicolau
# 62224 André Alexandre

class Organiser:
    """
    Class of the Organiser
    """
    
    def __init__(self, solutions, path, acumulate, networkInfo):
        """
        Organises the information
        
        Requires:
        solutions is dict which contains path (tuple) as keys and
        their time as values
        path is tuple
        acumulate is int
        networkInfo is dict containing station names as keys and
        their corresponding IDs as values
        Ensures:
        empty Digraph, i.e.
        Digraph such that [] == self.getNodes() and {} == self.getEdges() and
        {} == self.getEdgesInfo()
        """
        self._solutions = solutions
        self._path = path
        self._acumulate = acumulate
        self._networkInfo = networkInfo

        
    def getSolutions(self):
        """
        Gets the solutions
        """
        return self._solutions


    def getPath(self):
        """
        Gets the path
        """
        return self._path
    
    
    def getAcumulate(self):
        """
        Gets the acumulate
        """
        return self._acumulate
    
    
    def getNetworkInfo(self):
        """
        Gets the networkInfo
        """
        return self._networkInfo
    

    def setSolutions(self, newSolutions):
        """
        Sets self._solutions new value.

        Requires:
        newSolutions is dict
        Ensures:
        self.getSolutions() == newSolutions
        """
        self._nodes = newSolutions


    def setPath(self, newPath):
        """
        Sets self._path new value.

        Requires:
        newPath is tuple
        Ensures:
        self.getPath() == newPath
        """
        self._path = newPath


    def setAcumulate(self, newAcumulate):
        """
        Sets self._acumulate new value.

        Requires:
        newAcumulate is int
        Ensures:
        self.getAcumulate() == newAcumulate
        """
        self._acumulate = newAcumulate


    def setNetworkInfo(self, networkInfo):
        """
        Sets self._networkInfo new value.

        Requires:
        newNetworkInfo is dict
        Ensures:
        self.getNetworkInfo() == newNetworkInfo
        """
        self._networkInfo = networkInfo


    def decideBig(self):
        """
        Gets the index of the longest (time) path solution
        """
        newDict=self.getSolutions()
        decideBig = self.organiseFinal()
        newdecideBig = list(reversed(decideBig.items()))
        decideBig= newdecideBig
        bigger = decideBig[0][0]

        count=0
        for element in list(newDict.keys()):
            if bigger == element:
                return count
            count=count+1

    
    def decideAppend(self):
        """
        Maintains the _solutions with its maximum length (3 best solutions)
        """
        newDict=self.getSolutions()
        totalLen = len(newDict)

        if totalLen >=3:
            indexBig=self.decideBig()

            if list(newDict.values())[indexBig] == self.getAcumulate():
                if len(list(newDict.keys())[indexBig]) < len(self.getPath()):
                    del newDict[list(newDict.keys())[indexBig]]
                    newDict[self.getPath()] = self.getAcumulate()

                elif len(list(newDict.keys())[indexBig]) == len(self.getPath()):
                    result = self.organiseAlphabet(indexBig)
                    if result == True:
                        del newDict[list(newDict.keys())[indexBig]]
                        newDict[self.getPath()] = self.getAcumulate()

            elif list(newDict.values())[indexBig] > self.getAcumulate():
                del newDict[list(newDict.keys())[indexBig]]
                newDict[self.getPath()] = self.getAcumulate()

        else:
            newDict[self.getPath()] = self.getAcumulate()

        return newDict
    

    def organiseAlphabet(self, indexBig):
        """
        Organises the list alphabetically

        Requires:
        indexBig is int
        Ensures:
        A boolean value
        """
        infoDict=self.getSolutions()
        netInfo=self.getNetworkInfo()

        list(infoDict.keys())[indexBig][1]

        testList=[list(netInfo.keys())[list(netInfo.values()).index(list(infoDict.keys())[indexBig][1])], list(netInfo.keys())[list(netInfo.values()).index(self.getPath()[1])]]

        testList=sorted(testList, reverse=False)

        if testList[0] == list(netInfo.keys())[list(netInfo.values()).index(list(infoDict.keys())[indexBig][1])]:
            return False
        else:
            return True
        

    def organiseFinal(self):
        """
                                                ???????

        Requires:
        Reverse is a boolean value
        Ensures:
        final dictionary with best solutions (???)
        """
        netInfo=self.getNetworkInfo()
        newDict=self.getSolutions()

        if len(newDict) == 1 or len(newDict)==0:
            return newDict
        
        elif len(newDict) == 2:
            testList={"0":list(netInfo.keys())[list(netInfo.values()).index(list(newDict.keys())[0][1])], "1": list(netInfo.keys())[list(netInfo.values()).index(list(newDict.keys())[1][1])]}

        elif len(newDict) == 3:
            testList={"0":list(netInfo.keys())[list(netInfo.values()).index(list(newDict.keys())[0][1])], "1": list(netInfo.keys())[list(netInfo.values()).index(list(newDict.keys())[1][1])], "2": list(netInfo.keys())[list(netInfo.values()).index(list(newDict.keys())[2][1])]}

        testList=dict(sorted(testList.items(), reverse=False, key=lambda item: item[1]))

        testListNum=list(testList.keys())


        trueDict={}
        for element in testListNum:
            trueDict[list(newDict.items())[int(element)][0]]=list(newDict.items())[int(element)][1]

        newtrueDict = {}
        for item in sorted(trueDict, key=len, reverse=True):
            newtrueDict[item] = trueDict[item]

        trueDict = newtrueDict

        trueDict=dict(sorted(trueDict.items(), key=lambda item: item[1]))

        return trueDict