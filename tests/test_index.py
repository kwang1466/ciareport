import unittest
from collections import defaultdict
import re


class TestString(unittest.TestCase):

    @unittest.skip('old case\n')
    def test_index(self):
        str1 = 'memberUrl2) + "api/Company/SearchLikeCompany'
        str2 = str1[str1.index('"') + 1:]
        print(str2)

    @unittest.skip('old case\n')
    def test_dict(self):
        temdict = dict()
        a = [1, 2, 3, 4]
        b = ['a', 'b', 'c', 'd']
        for o, v in zip(b, a):
            temdict[o] = v
        for o in temdict.keys():
            print('{}:{}'.format(o, temdict[o]))
        # print(temdict['b'])

    def test_re(self):
        str1 = ' -cp $CLASSPATH $BASECLASS $MAINCLASS $CONFIG\n'
        pattern = r'\$[A-Z]+'
        # for o in re.finditer(pattern, str1):
        #     print(str1[o.start()+1:o.end()])
        print([str1[o.start() + 1:o.end()] for o in re.finditer(pattern, str1)])

if __name__ == '__main__':
    unittest.main()
