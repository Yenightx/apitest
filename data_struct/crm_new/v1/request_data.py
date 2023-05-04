from Zlib.co_unity import *


class ResourceListDTO(BaseData):
    """
    资源表列表DTO
    """
    def __init__(self, actualResourceUserDateEnd=None, actualResourceUserDateStart=None, actualResourceUserId=None,
                 addressIdList=None, admissionDateEnd=None, admissionDateStart=None, atTimeEnd=None, atTimeStart=None,
                 channelSourceIds=None, createTimeEnd=None, createTimeSend=None, createUserIds=None, crmReferrerIds=None,
                 crmResourceLevelIds=None, crmResourceTypeId=None, currentPage=None, filterResourceIds=None,
                 firstVisitDateEnd=None, firstVisitDateStart=None, followupNumEnd=None, followupNumStart=None,
                 isReferrer=None, isReferrerUrl=None, labelList=None, lastFollowupDateEnd=None, lastFollowupDateStart=None,
                 leavingDateEnd=None, leavingDateStart=None, maintainUserIds=None, mergeCheckUserIdList=None,
                 mergeDateEnd=None, mergeDateStart=None, mergeUserIdList=None, oldStudentsToSchool=None, orderField=None,
                 orgList=None, ownerIds=None, pageSize=None, permScope=None, planFollowupDateEnd=None, planFollowupDateStart=None,
                 possessStatus=None, quitRegistrationDateEnd=None, quitRegistrationDateStart=None, receiveUserIds=None,
                 recoveryStatus=None, registrationDateEnd=None, registrationDateStart=None, resourceAcquireDateEnd=None,
                 resourceAcquireDateSend=None, resourceReceiveTimeEnd=None, resourceReceiveTimeStart=None,
                 resourcesAttributionCenterIds=None, search=None, source=None, status=None, studentNameResourceIds=None,
                 type=None, updateDateEnd=None, updateDateStart=None, workbenchCode=None, workbenchEndTime=None,
                 workbenchStartTime=None):
        """
        :param actualResourceUserDateEnd: 搜索项-转有效资源时间 - 结束		false   string(date-time)
        :param actualResourceUserDateStart: 搜索项-转有效资源时间 - 开始		false	string(date-time)
        :param actualResourceUserId: 转有效资源人		false	array   integer
        :param addressIdList: (资源家庭住址)id列表		false	array   string
        :param admissionDateEnd: 搜索项-入校日期 - 结束		false	string(date-time)
        :param admissionDateStart: 搜索项-入校日期 - 开始		false	string(date-time)
        :param atTimeEnd: 搜索项-资源分配时间结束		false	string(date-time)
        :param atTimeStart: 搜索项-资源分配时间开始		false	string(date-time)
        :param channelSourceIds: 搜索项-渠道ids		false	array   integer
        :param createTimeEnd: 搜索项-创建时间 - 结束		false	string(date-time)
        :param createTimeSend: 搜索项-创建时间 - 开始		false	string(date-time)
        :param createUserIds: 资源录入人		false	array   integer
        :param crmReferrerIds: 搜索项-转介绍人Ids		false	array   integer
        :param crmResourceLevelIds: 搜索项-资源等级ids		false	array   integer
        :param crmResourceTypeId: 搜索项-资源分类id		false	integer(int32)
        :param currentPage:
        :param filterResourceIds: 需要过滤的资源ids		false	array   integer
        :param firstVisitDateEnd: 搜索项-首次到访日期 - 结束		false	string(date-time)
        :param firstVisitDateStart: 搜索项-首次到访日期 - 开始		false	string(date-time)
        :param followupNumEnd: 跟进次数结束		false	integer(int32)
        :param followupNumStart: 跟进次数开始		false	integer(int32)
        :param isReferrer: 搜索项-转介绍资源 1 转介绍 2 非转介绍		false	integer(int32)
        :param isReferrerUrl: 搜索项-转介绍凭证 1 有 2 无		false	integer(int32)
        :param labelList: 资源标签关联表DTO
        :param lastFollowupDateEnd: 搜索项-最后跟进日期 - 结束		false	string(date-time)
        :param lastFollowupDateStart: 搜索项-最后跟进日期 - 开始		false	string(date-time)
        :param leavingDateEnd: 搜索项-离校日期 - 结束		false	string(date-time)
        :param leavingDateStart: 搜索项-离校日期 - 开始		false	string(date-time)
        :param maintainUserIds: 搜索项-维护人Ids		false	array   integer
        :param mergeCheckUserIdList: 合并审批人		false	array   integer
        :param mergeDateEnd: 合并时间 - 结束		false	string(date-time)
        :param mergeDateStart: 合并时间 - 开始		false	string(date-time)
        :param mergeUserIdList: 合并发起人		false	array   integer
        :param oldStudentsToSchool: 是否离校返校 1：否 2：是		false	integer(int32)
        :param orderField: 排序字段 false   string
            crm_followup_last_time:最近跟进时间
            actual_resource_user_update_time:转有效资源时间
            registration_date:报名日期
            admission_date:入校日期
            leaving_date:离校日期
            create_time:创建时间
            resource_acquire_date:资源获取时间
            resource_receive_time:资源接收时间
            first_visit_time:首次到访时间
            crm_followup_num:跟进次数
        :param orgList:
        :param ownerIds: 当前所属人ids		false	array   integer
        :param pageSize:
        :param permScope: 权限范围		false	integer(int32)
        :param planFollowupDateEnd: 搜索项-计划跟进日期 - 结束		false	string(date-time)
        :param planFollowupDateStart: 搜索项-计划跟进日期 - 开始		false	string(date-time)
        :param possessStatus: 资源是否有所有人 0 有 1 无		false	integer(int32)
        :param quitRegistrationDateEnd: 搜索项-退报日期 - 结束		false	string(date-time)
        :param quitRegistrationDateStart: 搜索项-退报日期 - 开始		false	string(date-time)
        :param receiveUserIds: 搜索项-接收人用户ids		false	array   integer
        :param recoveryStatus: 是否有康复史 1：否 2：是,3.已问未知,4.未问未知		false	integer(int32)
        :param registrationDateEnd:	搜索项-报名日期 - 结束		false	string(date-time)
        :param registrationDateStart:搜索项-报名日期 - 开始		false	string(date-time)
        :param resourceAcquireDateEnd: 搜索项-资源获取日期 - 结束		false	string(date-time)
        :param resourceAcquireDateSend: 搜索项-资源获取日期 - 开始		false	string(date-time)
        :param resourceReceiveTimeEnd: 搜索项-资源接收时间 - 结束		false	string(date-time)
        :param resourceReceiveTimeStart: 搜索项-资源接收时间 - 开始		false	string(date-time)
        :param resourcesAttributionCenterIds: 所属中心ids		false	array   integer
        :param search: 搜索项-资源手机号、资源姓名、所有人姓名、所在地区、中心等关键字进行搜索		false	string
        :param source: 搜索项-来源		false	integer(int32)
        :param status: 搜索项-资源状态		false	array   integer
        :param studentNameResourceIds: 学生姓名对应资源ids		false	array   integer
        :param type: 资源tab类型		false	string
        :param updateDateEnd: 搜索项-最后修改日期 - 结束		false	string(date-time)
        :param updateDateStart: 搜索项-最后修改日期 - 开始		false	string(date-time)
        :param workbenchCode: 工作台唯一标识		false	integer(int32)
        :param workbenchEndTime: 工作台查询时间 - 结束		false	string(date-time)
        :param workbenchStartTime: 工作台查询时间 - 开始		false	string(date-time)
        """
        BaseData.__init__(self)
        self.params = copy_dict(locals())


class LabelListDTO(BaseData):
    """
    资源标签关联表DTO
    """
    def __init__(self, classifyType=None, labelList=None):
        """
        :param classifyType: integer(int32)	类型 ClassifyTypeEnum
        :param labelList: array	资源标签列表	integer
        """
        BaseData.__init__(self)
        self.params = copy_dict(locals())


class AttributionCenterDTO(BaseData):
    """
    归属中心DTO
    """
    def __init__(self, currentPage=None, enableStatus=None, id=None, name=None, orgIds=None, orgList=None, pageSize=None):
        """
        :param currentPage: 分页数	false	integer(int32)
        :param enableStatus: 启用状态，0 ：启用，1：禁用		false	integer(int32)
        :param id: 主键 新增时不传		false	integer(int32)
        :param name: 名称		false	string
        :param orgIds: 组织架构ids		false	string
        :param orgList: array
        :param pageSize: 页数  integer(int32)
        """
        BaseData.__init__(self)
        self.params = copy_dict(locals())