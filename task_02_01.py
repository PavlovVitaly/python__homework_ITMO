def is_palindrome(s):
    DICT = {ord(' '): '',
            ord('.'): '',
            ord(','): '',
            ord('!'): '',
            ord('?'): '',
            ord(':'): '',
            ord(';'): '',
            ord('#'): '',
            ord('*'): ''}
    s = list((str(s).translate(DICT)).lower())
    s_invert = s.copy()
    s_invert.reverse()

    for i in range(len(s)-1):
        if s[i] != s_invert[i]:
            return False
    return True
