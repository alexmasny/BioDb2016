def fibd(n, m):
    lst_fibd = [1] + [0] * (m - 1)
    for i in range(1, n):
        bun = 0
        for j in range(1, m):
            bun += lst_fibd[(i - j - 1) % m]
        lst_fibd[(i) % m] = bun

    # Total rabbits is the sum of the living rabbits.
    int_ret = sum(lst_fibd)
    return int_ret


# fibd(6, 3)
fibd(87, 19)
