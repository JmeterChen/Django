# coding=utf-8
# @Author:ChenBo lin

import json

# 序列化与反序列化

# 把字典拼成json格式的字符串 ---序列化
# json.dumps()

#  --写入文件
json.dump()

data = {'info': '我的'}
print ((json.dumps(data),))


# json字符串，转成字典   ---反序列化
# json.loads()


sorce = '{"info": "123"}'

print(type(json.loads(sorce)))

# 从某个文件读取
json.load()