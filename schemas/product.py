from pydantic import BaseModel, Field
from typing import Optional 

class Product(BaseModel):
    id : Optional[int] = None
    name : str = Field(max_length=30,min_length=3)
    brand : str = Field(max_length=30,min_length=3)
    description : str = Field(max_length=30,min_length=3)
    price : float = Field(ge=1,le=10000000)
    entry_date : str  = Field(max_length=15,min_length=3)
    availability : str = Field(max_length=300,min_length=10)
    available_quantity : int = Field(le=10000)

    class Config:
        schema_extra = {
            "example":{
                'id' : 1,
                'name' : 'example',
                'brand': 'example brand',
                'description' : 'example description' ,
                'price' : 25000,
                'entry_date' : 1205223,
                'availability' : 'availability' ,
                'available_quantity' : 5
            }
        }