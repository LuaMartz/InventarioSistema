from pydantic import BaseModel, Field
from typing import Optional


class Supplier(BaseModel):
    id : Optional[int] = None
    sup_name : str = Field(max_length=15,min_length=3, description="Supplier product name")
    
    class Config:
        schema_extra =  {
            "example":{
                "id":1,
                "name" : "name supplier",
                "address" : "address supplier",
                "phone" : "phone supplier",
                "email" : "email supplier"
            }
        }