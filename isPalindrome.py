def isPalindrome(s: str) -> bool:
    l = 0
    r = len(s) - 1
    while (l < r):
        while (l < r) and not alphaNumeric(s[l]):
            l += 1
        while (l < r) and not alphaNumeric(s[r]):
            r -= 1
        if (s[l].lower() != s[r].lower()):
            return False
        l += 1
        r -= 1
    return True


def alphaNumeric(c):
    return (ord('A') <= ord(c) <= ord('Z') or 
    ord('a') <= ord(c) <= ord('z') or 
    ord('0') <= ord(c) <= ord('9'))

testS = "Was it a car or a cat I saw?"
print(isPalindrome(testS))