from collections import OrderedDict


ordered_dict_obj = OrderedDict()
ordered_dict_obj['abc'] = 1
ordered_dict_obj['bdc'] = 2
ordered_dict_obj['cde'] = 3


normal_dict_obj = {'abc': 1, 'bdc': 2, 'cde': 3}

# print(ordered_dict_obj)
for k, v in ordered_dict_obj.items():
    print('{}: {}'.format(k, v))

print(normal_dict_obj)
