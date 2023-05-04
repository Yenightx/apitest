from api_call.finbiz.admin import ManagerAPI
from Zlib.co_restful import Restful
from testCases import *


@allure.feature("获取账单列表")
class TestPostBillInfo:
    def setup_class(self, env='test'):
        self.manager_o = ManagerAPI(env)
        self.rest_o = Restful()

    def teardown_class(self):
        pass

    @allure.story("获取账单列表")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.H
    def test_get_current_org_info_h(self):
        """
        获取当前切换到的组织的组织信息接口
        """
        body = dict(currentPage=1, pageSize=20, createBeginTime="2023-03-28", createEndTime="2023-04-27", checkType=1)
        res = self.manager_o.post_page_bill_info(body)
        data_struct = self.rest_o.parse_response(res, 200, "获取账单列表失败")


