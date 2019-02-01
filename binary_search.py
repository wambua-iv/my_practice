pos = -1


def search(list, n):
    sorted(list)
    lower = 0
    upper = len(list) - 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                lower = mid + 1
            else:
                upper = mid- 1
    return False


list = [6, 55, 45, 54, 585, 457, 545, 565, 854, 885]
n = 585


if search(list, n):

    print("found at position:", pos+1)
else:
    print("not found")

