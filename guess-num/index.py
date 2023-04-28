def get_guess(in_mind):
    def guess(guess_n):
        if guess_n > in_mind:
            return -1
        if guess_n < in_mind:
            return 1
        if guess_n == in_mind:
            return 0

    return guess


def guess_number(guess, n: int) -> int:
    low = 0
    high = n
    if n == 1:
        return n
    while low <= high:
        guess_num = int((low + high) / 2)
        result = guess(guess_num)
        if result == 0:
            return guess_num
        if result == -1:
            high = guess_num - 1
        if result == 1:
            low = guess_num + 1
    return None


def run(input, in_mind):
    result = guess_number(get_guess(in_mind), input)
    print(f"result is: {result}")


run(2, 2)
