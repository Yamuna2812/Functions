def common(a, b):
    return list(set(a) & set(b))

print(common([1,2,3], [2,3,4]))
