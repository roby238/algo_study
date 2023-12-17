import sys
import math


def solution_proc():
    """
    Get combination of nodes and determinate the minimum distance.
    :return:
    """
    # Get inputs and set variables.
    read = sys.stdin.readline
    n, m = map(int, read().split())
    god_info = [list(map(int, read().split())) for _ in range(n)]
    connect_info = [list(map(int, read().split())) for _ in range(m)]
    parent = [i for i in range(n + 1)]
    graph = []

    def get_parent(x):
        """
        Get root node of any node.
        :param x: a node
        :return:
        """
        if x == parent[x]: return x
        parent[x] = get_parent(parent[x])
        return parent[x]

    def set_parent(a, b):
        """
        Set root node to be same that if they have different parent.
        :param a: node a
        :param b: node b
        :return:
        """
        parent_a = get_parent(a)
        parent_b = get_parent(b)
        if parent_a > parent_b:
            parent[parent_a] = parent_b
        elif parent_a < parent_b:
            parent[parent_b] = parent_a

    def get_dist(a, b):
        """
        Get root node of any node.
        :param a:
        :param b:
        :return:
        """
        return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    # Set parent of nodes.
    for i in range(m):
        set_parent(connect_info[i][0], connect_info[i][1])

    # Get combination between nodes of graph.
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            graph.append((i, j, get_dist(god_info[i - 1], god_info[j - 1])))

    # Sort combinations with distance between two node.
    graph.sort(key= lambda x: x[2])

    dist = 0
    for node in graph:
        # Determinate that they have same root node or not.
        if get_parent(node[0]) == get_parent(node[1]): continue
        # If not, set parent of nodes.
        set_parent(node[0], node[1])
        # Get minimum distance and sum that.
        dist += node[2]

    # Print the minimum distance.
    print(format(dist, ".2f"))


solution_proc()
