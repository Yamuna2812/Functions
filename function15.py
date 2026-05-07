def swap_case(s):
    string = ""
    for i in s:
        if i == i.lower():
            string = string + i.upper()
        else:
            string = string + i.lower()
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)