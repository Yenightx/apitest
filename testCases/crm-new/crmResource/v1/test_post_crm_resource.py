from api_call.finbiz.admin import ManagerAPI
from Zlib.co_restful import Restful
from testCases import *


@allure.feature("资源池列表分页查询")
class TestPostCrmResource:
    def setup_class(self):
        self.manager_o = ManagerAPI(ENVIRONMENT)
        self.rest_o = Restful()

    def teardown_class(self):
        pass

    @allure.story("获取资源测试列表数据")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.H
    def test_post_crm_resource(self):
        # 配置请求参数
        label_list = [LabelListDTO(classifyType=1, labelList=[]).get(),
                      LabelListDTO(classifyType=2, labelList=[]).get(),
                      LabelListDTO(classifyType=3, labelList=[]).get()]
        body = ResourceListDTO(pageSize=10, currentPage=1, permScope=0, labelList=label_list).get()

        # 发送请求
        res = self.manager_o.post_crm_resource(body=body)

        # 断言返回状态码
        data_struct = self.rest_o.parse_response(res, 200, "资源池列表分页查询失败")

        # 验证返回的数据结构
        ResultOfPageInfoOfCrmResourceVO(data_struct)