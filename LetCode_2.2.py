def check2rec(num):
    if num == 1:
        return True
    if num & 1:
        return False
    return check2rec(num >> 1)


print(check2rec(61))