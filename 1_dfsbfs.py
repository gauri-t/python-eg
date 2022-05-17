#DFS BFS
import collections

class Graph:
    #creating a dictionary with {key: value} --> {vertex, set(adjoining vertices)} for graph
    graph = {}

    #initializing garaj nahi ahe
    def __init__(self):
        pass

    #appending the 'graph' (dictionary) in the given form => {key, value} --> {vertex, set(adjoining vertices)}
    def addVertices(self):
        #Taking no. of vertices as input
        n = int(input("Enter number of vertices: "))
        #Basically, pratyek vertex chi adjoining vertices ghet ahot.. so just looping it
        #for every vertex in the graph
        for i in range(n):
            #taking every vertex..
            vertex = int(input("Enter vertex: "))
            #Using map() function and taking the input n splitling them as a set (je aapla decided format hota graph cha..
            #tya form madhe store karayla set(map()) --> map (int, input().split())
            #adj is the set()
            adj = set(map(int,input("Enter adjacent vertices (space separated): ").split()))
            #adding the set of adjoing vertices 'adj' (value of dict) into the graph for the given 'vertex' (key of dict)
            self.graph[vertex] = adj


    #DFS cha logic lavat ahot..
    #Also, function madhe starting point 'start' mhanun ghet ahot, which by default is kept at =1
    def dfs(self, start):
        #creating a set() for visited nodes
        visited = set()
        #tyat apan 'start' vala point add karat ahot
        visited.add(start)
        #creating a stack as a list
        stack = []
        #stack madhe pan aadhi aapan 'start' vertex takat ahot
        stack.append(start)

        #
        while len(stack)>0:
            #pop() removes the last element from the list
            #here, the last element from the 'stack' (list) gets removed but the value is stored in 'x'
            x = stack.pop()
            #printing the values once
            print(x,end=" ")

            #adding all the visited nodes in the set 'visited'
            #set helps in handling duplication and operator overloading of '-' (substraction)
            visited.add(x)

            #so the 'x' chya adjoining vertices chya set madhun aapan visited vertices cha set kadhato
            # so unvis = list( --> graph{x: (adjoining vertices)}  - visited() )
            unvisited = list(self.graph[x] - visited)
            print("unvisited: {} \nvisited: {} \ngraph[x]: {} ".format(unvisited, visited, self.graph[x]))

            #mag aata hya navin unvisited vetices chya list madhe scan karto for vertices who are not there in the list 'stack'
            for node in unvisited:
                if node not in stack:
                    stack.append(node)

    #
    def bfs(self,start):
        #creating a set() for visited nodes
        visited = set()
        #tyat apan 'start' vala point add karat ahot
        visited.add(start)
        #python cha 'collections' module provides for a many advances data structures like deque, counters, user defined -(lists, tuples, dicts)

        #collections.deque -- Doubly Ended Queue --> is optimised for quick append() & pop()
        #Yachi time complex = O(1)
        #whereas regular valyachi is O(n)
        q = collections.deque()
        #aapan deque madhe starting vertex 'start' hi add karto
        q.append(start)

        #
        while q:
            #popleft()  --> popping from left side
            #thus, queue cha principle of 'FIFO --> First In First Out' follow karat ahot
            x = q.popleft()
            #
            print(x,end=" ")
            #
            visited.add(x)
            #
            print("\nvisited: {} \ngraph[x]: {}".format(visited, self.graph[x]))

            # so aata check karat ahot ki adjoining vertices of 'x' madhale sarva aapn append karat ahot visited madhe
            for node in self.graph[x]:
                #
                if node not in visited:
                    #
                    visited.add(node)
                    #deque madhe hi takat ahot so that q doesnt remain empty
                    q.append(node)


g = Graph()
g.addVertices()
print("\nDFS: ")
g.dfs(1)
print("\nBFS: ")
g.bfs(1)
