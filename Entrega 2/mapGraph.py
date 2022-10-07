from subprocess import call
from turtle import st


class Vertex:
    def __init__(self, n, hCost = 0):
        self.streetName = n
        self.visited = False
        self.neighbours = []
        self.parent = None
        self.gCost = float('inf')
        self.hCost = hCost
        self.fCost = float('inf')

    def addNeighbour(self, n, lenght):
        if not n in self.neighbours:
            self.neighbours.append([n, lenght])


class Graph:
    def __init__(self):
        self.vertex = {}

    def addVertex(self, coor):
        if coor not in self.vertex:
            self.vertex[coor] = Vertex(coor)
            #print(f"- Vertex {coor} agregado")

    def addEdge(self, a, b, lenght):
        if a in self.vertex and b in self.vertex:
            self.vertex[a].addNeighbour(b, lenght)
            self.vertex[b].addNeighbour(a, lenght)  
            #print(f"Edge agregado entre {a} y entre {b} con un largo de {lenght}")    

def minList(self, list):
    if len(list) > 0:
        m = self.vertex[list[0].heuristic]
        v = list[0]

        for i in list:
            if m > self.vertex[i].heuristic:
                m = self.vertex[i].heuristic
                v = i
        return v

def lessFCostVertex(self, _open_list):
    if len(_open_list) > 0:
        m = self.vertex[_open_list[0]].fCost
        v = _open_list[0]

        for i in _open_list:
            if m > self.vertex[i].fCost:
                m = self.vertex[i].fCost
                v = i
        return v

def AStar(self, startNode, endNode):
    open_list = [startNode]
    close_list = []
    while len(open_list) > 0:
        startNode = lessFCostVertex(open_list)

def main():
    streetsList = []
    file = open("Files/calles_de_medellin_con_acoso.csv")
    for line in file:
        streetsList.append(line.split(";"))
    mapGraph = Graph()
    for i in range(1,len(streetsList)):       
        mapGraph.addVertex(streetsList[i][1])
        mapGraph.addVertex(streetsList[i][2])
        mapGraph.addEdge(streetsList[i][1], streetsList[i][2], streetsList[i][3])

main()