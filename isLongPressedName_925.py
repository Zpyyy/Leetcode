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
    
    
    
# 解法2
def isLongPressedName2(name,typed):
    dict = {}
    count = temp = 0

    for i in range(len(name)):
        if i == 0 or name[i] != name[i-1] :
            temp = i
            count = 1
            dict[i] = count
        else:
            count += 1
            dict[temp] = count
    print(dict)
    dict2 = {}

    for i in range(len(typed)):
        if i == 0 or typed[i] != typed[i-1] :
            temp = i
            count = 1
            dict2[i] = count
        else:
            count += 1
            dict2[temp] = count

    print(dict2)

    index1 = index2 = 0
    while index1 < len(name) and index2 < len(typed):
        if name[index1] == typed[index2]:
            if dict[index1] <= dict2[index2]:
                index1 = index1 + dict[index1]
                index2 = index2 + dict2[index2]
            else:
                return False
        else:
            return False

    if index1 == len(name) and index2 == len(typed):
        return True
    else:
        return False


if __name__ == '__main__':
    ret = isLongPressedName2("assd","bssd")
    print(ret)


