import json
info={'pishro': ['HSHA']}
str_info=json.dumps(info)
print(str_info,type(str_info))


c_info=json.loads(str_info)
print(c_info,type(c_info))