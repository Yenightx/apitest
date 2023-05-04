# coding=utf-8
__author__ = 'ztx'

import json
import os
import time

from Zlib.co_path import Path
from Zlib.co_request import RequestHandler
from Zlib.co_token.finbiz_login import FinBiz
from Zlib.co_readfiledata import ReadFileData


class BaseHttp(object):
    def __init__(self, config_name, env="test", account_config_name=None):
        """
        :param env: 指定配置文件中的环境名称
        """
        self.env = env
        # self.language = language
        self.config_name = config_name
        self.account_config_name = account_config_name
        self.token_o = FinBiz(self.env)

        # 读取配置文件
        path_o = Path()
        self.root_path = path_o.get_root_path()
        self.conf = ReadFileData()
        conf_list = self.conf.load_yaml(file_path=self.root_path + os.sep + "config" + os.sep + "config.yaml")[self.env]
        self.host = conf_list["host"]

        # 设置请求头部
        self.headers = dict()
        self.headers['Content-Type'] = 'application/json'
        self.headers['app_id'] = conf_list['appId']
        self.headers['nonce_str'] = conf_list['nonceStr']
        self.thread = RequestHandler()

    def set_auth(self, token_type=1, account=None, password=None, body=None):
        """
        设置身份信息
        :param token_type:
            0：不设置X-User-Token
            1：正常传入X-User-Token
        :param account: 账号
        :param password: 密码
        :return:
        """
        conf = ReadFileData()
        conf_list = conf.load_yaml(file_path=self.root_path + os.sep + "config" + os.sep + "config.yaml")[self.env]
        if token_type == 0:
            self.remove_user_token()
        elif token_type == 1:
            if account is None:
                account = conf_list["account"]
            if password is None:
                password = conf_list["password"]
            self.headers["token"] = self.token_o.get_token(account=account, password=password)

    def get(self, url, params=None):
        url = self.host + url
        return self.thread.visit(method="GET", url=url, params=params, headers=self.headers)

    def post(self, url, params=None, data=None, body=None):
        self.headers['sign'], self.headers['timestamp'] = self.token_o.get_sign(token=self.headers['token'], body=body)
        url = self.host + url
        return self.thread.visit(method="POST", url=url, params=params, data=data, json=body, headers=self.headers)

    def remove_user_token(self):
        if 'token' in self.headers.keys():
            self.headers.pop('token')


if __name__ == '__main__':
    a = BaseHttp(config_name="config.yaml", env="test", account_config_name="account.yaml")
    a.set_auth()

