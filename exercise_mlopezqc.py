def count_multiples(a, b):
    if b % a:
        return 0
    return 1 + count_multiples(a, b / a)
