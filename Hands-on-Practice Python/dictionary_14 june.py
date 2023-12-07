#dictionary-association- key-value pairs
phone={"amit":982537,"sumit":987654321,"riya":1234567}
print(phone)

info={}
info["name"]="sandy"
info["desg"]="professor"
print(info)
info["desg"]="manager"
info["occupation"]="manager"
print(info)
'''print(info["desg"])
if "job" in info:
    print(info["job"])
else:
    print("no job")

#get

print(info.get("desg",None))
print(info.get("job",None))

#remove keys
print(info.pop("job",None))
#print(info.pop("desg"))
print(info)
#dictionary elements
for key in info:
    print(key,info[key])

print(list(info.items()))

for (key,value) in info.items():
    print(key,value)

print(list(info.keys()))
print(list(info.values()))
for key in list(info.keys()):
    print(info[key])

#len(info)
#info.clear()
#print(info)
info={'name':['amit','sumit','abhi'],'desg':'manager'}
print(info)
print(type(info))

#use of dict keyword

info=dict(name='amit',age=18)
print(info)'''












    

