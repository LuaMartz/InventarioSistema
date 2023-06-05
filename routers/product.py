from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models.product import Product as ProductModel
from service.product import ProductService
from schemas.product import Product

product_router = APIRouter()

#@app.get('/product',tags=['product'],response_model=List[Movie],status_code=200, dependencies=[Depends(JWYBearer())])
@product_router.get('/products',tags=['products'],response_model=List[Product],status_code=200)
def get_product() -> Product:
    db = Session()
    result = ProductService(db).get_product()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@product_router.get('/products/{id}',tags=['products'])
def get_product(id:int = Path(ge=1,le=2000)):
    """this function returns one and only one product for id"""
    db = Session()
    result = ProductService(db).get_product(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
    
@product_router.get('/products/',tags=['products'],response_model=List[Product],status_code=200)
def get_products_by_release_contry(release_contry:str = Query(min_length=3,max_length=15)):
    db = Session()
    result = db.query(ProductModel).filter(ProductModel.release_contry == release_contry).all()
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@product_router.post('/products',tags=['products'],status_code=201,response_model=dict)
def create_product(product:Product)->dict:
    db = Session()
    ProductService(db).create_product(product)
    return JSONResponse(content={"message":"Se ha registrado el producto","status_code":201})

@product_router.put('/products{id}',tags=['products'])
def update_product(id:int,product:Product):
    db =  Session()
    result = ProductService(db).get_product(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    ProductService(db).update_product(id,product)
    return JSONResponse(content={"message":"Se ha modificado el producto con id: {id}"})

@product_router.delete('/products/{id}', tags=['products'], response_model=dict, status_code=200)
def delete_product(id: int)-> dict:
    db = Session()
    result: ProductModel = db.query(ProductModel).filter(ProductModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    ProductService(db).delete_product(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el producto"})