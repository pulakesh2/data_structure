def check_palindrome(str):
    l = 0
    r = len(str)-1
    return False if not helper(str, l, r) else True

def helper(str, l, r):
    if l >= r:
        return True

    if str[l] != str[r]:
        return False
    else:
        return helper(str, l+1, r-1)


print(check_palindrome('tenet'))
