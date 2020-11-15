# author:Boyle time:2020/11/15

def FG_equal(F, G):
    """
    判断是否是同一个函数依赖集
    :param F: 函数依赖集F
    :param G: 函数依赖集G
    :return: <bool> 是否是同一个
    """
    for f_i in F:
        for g_i in G:
            if set(f_i["V"]) == set(g_i["V"]) and set(f_i["W"]) == set(g_i["W"]):
                break
        else:
            return False

    for g_i in F:
        for f_i in G:
            if set(f_i["V"]) == set(g_i["V"]) and set(f_i["W"]) == set(g_i["W"]):
                break
        else:
            return False

    return True