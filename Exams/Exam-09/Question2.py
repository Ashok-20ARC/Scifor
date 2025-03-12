import json

class Person:
    def __init__(self,name,age,city,married):
        self.name=name
        self.age=age
        self.city=city
        self.married=married

def json_data(obj):
    if isinstance(obj,Person):
        return obj.__dict__
    else:
        print("Error")

person=Person('Ashok',21,'Tamilnadu',False)

json_person=json.dumps(person,default=json_data,indent=4)

print(person.__dict__)
print(json_person)
        