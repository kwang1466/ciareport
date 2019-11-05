# this package is for Cast Objects

class CastObj(object):
    """docstring for CastObj"""
    def __init__(self, id, name, obj_type, full_name):
        super(CastObj, self).__init__()
        self.id = id
        self.name = name
        self.obj_type = obj_type
        self.full_name = full_name 
        

class ImpactObj(CastObj):
    """docstring for ImpactObj"""
    def __init__(self, id, name, obj_type, full_name, link_type=''):
        super(ImpactObj, self).__init__()
        self.link_type = link_type


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
        
        