import sys


def solution_proc():
    """
    Solution Process \n
    In this process, read the inputs of system \n
    and check if end_flag is on in the simulation from 0 to k - 1 in super loop.
    :param:
    :return: None
    """
    # Read inputs: n, k, board_color_status, piece_status.
    read = sys.stdin.readline
    n, k = map(int, read().split())
    board_color_status = [list(map(int, read().split())) for _ in range(n)]
    board_piece_status = [[[] for _ in range(n)] for _ in range(n)]
    piece_status = [list(map(int, read().split())) for _ in range(k)]
    # Setting Inputs and preprocessing them.
    for i in range(k):
        y, x, d = piece_status[i]
        # Index starts at 0 in python.
        piece_status[i] = [y - 1, x - 1, d - 1]
        board_piece_status[y - 1][x - 1].append(i)
    # Generate norm vectors along each direction.
    dy, dx = (0, 0, -1, 1), (1, -1, 0, 0)
    # Mapped tuple about reflection.
    reflective = (1, 0, 3, 2)

    def is_valid(y, x):
        """
        Valid Position Check \n
        Determine if the position is out of range.
        :param: int, int
        :return: bool
        """
        if y >= n or y < 0 or x >= n or x < 0: return False
        return True

    def move_with_white_red_proc(idx, ny, nx, sy, sx):
        """
        Move With Only White and Red Area Process \n
        Move a part of list to other list.
        :param: int, int, int, int, int
        :return: int
        """
        # Height initialized.
        height = 0
        # Determine height of current index in the list.
        for i in board_piece_status[sy][sx]:
            if idx == i: break
            height += 1
        # If the area color is white ,
        if not board_color_status[ny][nx]:
            # Get sub list and Connect next list.
            board_piece_status[ny][nx] += board_piece_status[sy][sx][height:]
            # Move the position of list components.
            for i in board_piece_status[sy][sx][height:]:
                piece_status[i] = [ny, nx, piece_status[i][2]]
            # Cut moved components.
            board_piece_status[sy][sx] = board_piece_status[sy][sx][:height]
        # Else if the area color is red ,
        elif board_color_status[ny][nx] == 1:
            # Get sub-reverse list and Connect next list.
            board_piece_status[ny][nx] += board_piece_status[sy][sx][height:][::-1]
            # Move the position of list components.
            for i in board_piece_status[sy][sx][height:]:
                piece_status[i] = [ny, nx, piece_status[i][2]]
            # Cut moved components.
            board_piece_status[sy][sx] = board_piece_status[sy][sx][:height]
        # The floor of current list is over or equal to 4.
        if len(board_piece_status[ny][nx]) >= 4: return -1

    def move_proc(idx):
        """
        Move Process \n
        Move along the area(White, Red, Blue).
        :param: int
        :return: bool
        """
        end_flag = 0
        sy, sx, sd = piece_status[idx]
        ny, nx = sy + dy[sd], sx + dx[sd]
        # Reflective area
        if not is_valid(ny, nx) or board_color_status[ny][nx] == 2:
            piece_status[idx][2] = sd = reflective(sd)
            ny, nx = sy + dy[sd], sx + dx[sd]
            # Non reflective area
            if is_valid(ny, nx) and board_color_status[ny][nx] != 2:
                end_flag = move_with_white_red_proc(idx, ny, nx, sy, sx)
        # Non reflective area
        else:
            end_flag = move_with_white_red_proc(idx, ny, nx, sy, sx)
        # The end_flag in on.
        if end_flag: return True
        return False

    # Initialize turn_cnt to 1.
    turn_cnt = 1
    while 1: # Super loop
        for i in range(k): # Repeat move process from 0 to k - 1.
            if move_proc(i): # If end_flag on, print turn_cnt and return.
                print(turn_cnt)
                return
        # The turn_cnt increased.
        turn_cnt += 1
        if turn_cnt >= 1000: # If turn_cnt >= 1,000 print -1 and return.
            print(-1)
            return


solution_proc()