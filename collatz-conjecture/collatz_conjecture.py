def steps(n: int) -> int:
    if n <= 0: raise ValueError("Rawr xD")
    step: int = 0
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n /= 2
        step += 1

    return step
