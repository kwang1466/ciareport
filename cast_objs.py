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
    def __init__(self, source_id, target_id, caller_name,
                 caller_fullname, callee_name, callee_fullname,
                 call_level, call_way):
        super(ImpactObj, self).__init__()
        self.source_id = source_id
        self.target_id = target_id
        self.caller_name = caller_name
        self.caller_fullname = caller_fullname
        self.callee_name = callee_name
        self.callee_fullname = callee_fullname
        self.call_level = call_level
        self.call_way = call_way


class ChangedObj(object):
    """docstring for ChangedObj"""
    # obj_type is not like normal obj_type 
    # instead of technology type when status is 'deleted'
    def __init__(self, lid, cid, full_name, module, 
                 snapshot, status, obj_type):
        super(ChangedObj, self).__init__()
        self.local_id = lid
        self.central_id = cid
        self.full_name = full_name
        self.module = module
        self.snapshot = snapshot
        self.status = status
        self.obj_type = obj_type
        
        