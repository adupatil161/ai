graph={'A':set(['B','C']),
       'B':set(['A','D','E']),
       'C':set(['A','F']),
       'D':set(['B']),
       'E':set(['B','F']),
       'F':set(['C','E'])
       }
def dfs(graph,start):
    visited,stack=set(),[start]
    while stack:
        vertex=stack.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex]-visited)
    return visited
print("visited nodes:",dfs(graph,'A'))

def dfs_paths(graph,start,goal):
    stack=[(start,[start])]
    while stack:
        vertex,path=stack.pop(0)
        for next in graph[vertex]-set(path):
            if next==goal:
                yield path+[next]
            else:
                stack.append(( next,path+[next]))

l1=list(dfs_paths(graph,'A','F'))
print(l1)
        

#output
visited nodes: {'C', 'A', 'E', 'D', 'B', 'F'}
[['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
