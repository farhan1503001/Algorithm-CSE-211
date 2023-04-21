from Graph import Graph

def bicoloring(g,source):
    #First create visited array
    colored=dict()
    q=[]
    q.append(source)
    colored[source]='red'

    while len(q)!=0:
        u=q.pop(0)

        for v in g.graph[u]:
            if v not in colored:
                if colored[u]=='red':
                    colored[v]='blue'
                elif colored[u]=='blue':
                    colored[v]='red'
                q.append(v)
            if colored[u]==colored[v]:
                print("Not Bicolorable")
                return False
            
    print("The graph is bicolorable")
    return True
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
    print(graph.__len__())

    bicoloring(graph,0)
                