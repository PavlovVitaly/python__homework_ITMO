def is_palindrome(s):
    s = list((str(s).replace(' ', '')).lower())
    s_invert = s.copy()
    s_invert.reverse()

    for i in range(len(s)-1):
        if s[i] != s_invert[i]:
            return False
    return True
