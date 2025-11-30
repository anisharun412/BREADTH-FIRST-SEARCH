from collections import deque
from collections import defaultdict


'''
V E
FOR EVERY EDGE
U V
7 9
A B
A C
A F
C E
C F
C D
D E
D G
G F
'''
def bfs(graph,start,visited,path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True
    
    while len(queue) != 0:
        tmpnode = queue.popleft()
        for nbr in sorted(graph[tmpnode]):
            if not visited[nbr]:
                visited[nbr] = True
                path.append(nbr)
                queue.append(nbr)
                
    return path

graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    node_1, node_2 = input().split()
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

start = input()
path = []
visited = defaultdict(bool)
traversedpath = bfs(graph,start,visited,path)
print(traversedpath)
