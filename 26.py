def palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    return "Not Palindrome"

print(palindrome("madam"))
