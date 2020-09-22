# this package is for Cast Objects


class CastObj(object):

    """docstring for CastObj"""

    def __init__(self, id, name, obj_type, full_name):
        super(CastObj, self).__init__()
        self.id = id
        self.name = name
        self.obj_type = obj_type
        self.full_name = full_name


class ImpactObj(object):

    """docstring for ImpactObj"""

    # def __init__(self, source_id, source_file, target_id, target_file, caller_name,
    #              caller_fullname, callee_name, callee_fullname,
    #              call_level, call_way):
    #     super(ImpactObj, self).__init__()
    #     self.source_id = source_id
    #     self.source_file = source_file
    #     self.target_id = target_id
    #     self.target_file = target_file
    #     self.caller_name = caller_name
    #     self.caller_fullname = caller_fullname
    #     self.callee_name = callee_name
    #     self.callee_fullname = callee_fullname
    #     self.call_level = call_level
    #     self.call_way = call_way

    def __init__(self, source_id, source_file, target_file, source_name,
                 source_fullname, target_name, target_fullname,
                 call_level, call_way):
        super(ImpactObj, self).__init__()
        self.source_id = source_id
        self.source_file = source_file
        # self.target_id = target_id
        self.target_file = target_file
        self.source_name = source_name
        self.source_fullname = source_fullname
        self.target_name = target_name
        self.target_fullname = target_fullname
        self.call_level = call_level
        self.call_way = call_way


class ChangedObj(object):

    """docstring for ChangedObj"""
    # obj_type is not like normal obj_type
    # instead of technology type when status is 'deleted'

    # def __init__(self, lid, cid, file_path, full_name, module,
    #              snapshot, status, obj_type):
    #     super(ChangedObj, self).__init__()
    #     self.local_id = lid
    #     self.central_id = cid
    #     self.file_path = file_path
    #     self.full_name = full_name
    #     self.module = module
    #     self.snapshot = snapshot
    #     self.status = status
    #     self.obj_type = obj_type

    def __init__(self, lid, full_name, file_path, status, obj_type):
        super(ChangedObj, self).__init__()
        self.local_id = lid
        # self.central_id = cid
        self.file_path = file_path
        self.full_name = full_name
        # self.module = module
        # self.snapshot = snapshot
        self.status = status
        self.obj_type = obj_type


class TargetFile(object):

    def __init__(self, target_file_name):
        super(TargetFile, self).__init__()
        self.target_file = target_file_name
