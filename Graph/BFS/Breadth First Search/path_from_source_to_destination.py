from Graph import Graph
from collections import defaultdict
def path_source_to_destination(graph,source):
    path=defaultdict(list)
    visited=dict()
    level=dict()
    q=[]
    q.append(source)
    visited[source]=True
    level[source]=0
    while len(q)!=0:
        u=q.pop(0)

        for  v in graph.graph[u]:
            if v not in visited:
                level[v]=level[u]+1
                path[u].append(v)
                q.append(v)
                visited[v]=True
    
    print(path)
    print(level)
    return path,level

if __name__=="__main__":
    graph=Graph()
    graph.add_edge(1,3)
    graph.add_edge(3,1)
    graph.add_edge(0,1)
    graph.add_edge(1,0)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,1)

    graph.print_graph()

    path_source_to_destination(graph,0)