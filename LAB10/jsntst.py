import json
a={"name":"Ayush","age":21}
b=json.dumps(a)
c=json.loads(b)
print(b)
print(c)
