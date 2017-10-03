def is_palindrome(s):
    s = str(s).replace(' ', '')
    s = list(s.lower())
    s_invert = s.copy()
    s_invert.reverse()

    for i in range(len(s)-1):
        if s[i] != s_invert[i]:
            return False
    return True
