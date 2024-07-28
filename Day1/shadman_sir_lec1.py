class Graph:
    # class variables
    # V E
    # adjList - list of lists
    def __init__(self,V,E):
        self.V=V
        self.E=E
        self.adjList= list()
        for i in range(V):
            self.adjList.append([])

    def printAdjList(self):
        for i in self.adjList:
            print(i)

    def addEdge(self,u,v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
        
        
graph = Graph(5,6)
graph.printAdjList()

# adding the edges
graph.addEdge(0,4)
graph.addEdge(0,1)
graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(2,3)
graph.addEdge(4,3)

graph.printAdjList()

def bfs(graph,s):
  WHITE = 1
  GREY =  2
  BLACK = 3
  INF = 9999

  # dictionaries for storing vertex properties
  color=dict()
  parent=dict()
  distance=dict()

  for i in range(graph.V):
      color[i]=WHITE
      parent[i]=-1
      distance[i]=INF

  color[s]=GREY
  parent[s]=-1
  distance[s]=0

  queue = list()
  queue.append(s)

  while len(queue)!=0:
      u = queue.pop(0)
      for v in graph.adjList[u]:
          if color[v]==WHITE:
              color[v]=GREY
              distance[v]=distance[u]+1
              parent[v]=u
              queue.append(v)

      color[u]=BLACK

  print(color)
  print(distance)
  print(parent)
  
  bfs(graph,0)