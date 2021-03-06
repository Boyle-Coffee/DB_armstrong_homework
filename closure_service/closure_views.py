# author:Boyle time:2020/11/15
from flask import Blueprint, json, request

from common_utils.http_util import *
from .closure_util import closure_main


closure_app = Blueprint("closure", __name__)


@closure_app.route("/closure/inputList", methods=["POST"])
def closure_input_list():
    # 要求的参数
    json_params = ["X", "F"]
    F_obj_params = ["V", "W"]

    post_json = json.loads(request.get_data())
    if isinstance(post_json, dict):
        isSuccess, message = check_params(json_params, list(post_json.keys()))
        if not isSuccess:
            return common_result(400, False, message, None)
    else:
        return common_result(400, False, "the type of json is error", None)
    if isinstance(post_json["X"], list):
        for obj in post_json["X"]:
            if not isinstance(obj, str):
                return common_result(400, False, "the elements of 'X' is error", None)
    else:
        return common_result(400, False, "the type of 'X' is error", None)
    if isinstance(post_json["F"], list):
        for obj in post_json["F"]:
            if isinstance(obj, dict):
                isSuccess, message = check_params(F_obj_params, list(obj.keys()))
                if isSuccess:
                    for i in ["V", "W"]:
                        if isinstance(obj[i], list):
                            for obj2 in obj[i]:
                                if not isinstance(obj2, str):
                                    return common_result(400, False, "the elements of 'F' is error", None)
                        else:
                            return common_result(400, False, "the elements of 'F' is error", None)
                else:
                    return common_result(400, False, message, None)
            else:
                return common_result(400, False, "the elements of 'F' is error", None)
    else:
        return common_result(400, False, "the type of 'F' is error", None)

    X = post_json["X"]
    F = post_json["F"]
    code, isSuccess, message, data = closure_main(X, F)

    return common_result(code, isSuccess, message, data)