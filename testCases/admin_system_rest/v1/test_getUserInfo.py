from api_call.finbiz.admin import ManagerAPI
from Zlib.co_restful import Restful
from testCases import *


@allure.feature("根据token获取用户信息")
class TestGetCurrentOrgInfo:
    def setup_class(self, env=ENVIRONMENT):
        self.manager_o = ManagerAPI(env)
        self.rest_o = Restful()

    def teardown_class(self):
        pass

    def test_2(self):
        res = self.manager_o.get_user_info()
        data_struct = self.rest_o.parse_response(res, 200, "根据token获取用户信息访问失败")

