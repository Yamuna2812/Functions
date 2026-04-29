def sentence(*letters):
    count=0
    for letter in letters:
        count +=len(letter)
    return count
print(sentence("letter"))
print(sentence("yamuna"))
print(sentence("google"))
