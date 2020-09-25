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

    @unittest.skip('old case\n')
    def test_re(self):
        str1 = ' -cp $CLASSPATH $BASECLASS $MAINCLASS $CONFIG\n'
        pattern = r'\$[A-Z]+'
        # for o in re.finditer(pattern, str1):
        #     print(str1[o.start()+1:o.end()])
        print([str1[o.start() + 1:o.end()] for o in re.finditer(pattern, str1)])

    def test_set(self):
        print('test set and list')
        set_a = set()
        # count = 0
        for i in range(10):
            set_a.add(i)
        print(set_a)
        print(list(set_a))

        list_b = list()
        for j in range(20):
            list_b.append(j)
        for i in range(10):
            list_b.append(i)
        print(list_b)
        print(list(set(list_b)))


if __name__ == '__main__':
    unittest.main()
