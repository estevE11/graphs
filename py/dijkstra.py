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
    pq = [Node(start, 0, [])]
    visited = []
    while pq[0].val != target:
        visited.append(pq[0].val)
        add_neigbours(pq, pq.pop(0), graph, visited)
        pq.sort(key=lambda x: x.cost)

    return pq[0]

def add_neigbours(pq, node, graph, visited):
    for nd in graph[node.val]:
        if nd[0] not in visited:
            pq.append(Node(nd[0], node.cost + nd[1], node.combine_trace()))
    return pq

class Node():
    def __init__(self, val: int, cost: int, trace: list):
        self.val = val
        self.cost = cost
        self.trace = trace

    def combine_trace(self):
        new_trace = self.trace.copy()
        new_trace.append(self.val)
        return new_trace

if __name__ == "__main__":
    main()