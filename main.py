import sys
from collections import deque


def load_num():
    num_str = sys.stdin.readline()
    if num_str == '\n' or num_str=='':
        return None

    return list(map(int, num_str.rstrip().split()))


def load_graph():
    """Load graph into its adjacency list"""
    vertices = load_num()[0]
   
    # Check it is a valid graph and not the end of the file
    if vertices==0:
        return None

    # Load each edge an construct adjcency  list
    edges = load_num()[0]
   
    adjList = [list() for v in range(vertices)]

    for i in range(edges):
        s, e = load_num()
        adjList[s].append(e)
        adjList[e].append(s)

    return adjList


def is_bicolored(adjList):
    """Use BFS, when the edges of a vertex are processed: 
        * If the vertex found is new assign a color opposite to current.
        * If the vertex was already processed and has same color to current 
        the graph is not bicolored
    """
    vertices = len(adjList)
    
    discovered = [False for x in range(vertices)]
    processed = [False for x in range(vertices)]
    color = [-1 for x in range(vertices)]

    q = deque([0])
    color[0] = 0

    while q:
        v = q.popleft()
        processed[v] = True

        for n in adjList[v]:

            if not discovered[n]:
                discovered[n] = True
                color[n] = 0 if color[v] else 1
                q.append(n)
            elif color[n]==color[v]:
                return False
        

    return True


if __name__ == '__main__':

    while True:
        adj = load_graph()
        if not adj:
            break

        if is_bicolored(adj):
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")

    exit(0)

