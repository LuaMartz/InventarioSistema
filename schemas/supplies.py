from pydantic import BaseModel, Field
from typing import Optional

class Supplies(BaseModel):
    supplier_id : int = Field(ge=1,description="llave foranea de supplier id")
    product_id : int = Field(ge=1,description="llave foranea de producto id")
    purchase_price : float = Field(ge=1)

    class Config:
        schema_extra = {
            "example":{
                "supplier_id": 1,
                "product_id": 1,
                "purchase_price": 1000
            }
        }