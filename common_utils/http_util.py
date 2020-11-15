# author:Boyle time:2020/11/15
from flask import jsonify


def common_result(code, isSuccess, message, data):
    # common result 返回参数
    return jsonify({"code": code,
                    "isSuccess": isSuccess,
                    "message": message,
                    "data": data
                    })


def check_params(require_params, json_params):
    """
    检查接口获取的参数是否正确
    :param <list> require_params: 接口要求的参数
    :param <list> json_params: 接口获取的 json 参数
    :return:
        <bool> isSuccess: "是否检查成功"
        <str> message: "返回错误信息，检查成功返回 None"
    """
    for param in json_params:
        if param not in require_params:
            message = "'%s' is an invalid param" % (param)
            return False, message

    for param in require_params:
        if param not in json_params:
            message = "request missing required param '%s'" % (param)
            return False, message

    return True, None
