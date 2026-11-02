

from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state: str
    road : int

class Patient(BaseModel):
    name: str
    age: int
    gender :str
    address : Address  # this is an address type data

add_dict = {"city": "Hyderabad","state":"Telangana","road":1212}
address_1 = Address(**add_dict)

patient_dict = {"name":"Sabbir","age":24,"gender":"Male","address":address_1}
patient_1 = Patient(**patient_dict)


###########
temp1 = patient_1.model_dump()
print(temp1)
print(type(temp1))

temp2 = patient_1.model_dump_json()
print(temp2)
print(type(temp2))


# In dictionary adding we can choose whatever I wanna include using keys.

temp = patient_1.model_dump(include=["name","address"])
print(temp)


# we can exclude some items and export the rest


temp = patient_1.model_dump(exclude=["name","address"])
print(temp)

# now I want to export all except state


temp = patient_1.model_dump(exclude={"address":["state"]})
print(temp)

# another parameter is (exclude_unset=True)
# which are set by default user don't pass data, that won't be exported