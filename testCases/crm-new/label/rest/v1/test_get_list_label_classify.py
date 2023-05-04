from api_call.finbiz.admin import ManagerAPI
from Zlib.co_restful import Restful
from testCases import *


@allure.feature("查询标签分组列表")
class TestGetListLabelClassify:
    def setup_class(self):
        self.manager_o = ManagerAPI(ENVIRONMENT)
        self.rest_o = Restful()

    def teardown_class(self):
        pass

    @allure.story("查询标签分组列表")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.M
    def test_get_list_label_classify(self):
        # 发送请求
        res = self.manager_o.get_list_label_classify()

        # 断言返回状态码
        data_struct = self.rest_o.parse_response(res, 200, "查询标签分组列表查询失败")

        # 验证返回的数据结构
        ResultOfListOfLabelClassFyObject(data_struct)