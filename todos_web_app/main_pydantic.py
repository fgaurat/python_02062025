
from pydantic import BaseModel,field_validator,ValidationError

class User(BaseModel):
    id:int
    name:str
    is_active:bool=True
    email:str
    
    @field_validator("email")
    def validate_email(cls,v):
        if '@' not in v:
            raise ValueError('Hooooooo !')
        return v
def main():

    try:
        user = User(id=123,name="Robert",email="toto")
        print(user)
    except ValidationError as e:
        print(e)



        
if __name__=='__main__':
    main()
