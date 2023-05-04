# coding=utf-8
__author__ = 'ztx'


from api_call.finbiz.http_o import BaseHttp


class ManagerAPI(BaseHttp):
    def __init__(self, env):
        """
        初始化方法
        各个接口方法中封装需要的公共内容
        """
        BaseHttp.__init__(self, config_name="config.yaml", env=env, account_config_name="account_cfg.ini")
        self.env = env

    def post_page_bill_info(self, body):
        """
        资源池列表分页查询
        :return:
        """
        url = '/finbizAdmin/front/v1/billInfo/pageBillInfo'
        self.set_auth(token_type=1)
        return self.post(url=url, body=body)
