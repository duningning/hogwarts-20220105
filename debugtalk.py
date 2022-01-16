import string
import time
import uuid
import os
import random


from httprunner import __version__
from httprunner.response import ResponseObject


def gen_random_request_id():
    # request_id = str(uuid.uuid4())
    # print(f"request_id:{request_id}")
    # return request_id
    return str(uuid.uuid4())

#实现测试环境和生产环境的切换
def get_test_host():
    if os.environ.get("TestEnv") == "Test":
        return "mubu.net"
    else:
        return "mubu.com"


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def get_folders_num(resp: ResponseObject)->int:
    resp_json = resp.resp_obj.json()
    folders_num = len(resp_json["data"]["folders"])#列表的数目
    print(f"folders_num----{folders_num}")
    return folders_num


def get_random_string(str_len): #生成指定属谬随机字符串
    return "".join(
        random.choice(string.ascii_letters+ string.digits) for _ in range(str_len)
    )