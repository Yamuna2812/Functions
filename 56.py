def perfect(n):
    s = 0

    for i in range(1, n):
        if n % i == 0:
            s += i

    if s == n:
        return "Perfect Number"
    return "Not Perfect"

print(perfect(6))
