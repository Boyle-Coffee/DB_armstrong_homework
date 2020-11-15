# author:Boyle time:2020/11/15
import traceback


def closure_main(X, F):
    """
    求解闭包函数
    :param X: 给定属性集
    :param F: 给定依赖集
    :return: common result 返回值
    """
    try:
        X_last = set(X)
        U = set()
        for f_i in F:
            U |= set(f_i["V"])
            U |= set(f_i["W"])
        if not X_last <= U:
            return 400, False, "属性集X中包含的元素不全在属性集总体U", None
        while True:
            B = set()
            for f_i in F:
                if set(f_i["V"]) <= X_last:
                    for A in f_i["W"]:
                        B.add(A)
            X_i = X_last | B
            print(X_i)
            if X_i == X_last or X_i == U:
                break
            else:
                X_last = X_i

        return 200, True, None, list(X_i)

    except Exception as e:
        print(traceback.format_exc())
        message = "计算时出现错误"
        return 500, False, message, None
