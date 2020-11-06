def isLongPressedName(name, typed):

    """
    :type name: str
    :type typed: str
    :rtype: bool
    """
    j = i = 0
    while i < len(name)-1 and j < len(typed)-1:
        # if typed[j] == name[i]:
        #     i += 1
        # elif typed[j] != name[i-1]:
        #     return False
        # j += 1
        if typed[j] == name[i]:
            i += 1
            j += 1
            continue

        if typed[j] == name[i-1]:
            j += 1

        else:
            return False

    if i == len(name) - 1:
        while j != len(typed)-1:
            if typed[j] == name[i] or typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        if typed[j] == name[i]:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    ret = isLongPressedName("jjyyyyy","jjjyyyy")
    print(ret)
