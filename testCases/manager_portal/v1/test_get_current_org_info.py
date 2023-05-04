from api_call.fsd.manager_portal_call import ManagerAPI
from Zlib.co_restful import Restful
from testCases import *


@allure.feature("获取当前切换到的组织的组织信息接口")
class TestGetCurrentOrgInfo:
    def setup_class(self, env='test'):
        self.manager_o = ManagerAPI(env)
        self.rest_o = Restful()

    def teardown_class(self):
        pass

    @allure.story("获取当前切换到的组织的组织信息接口")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.H
    def test_get_current_org_info_h(self):
        """
        获取当前切换到的组织的组织信息接口
        """
        res = self.manager_o.get_current_org_info()
        data_struct = self.rest_o.parse_response(res, 200, "获取当前切换到的组织的组织信息接口访问失败")

    @allure.story("获取当前切换到的组织的组织信息接口1")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.M
    def test_get_current_org_info_m(self):
        res = self.manager_o.get_current_org_info()
        data_struct = self.rest_o.parse_response(res, 200, "获取当前切换到的组织的组织信息接口访问失败")

    @allure.story("获取当前切换到的组织的组织信息接口2")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.L
    def test_get_current_org_info_l(self):
        res = self.manager_o.get_current_org_info()
        data_struct = self.rest_o.parse_response(res, 200, "获取当前切换到的组织的组织信息接口访问失败")

