# author:Boyle time:2020/11/15
import traceback
import random
from pprint import pprint

from closure_service.closure_util import closure_main
from common_utils.data_util import *

# 步骤1
def step1(F):
    F_m = []

    for f_i in F:
        for A in f_i["W"]:
            obj_copy = f_i.copy()
            obj_copy["W"] = [A]
            F_m.append(obj_copy)

    return F_m

# 步骤2
def step2(F):
    F_m = F.copy()

    for i in range(len(F)-1, -1, -1):
        G = F_m.copy()
        X = G[i]["V"]
        A = G[i]["W"]
        del G[i]
        print(X, A)
        code, isSuccess, message, X_G = closure_main(X, G)
        if not isSuccess:
            return None
        print(A[0], X_G)
        if A[0] in X_G:
            del F_m[i]

    return F_m

# 步骤3
def step3(F):
    F_m = F.copy()
    is_change = False

    for i in range(len(F)):
        X = F[i]["V"]
        A = F[i]["W"]
        X_new = []
        for B in X:
            X_B = list(set(X) - {B})
            code, isSuccess, message, X_B_F = closure_main(X_B, F_m)
            if not isSuccess:
                return None
            if A not in X_B_F:
                X_new.append(B)
            else:
                is_change = True
        F_m[i]["V"] = X_new

    return F_m, is_change


def minimal_cover_main(F):
    """
    请求最小依赖集函数
    :param F: 给定依赖集
    :return: common result 返回值
    """
    try:
        data = {}
        i = 1
        for _ in range(10):
            F_rand = F.copy()
            random.shuffle(F_rand)
            print("步骤1")
            F_m = step1(F_rand)
            while True:
                pprint(F_m)
                print("→步骤2")
                F_m = step2(F_m)
                if F_m is None:
                    message = "计算时出现错误"
                    return 500, False, message, None
                pprint(F_m)
                print("→步骤3")
                F_m, is_change = step3(F_m)
                if F_m is None:
                    message = "计算时出现错误"
                    return 500, False, message, None
                if not is_change:
                    break
            for F_mi in data.values():
                if FG_equal(F_m, F_mi):
                    break
            else:
                data["F_m"+str(i)] = F_m
                i += 1
        return 200, True, None, data
    except Exception as e:
        print(traceback.format_exc())
        message = "计算时出现错误"
        return 500, False, message, None
