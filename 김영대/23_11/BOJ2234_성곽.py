import sys
from collections import deque


def solution_proc():
    """
    Solution Process \n
    When bit-masked wall info given, \n
    the system outputs count of rooms, \n
    max area of rooms and max area by breaking any wall.
    :return: None
    """
    # Get inputs: size of castle(n, m), wall_info
    read = sys.stdin.readline
    n, m = map(int, read().split())
    wall_info = [list(map(int, read().split())) for _ in range(m)]
    # Generate norm vectors: dn, dy, dx
    dn, dy, dx = (1, -1, n, -n), (0, 0, 1, -1), (1, -1, 0, 0)
    # Generate lists: visit_info, parent_info, room_info
    visit_info = [[False for _ in range(n)] for _ in range(m)]
    parent_info = [i for i in range(n * m)]
    room_info = [0 for _ in range(n * m)]

    def convert_node_to_pos(node):
        """
        Convert node to position(y, x).
        :param node: Index of node
        :return: y, x
        """
        return node // n, node % n

    def is_possible_to_seek(start_info, next_info):
        """
        Determine that it is possible to seek.
        :param start_info: Index of start node
        :param next_info: Index of next node
        :return: possible or impossible to seek start node to next node
        """
        (sy, sx), (ny, nx) = \
            convert_node_to_pos(start_info), convert_node_to_pos(next_info)
        if sy == ny:
            if sx > nx and (wall_info[sy][sx] & 0x1):
                return False
            elif sx < nx and (wall_info[sy][sx] & 0x4) >> 2:
                return False
        elif sy > ny and sx == nx and (wall_info[sy][sx] & 0x2) >> 1:
            return False
        elif sy < ny and sx == nx and (wall_info[sy][sx] & 0x8) >> 3:
            return False
        return True

    def is_valid(y, x):
        """
        Determine that it is out of range.
        :param y: y of node to seek
        :param x: x of node to seek
        :return: valid or invalid
        """
        if y >= m or y < 0 or x >= n or x < 0: return False
        return True

    def get_parent_proc(x):
        """
        Seek parent node.
        :param x: Index of node
        :return: Index of root node
        """
        if x == parent_info[x]: return x
        parent_info[x] = get_parent_proc(parent_info[x])
        return parent_info[x]

    def set_parent_proc(a, b):
        """
        Union two node comparing their idx of root node.
        :param a: Index of node
        :param b: Index of node
        :return: None
        """
        parent_a = get_parent_proc(a)
        parent_b = get_parent_proc(b)
        if parent_a < parent_b:
            parent_info[parent_b] = parent_a
        elif parent_a > parent_b:
            parent_info[parent_a] = parent_b

    def bfs_proc(node):
        """
        BFS Process \n
        Count size of room through breadth first seek.
        :param node: Index of start node
        :return: Size of room
        """
        # Initialize size of room
        curr_size = 1
        # Generate a queue
        queue = deque()
        # Initialize queue with start node.
        queue.append(node)
        # While queue is NOT empty.
        while queue:
            # Pop the queue
            start_node = queue.pop()
            sy, sx = convert_node_to_pos(start_node)
            # Seek with 4-direction.
            for k in range(4):
                # Next position
                ny, nx = sy + dy[k], sx + dx[k]
                # Invalid position or sought previous.
                if not is_valid(ny, nx): continue
                if visit_info[ny][nx]: continue
                # Next node
                next_node = start_node + dn[k]
                # If possible to seek, union two nodes.
                if not is_possible_to_seek(start_node, next_node): continue
                set_parent_proc(start_node, next_node)
                # Enqueue for next seek.
                queue.append(next_node)
                # Increase room size.
                curr_size += 1
                # Visit processing is important in BFS.
                visit_info[ny][nx] = True
        return curr_size

    def get_max_room_size_proc():
        """
        First, check every space through brute force. \n
        And get max room size through BFS.
        :return: max size of rooms
        """
        max_room_size = 0
        # Brute force
        for i in range(m):
            for j in range(n):
                if visit_info[i][j]: continue
                visit_info[i][j] = True
                # Get max size of rooms through BFS.
                max_room_size = max(max_room_size, bfs_proc(n * i + j))
        return max_room_size

    def get_room_cnt_proc():
        """
        Get count of all rooms.
        :return: room count
        """
        # Initialize room count.
        room_cnt = 0
        for i in range(m * n):
            # Check same index of root node.
            if i == parent_info[i]: room_cnt += 1
            # Increase room count.
            room_info[parent_info[i]] += 1
        return room_cnt

    def get_new_max_room_size_proc():
        """
        Get max room size by combining other two rooms.
        :return: new max room size
        """
        # Initialize room size.
        new_max_room_size = 0
        for sy in range(m):
            for sx in range(n):
                for k in range(4):
                    ny, nx = sy + dy[k], sx + dx[k]
                    if not is_valid(ny, nx): continue
                    # Index of root node
                    start_parent, next_parent = \
                    get_parent_proc(n * sy + sx), get_parent_proc(n * ny + nx)
                    # If two root node are same, don't need to compare size of rooms.
                    if start_parent == next_parent: continue
                    new_max_room_size = \
                        max(new_max_room_size,\
                            room_info[start_parent] + room_info[next_parent])
        return new_max_room_size

    # Run each process
    max_room_size = get_max_room_size_proc()
    room_cnt = get_room_cnt_proc()
    new_max_room_size = get_new_max_room_size_proc()
    # Print each derives
    print(room_cnt)
    print(max_room_size)
    print(new_max_room_size)


solution_proc()
