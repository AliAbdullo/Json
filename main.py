import json

data = {"Model" : "Malibu", "Rang" : "Qora", "Yil" : 2020,"Narh":40000}
with open('Avto','w') as f:
  json.dump(data,f)
avto=json.dumps(data)
print(avto)

talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
with open('talaba','w') as t:
  json.dump(talaba_json, t)
talaba = json.dumps(talaba_json, indent=3)
ismi= ['ismi']

print(talaba)
