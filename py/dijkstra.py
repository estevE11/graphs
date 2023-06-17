def main():
    test_graph1 = [
        [(1, 6), (2, 2)],
        [(4, 4)],
        [(1, 3), (4, 6), (5, 3)],
        [(1, 3)],
        [(3, 3)],
        [(4, 2)]
    ]

    test_graph2 = [
        [(1, 3), (2, 2)],
        [(4, 1)],
        [(1, 3), (4, 2)],
        [(1, 2)],
        [(3, 3)]
    ]

    g = test_graph2
    for i in range(1, len(g)):
        path = solve_dijkstra(0, i, g)
        print(path.combine_trace(), path.cost)

def solve_dijkstra(start, target, graph):
    # init the pq with start node with 0 cost and empty trace
    pq = [Node(start, 0, [])]
    visited = []

    while pq[0].val != target: # do while the fist element of the list is not the target
        curr = pq[0] # get the first node of the list
        pq.pop(0) # delete the first node of the list
        visited.append(curr.val) # add the current node to visited
        add_neigbours(pq, curr, graph, visited) # add the neighbours to pq
        pq = sort(pq) # sort the pq by cost

    return pq[0]

# don't look at this please
def sort(pq):
    res = [pq[0]]
    for i in range(1, len(pq)):
        inserted = False
        for j in range(len(res)):
            if pq[i].cost < res[j].cost:
                res.insert(j, pq[i])
                inserted = True
                break
        if not inserted:
            res.append(pq[i])
    return res 

def add_neigbours(pq, node, graph, visited):
    for nd in graph[node.val]: # loop all the neighbours of the node
        if nd[0] not in visited: # only add if it is not visited
            # append a new node with a combined cost and the parent's trace
            pq.append(Node(nd[0], node.cost+nd[1], node.combine_trace()))
    return pq

class Node():
    def __init__(self, val: int, cost: int, trace: list):
        self.val = val
        self.cost = cost
        self.trace = trace

    # returns a list with it's trace and itself
    def combine_trace(self):
        new_trace = self.trace.copy()
        new_trace.append(self.val)
        return new_trace

if __name__ == "__main__":
    main()