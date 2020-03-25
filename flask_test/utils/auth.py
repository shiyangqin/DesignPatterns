# -*- encoding:utf-8 -*-
import functools


class Permission(object):
    """类函数权限验证装饰器"""

    def __init__(self, function, fail_msg='{"status": "not allow"}'):
        self.function = function
        self.failMsg = fail_msg

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user = Permission.get_user_info()
            flag = self.check_user(user)
            if flag:
                try:
                    kwargs['user'] = user
                    return func(*args, **kwargs)
                except TypeError as te:
                    raise te
            else:

                return self.failMsg
        return wrapper

    @staticmethod
    def get_user_info():
        """获取用户信息"""
        session = Permission.get_session()
        """
        查询用户信息，组装json
        包括各种账户信息，例如id，name等等，还有拥有的权限信息
        """
        return {"user": "this is user info"}

    @staticmethod
    def get_session():
        """获取请求头信息中的session"""
        """
        请根据个人情况获取session信息
        token = request.cookies.get('session', None)
        return token if token else request.headers.get('token', None)
        """
        return ""

    def check_user(self, user):
        """验证权限"""
        function = self.function
        user = user
        """
        使用user中的用户权限信息来验证是否包含function
        """
        return True
