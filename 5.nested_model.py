
# sometimes we can't do everything with the string or int ,we need some more type of data ,that can be made custom
# like address have different different information,if we store the whole as a string ,extracting specific info let's road number is hard
# so we make a class for address and use it as a data type in our main class

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

print(patient_1)

print(patient_1.name)
print(patient_1.address.city)