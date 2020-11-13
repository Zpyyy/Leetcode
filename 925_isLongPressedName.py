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
    
    
    

'''
解法2：利用字典
    将name，typed按顺序出现的不同字母索引作为key，该字母出现的次数作为value分别存入字典1、字典2
    如 name = "assd", typed = "bssd"
        dict_name  = {0: 1, 1: 2, 3: 1}   #第0个字符出现1次，第1个字符出现2次，第3个字符出现1次
        dict_typed = {0: 1, 1: 2, 3: 1}

    从第index（初始化为0）位遍历字符串name中的字母：
        若name[index1]==dict[index2]则说明字母相同，需比较字母出现的次数(value值)是否符合
            若typed中各字母出现的次数比name中还少，肯定是错误的。
            若 次数等于或多于，则比较下一个字母，下一个索引即为本次索引加上该字母出现的次数（即其value值）
        若不等 直接return false
    最后一次的key值一定等于字符串总长度，若不等则说明某一字符串还没有比较完，说明有不同数量的字母存在，则return false（如“sad""sadddrrr")
        
'''
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


