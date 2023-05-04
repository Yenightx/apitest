from Zlib.co_unity import *


class ResultOfPageInfoOfCrmResourceVO:
    """
    资源池列表分页信息查询结果汇总
    """
    def __init__(self, data):
        """
        :param data:
            code: 状态码
            data: PageInfoOfCrmResourceVO
            msg: 返回信息
        """
        assert_test(data, 'code', 'data', 'msg')
        if data['data']:
            PageInfoOfCrmResourceVO(data['data'])


class PageInfoOfCrmResourceVO:
    """
    资源池列表分页信息
    """
    def __init__(self, data):
        """
        :param data:
        """
        assert_test(data, 'endRow', 'firstPage', 'hasNextPage', 'hasPreviousPage', 'isFirstPage', 'isLastPage',
                    'lastPage', 'list', 'navigateFirstPage', 'navigateLastPage', 'navigatePages', 'navigatepageNums',
                    'nextPage', 'pageNum', 'pageSize', 'pages', 'prePage', 'size', 'startRow', 'total')
        if data['list']:
            for item in data['list']:
                CrmResourceVO(item)


class CrmResourceVO:
    """
    资源信息列表
    """
    def __init__(self, data):
        """
        :param data:
            actualResourceUserId	integer(int32)	转有效资源人
            actualResourceUserInfo	UserAndDeptDTO	转有效资源人信息	UserAndDeptDTO
            actualResourceUserName	string	转有效资源人名称
            actualResourceUserUpdateTime	string(date-time)	转有效资源人更新时间
            address	string	详细地址
            admissionDate	string(date-time)	入校日期
            area	string	县区
            channels	array	渠道数据	渠道来源与资源关联表对象
            city	string	市
            createTime	string(date-time)	创建时间
            createUserId	integer(int32)	创建人ID
            createUserName	string	创建人名称
            crmChannelSourceId	integer(int32)	到访渠道Id
            crmFollowupLastTime	string(date-time)	最后跟进时间
            crmFollowupRecord	CrmFollowupRecordVO	最近一次跟进记录	CrmFollowupRecordVO
            crmFollowupRecordId	integer(int32)	最后跟进记录id
            crmMembersFamilyId	integer(int32)	家庭组id
            crmMembersFamilyList	array	家庭组信息	CrmResourceVO
            crmMembersFamilyNum	integer(int32)	家庭组成员数
            crmReferrerId	integer(int32)	转介绍人Id
            crmReferrerVO	转介绍人VO	转介绍人信息	转介绍人VO
            crmReferrerVoucherUrls	array	转介绍人凭证urls	string
            crmResourceAllocationRecord	资源分配记录VO	资源最新一条分配记录	资源分配记录VO
            crmResourceLevelCode	string	资源等级编码
            crmResourceLevelId	integer(int32)	资源等级id
            crmResourceLevelName	string	资源等级Name
            crmResourceTypeId	integer(int32)	资源分类id
            crmResourceTypeName	string	资源分类Name
            deposit	number(double)	押金
            details	CrmResourceCustomerDetailVO	详细信息	CrmResourceCustomerDetailVO
            firstVisitInviteId	integer(int32)	首次到访id
            firstVisitTime	string(date-time)	首次到访时间
            followupNum	integer(int32)	总跟进次数
            hasCall	integer(int32)	电话拨打权限1-Y,0-n
            id	integer(int32)	id
            leavingDate	string(date-time)	离校日期
            maintainUserId	integer(int32)	维护人
            maintainUserName	string	维护人名称
            mergeCheckId	integer(int32)	合并审批人id
            mergeCheckInfo	UserAndDeptDTO	合并发起人id	UserAndDeptDTO
            mergeDate	string(date-time)	合并时间
            mergeEndDate	string(date-time)	合并结束时间
            mergeId	integer(int32)	合并id
            mergeName	string	合并后家长名称
            mergeStartDate	string(date-time)	合并发起时间
            mergeUserId	integer(int32)	合并发起人id
            mergeUserInfo	UserAndDeptDTO	合并发起人信息	UserAndDeptDTO
            name	string	名称
            notOptionalReason	string	合并不可选原因
            oldStudentsToSchool	string	是否离校返校
            orgId	integer(int32)	创建人机构
            orgName	string	创建人机构名称
            ownerId	integer(int32)	所属人id
            ownerIdRole	integer(int32)	当前持有者身份 1 资源持有人 2 被共享人(可编辑) 3 被共享人(不可编辑) 4 下属资源
            ownerInfo	UserAndDeptDTO	所属人信息	UserAndDeptDTO
            ownerName	string	所属人Name
            ownerOrgId	integer(int32)	所属人机构名称
            ownerOrgName	string	所属人机构名称
            ownerTypeCode	integer(int32)	资源拥有类型code:1-自己，2-下属，3-本部门，4-下属部门,5-共享给我(可编辑)，6-共享给我（不可编辑）
            parentsToNum	integer(int32)	到场机构数
            phone	string	手机号
            phoneFour	string	手机号4
            phoneThree	string	手机号3
            phoneTwo	string	手机号2
            planFollowupDate	string(date-time)	资源计划跟进日期
            province	string	省
            quitRegistrationDate	string(date-time)	退报日期
            recoveryStatus	string	是否有康复史
            recoveryStatusCode	integer(int32)	是否有康复史
            registrationDate	string(date-time)	报名日期
            remark	string	备注
            resourceAcquireDate	string(date-time)	资源获取日期
            resourceReceiveTime	string(date-time)	资源接收时间
            resourcesAttributionCenterId	integer(int32)	所属中心id
            resourcesAttributionCenterName	string	所属中心Name
            source	integer(int32)	来源:1-自研CRM，2-销售易
            sourceName	string	来源名称
            status	integer(int32)	状态()
            statusName	string	状态()
            studentNum	integer(int32)	学生数量
            students	array	学生数据	资源学生数据VO
            updateTime	string(date-time)	最后修改时间
            updateUserId	integer(int32)	最后修改人
            updateUserName	string	最后修改人
        """
        assert_test(data, 'actualResourceUserId', 'actualResourceUserInfo', 'actualResourceUserName',
                    'actualResourceUserUpdateTime', 'address', 'admissionDate', 'area', 'channels', 'city',
                    'createTime', 'createUserId', 'createUserName', 'crmChannelSourceId', 'crmFollowupLastTime',
                    'crmFollowupRecord', 'crmFollowupRecordId', 'crmMembersFamilyId', 'crmMembersFamilyList',
                    'crmMembersFamilyNum', 'crmReferrerId', 'crmReferrerVO', 'crmReferrerVoucherUrls',
                    'crmResourceAllocationRecord', 'crmResourceLevelCode', 'crmResourceLevelId', 'crmResourceLevelName',
                    'crmResourceTypeId', 'crmResourceTypeName', 'crmMembersFamilyId', 'deposit', 'details',
                    'firstVisitInviteId', 'firstVisitTime', 'followupNum', 'hasCall', 'id', 'leavingDate',
                    'maintainUserId', 'maintainUserName', 'mergeCheckId', 'mergeCheckInfo', 'mergeCheckId', 'mergeDate',
                    'mergeEndDate', 'mergeId', 'mergeName', 'mergeStartDate', 'mergeUserId', 'mergeUserInfo', 'name',
                    'notOptionalReason', 'oldStudentsToSchool', 'orgId', 'orgName', 'ownerId', 'ownerIdRole',
                    'ownerInfo', 'ownerName', 'ownerOrgId', 'ownerOrgName', 'ownerTypeCode', 'parentsToNum', 'phone',
                    'phoneFour', 'phoneThree', 'phoneTwo', 'planFollowupDate', 'province', 'quitRegistrationDate',
                    'recoveryStatus', 'recoveryStatusCode', 'registrationDate', 'remark', 'resourceAcquireDate',
                    'resourceReceiveTime', 'resourcesAttributionCenterId', 'resourcesAttributionCenterName', 'source',
                    'sourceName', 'status', 'statusName', 'studentNum', 'students', 'updateTime', 'updateUserId',
                    'updateUserName')

        if data['actualResourceUserInfo']:
            UserAndDeptDTO(data['actualResourceUserInfo'])
        if data['channels']:
            for item in data['channels']:
                ChannelSourceResourcesAssociationVO(item)


class UserAndDeptDTO:
    """
    转有效资源人信息
    """
    def __init__(self, data):
        """
        :param data:
            deptCode	string	部门编码
            deptId	integer(int32)	部门id
            deptName	string	部门名称
            phone	string	用户手机号
            staffId	integer(int32)	员工id
            userId	integer(int32)	用户id
            userName	string	用户名称
        """
        assert_test(data, 'deptCode', 'deptId', 'deptName', 'phone', 'staffId', 'userId', 'userName')


class ChannelSourceResourcesAssociationVO:
    """
    渠道来源与资源关联表对象
    """
    def __init__(self, data):
        """
        :param data:
            channelId	integer(int32)	渠道来源id
            channelPriority	string	渠道优先级
            channelPriorityName	string	渠道优先级
            channelScenes	string	渠道场景
            channelScenesName	string	渠道场景
            channelSourceName	string	渠道来源名称
            channelSourceName2	string	渠道来源名称2
            id	integer(int32)	主键
            parentChannelId	integer(int32)	父渠道id
            position	integer(int32)	渠道位置
            resourceId	integer(int32)	资源id
        """
        assert_test(data, 'channelId', 'channelPriority', 'channelPriorityName', 'channelScenes', 'channelScenesName',
                    'channelSourceName', 'channelSourceName2', 'id', 'parentChannelId', 'position', 'resourceId')


class ResultOfListOfLabelClassFyObject:
    """
    ResultOfListOf标签分类表对象
    """
    def __init__(self, data):
        """
        :param data:
            code	string
            data	array		标签分类表对象
            msg	string
        """
        assert_test(data, 'code', 'data', 'msg')
        if data['data']:
            for item in data['data']:
                LabelClassFyObject(item)


class LabelClassFyObject:
    """
    标签分类表对象
    """
    def __init__(self, data):
        """
        :param data:
            appId	integer(int32)	应用id
            classifyName	string	分类名称
            classifyType	integer(int32)	标签类型（1:客户标签）
            createTime	string(date-time)	创建时间
            createUserId	integer(int32)	创建人
            currentPage	integer(int32)
            deleteStatus	integer(int32)	删除状态，0：未删，1：已刪
            id	integer(int32)	主键
            orderNum	integer(int32)	显示顺序
            orgId	integer(int32)	机构id
            orgList	array		integer
            pageSize	integer(int32)
            parentId	integer(int32)	上级id
            updateTime	string(date-time)	最后修改时间
            updateUserId	integer(int32)	最后修改人
        """
        assert_test(data, 'appId', 'classifyName', 'classifyType', 'createTime', 'createUserId', 'currentPage',
                    'id', 'orderNum', 'orgId', 'orgList', 'pageSize', 'parentId', 'updateTime', 'updateUserId')


class ResultOfListOfAttributionCenterVO:
    """
    ResultOfListOf归属中心VO
    """
    def __init__(self, data):
        """
        :param data:
            code	string
            data	array		归属中心VO
            msg	string
        """
        assert_test(data, 'code', 'data', 'msg')
        if data['data']:
            for item in data['data']:
                AttributionCenterVO(item)


class AttributionCenterVO:
    """
    归属中心VO
    """
    def __init__(self, data):
        """
        :param data:
            enableStatus	integer(int32)	启用状态，0 ：启用，1：禁用
            id	integer(int32)	id
            name	string	名称
            orgIds	string	组织架构ids
            orgNames	string	组织架构名称
        """
        assert_test(data, 'enableStatus', 'id', 'name', 'orgIds', 'orgNames')
