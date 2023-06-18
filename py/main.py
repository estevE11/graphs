import dijkstra

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
        path = dijkstra.solve(0, i, g)
        print(path.combine_trace(), path.cost)

if __name__ == "__main__":
    main()