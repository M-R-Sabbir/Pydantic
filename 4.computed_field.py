
# It is like we derive something or compute something with the existing data
 
from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List,Dict,Optional


class Patient(BaseModel):
    name : str
    age : int
    email: EmailStr                # instead of giving str ,Emailstr restrict user to give proper mail format
    linkdin:AnyUrl                 # make sure that user is giving right format of url
    height: float
    weight : float
    married : bool=False
    things : Optional[list]= None
    allergies : List[str]
    contact : Dict[str,str]


    @computed_field
    @property
    def calculate_bmi(self) -> float:          # defining this is a must
        bmi = round(self.weight/(self.height*self.height),2)
        return bmi


patient_info = {'name':"Sabbir","age":24,"height":1.6,"weight":70.9,"allergies":["Hello","world"],'contact':{"mail":"abc@gmail","call":"1627113136"},
                "married":True,"email":"abc@gmail.com","linkdin":"https://linkdin.com/123"}

patient2 = Patient(**patient_info)

def insertion(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.things)
    print(patient.email)
    print(patient.linkdin)
    print(patient.calculate_bmi) 


insertion(patient2)
