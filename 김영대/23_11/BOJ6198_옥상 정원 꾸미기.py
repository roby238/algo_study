import sys
from collections import deque


def solution_proc():
    """
    Solution Process
    Sum count of buildings to be able to do benchmarking.
    :return: None
    """
    # Get n.
    read = sys.stdin.readline
    n = int(read())

    def get_benchmarking_cnt_proc():
        """
        Get sum of count of buildings to be able to do benchmarking.
        :return: int
        """
        # Initialize cnt and stack.
        benchmarking_cnt = 0
        stack = deque()
        for _ in range(n):
            # Get input.
            height = int(read())
            # If stack is NOT empty, compare top of stack and height.
            # 1) top of stack <= height, pop stack and add length of stack.
            # 2) top of stack > height, do NOTHING.
            # Else stack is empty, do NOTHING.
            while stack and stack[-1] <= height:
                stack.pop()
                benchmarking_cnt += len(stack)
            # Push height to stack.
            stack.append(height)
        # Because there is NOT to compare to last input, just pop stack and add length of stack.
        while stack:
            stack.pop()
            benchmarking_cnt += len(stack)
        # Return cnt.
        return benchmarking_cnt

    # Print result
    print(get_benchmarking_cnt_proc())


solution_proc()