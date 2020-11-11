def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    # """
    dic = {}
    str_list = s.split(" ")
    if len(str_list) != len(pattern):
        return False

    for ch, str in zip(pattern, str_list):
        if ch not in dic.keys():
            # 字符串不在字典的值中，就加入该字符作为key，value=其匹配的字符串
            if str not in dic.values():
                dic[ch] = str
            # 在字典中，说明该字符串提前匹配了其他的key字母
            else:
                return False
        else:
            # key已经存在于字典中，判断此时的str是否为其value。不是则不匹配、
            if dic[ch] != str:
                return False
    print(dic)
    return True
