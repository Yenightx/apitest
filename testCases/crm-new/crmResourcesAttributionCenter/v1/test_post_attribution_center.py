from api_call.finbiz.admin import ManagerAPI
from Zlib.co_restful import Restful
from testCases import *


@allure.feature("归属中心列表查询")
class TestPostAttributionCenter:
    def setup_class(self):
        self.manager_o = ManagerAPI(ENVIRONMENT)
        self.rest_o = Restful()

    def teardown_class(self):
        pass

    @allure.story("归属中心列表查询")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.M
    def test_post_crm_resource(self):
        # 配置请求参数
        body = AttributionCenterDTO(enableStatus=0).get()

        # 发送请求
        res = self.manager_o.post_attribution_center(body=body)

        # 断言返回状态码
        data_struct = self.rest_o.parse_response(res, 200, "归属中心列表查询失败")

        # 验证返回的数据结构
        ResultOfListOfAttributionCenterVO(data_struct)