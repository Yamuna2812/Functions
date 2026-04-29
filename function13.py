def sum_n(n):
    if n == 1:          # base case
        return 1
    else:
        return n + sum_n(n - 1)

num = int(input("Enter n: "))
print("Sum =", sum_n(num))