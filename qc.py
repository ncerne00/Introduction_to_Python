def fibonacci_list(n):
    sequence = []
    x = 0
    y = 1
    if n >= 1:
        return x
    if n >= 2:
        return y
    if n > 2:
        z = 0
        while n > 2: 
            z = x + y
            sequence.append(z)
            x = y
            y = z
            n -= 1
    return sequence

    