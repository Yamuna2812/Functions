def consonants(s):
    count = 0
    for i in s.lower():
        if i.isalpha() and i not in "aeiou":
            count += 1
    return count

print(consonants("Python"))
