def isGF(list):
    if len(list) < 2:
        return True
    elif list[0] == 0:
        return False
    else:
        q = list[1] / list[0]
        i = 2
        while i < len(list):
            if list[i] / list[i-1] != q:
                return False
            i += 1
        return True
print(isGF([5/4,5/2, 5, 10, 20] ))