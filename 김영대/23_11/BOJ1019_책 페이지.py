def solution_proc():
    """
    Solution Process \n
    Get count of appearance of each digit in from 1 to target number.
    :return: None
    """
    # Get input : target number
    n_str = input()
    # Get length of target number.
    length = len(n_str)
    # Make string number integer.
    n = int(n_str)
    # Generate decimal.
    # Because target number is up to 1,000,000,000 in this system,
    # Set size of list to 11
    decimal = [1 for _ in range(11)]
    # Initialize decimal.
    for i in range(1, 11):
        decimal[i] = decimal[i - 1] * 10

    def get_appearance_cnt_proc(num, kth, digit):
        """
        Get Digit Count Process \n
        Return cnt of appearance of d at kth position.
        :param num: a whole number
        :param kth: order of position of number
        :param digit: target digit
        :return: appearance_cnt
        """
        # Initialize cnt.
        appearance_cnt = 0
        # Cut leading zero cnt.
        non_leading_zero_num = num // decimal[kth + 1]
        # If the digit and non_leading_zero_num equal zero,
        # don't need to continue process.
        if digit == 0 and non_leading_zero_num == 0:
            return 0
        # Count
        appearance_cnt += non_leading_zero_num * decimal[kth]
        # Get kth digit
        kth_digit = num // decimal[kth] % 10
        # Case
        # 1) kth_digit > digit : count previous
        # 2) kth_digit == digit : count current
        if kth_digit > digit:
            appearance_cnt += decimal[kth]
        elif kth_digit == digit:
            appearance_cnt += num % decimal[kth] + 1
        # If digit is zero, substitute cnt of kth decimal.
        if digit == 0:
            appearance_cnt -= decimal[kth]
        # Return result.
        return appearance_cnt

    # Loop of each digit
    for i in range(10):
        # Initialize cnt.
        cnt = 0
        # Count considering each position of digit.
        for j in range(length):
            cnt += get_appearance_cnt_proc(n, j, i)
        # Print result of cnt.
        print(cnt, end=" ")


solution_proc()
