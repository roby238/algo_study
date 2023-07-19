# BOJ_2174
# 로봇 시뮬레이션

import sys


def solution():
    field_size_x, field_size_y = map(int, input().split())
    robot_num, inst_num = map(int, input().split())
    robot_list = list()
    inst_list = list()

    # 방향 : N = 0, E = 1, S = 2, W =3
    for i in range(robot_num):
        robot_list.append([int(x) if idx < 2 else x for idx, x in enumerate(input().split())])
        if robot_list[i][2] == 'N':
            robot_list[i][2] = 0
        elif robot_list[i][2] == 'E':
            robot_list[i][2] = 1
        elif robot_list[i][2] == 'S':
            robot_list[i][2] = 2
        else:
            robot_list[i][2] = 3
    for i in range(inst_num):
        inst_list.append([x if idx == 1 else int(x) for idx, x in enumerate(input().split())])

    def turn_left(turn_inst):
        for r in range(turn_inst[2] % 4):
            robot_list[turn_inst[0] - 1][2] = (robot_list[turn_inst[0] - 1][2] + 3) % 4

    def turn_right(turn_inst):
        for r in range(turn_inst[2] % 4):
            robot_list[turn_inst[0] - 1][2] = (robot_list[turn_inst[0] - 1][2] + 1) % 4

    def error_detect(forward_inst, robot_index):
        # bound = [0이면 벽 / 숫자면 로봇, 이동 가능 길이]
        bound = [0, None]
        if robot_list[robot_index][2] == 0:
            bound[1] = field_size_y - robot_list[robot_index][1]
            for r in range(robot_num):
                if (robot_list[r][0] == robot_list[robot_index][0] and
                        0 <= (robot_list[r][1] - robot_list[robot_index][1] - 1) < bound[1]):
                    bound = [r + 1, robot_list[r][1] - robot_list[robot_index][1] - 1]
        elif robot_list[robot_index][2] == 1:
            bound[1] = field_size_x - robot_list[robot_index][0]
            for r in range(robot_num):
                if (robot_list[r][1] == robot_list[robot_index][1] and
                        0 <= (robot_list[r][0] - robot_list[robot_index][0] - 1) < bound[1]):
                    bound = [r + 1, robot_list[r][0] - robot_list[robot_index][0] - 1]
        elif robot_list[robot_index][2] == 2:
            bound[1] = robot_list[robot_index][1] - 1
            for r in range(robot_num):
                if (robot_list[r][0] == robot_list[robot_index][0] and
                        0 <= (robot_list[robot_index][1] - robot_list[r][1] - 1) < bound[1]):
                    bound = [r + 1, robot_list[robot_index][1] - robot_list[r][1] - 1]
        else:
            bound[1] = robot_list[robot_index][0] - 1
            for r in range(robot_num):
                if (robot_list[r][1] == robot_list[robot_index][1] and
                        0 <= (robot_list[robot_index][0] - robot_list[r][0] - 1) < bound[1]):
                    bound = [r + 1, robot_list[robot_index][0] - robot_list[r][0] - 1]

        if forward_inst[2] > bound[1]:
            if bound[0] == 0:
                print(f"Robot {robot_index + 1} crashes into the wall")
                sys.exit(0)
            else:
                print(f"Robot {robot_index + 1} crashes into robot {bound[0]}")
                sys.exit(0)

    def forward(forward_inst):
        robot_index = forward_inst[0] - 1
        error_detect(forward_inst, robot_index)

        if robot_list[robot_index][2] == 0:
            robot_list[robot_index][1] += forward_inst[2]
        elif robot_list[robot_index][2] == 1:
            robot_list[robot_index][0] += forward_inst[2]
        elif robot_list[robot_index][2] == 2:
            robot_list[robot_index][1] -= forward_inst[2]
        else:
            robot_list[robot_index][0] -= forward_inst[2]

    for inst in inst_list:
        if inst[1] == 'L':
            turn_left(inst)
        elif inst[1] == 'R':
            turn_right(inst)
        else:
            forward(inst)
    else:
        print("OK")


if __name__ == "__main__":
    solution()
