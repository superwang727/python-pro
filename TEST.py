import json

# data = {}
# data['code'] = 20000
# data['message'] = '成功'

data = {
    'code': 20000,
    'message': '成功',
    'datalist': {'token':'admin'}
}
print(json.dumps(data, ensure_ascii=False))