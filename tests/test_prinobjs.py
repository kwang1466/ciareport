import unittest


class CastObj(object):
    """docstring for CastObj"""
    def __init__(self, id, name, obj_type, full_name):
        super(CastObj, self).__init__()
        self.id = id
        self.name = name
        self.obj_type = obj_type
        self.full_name = full_name 

    def abc(self):
        print('abc')

class TestPrintObjs(unittest.TestCase):

    def test_pritobjs(self):
        obj = CastObj(123, 'test', 'java method', 'com.demo.test')
        # print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))
        # for k, v in enumerate(obj.__dict__.keys()):
        #     print('{}:{}'.format(k, v))
        # print(obj.__dict__.keys())
        for o in obj.__dict__.keys():
            print(o)
        # print(obj.__dict__.values())


if __name__ == "__main__":
    unittest.main()
