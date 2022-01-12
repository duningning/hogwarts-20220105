import time
import uuid
import os

from httprunner import __version__

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
