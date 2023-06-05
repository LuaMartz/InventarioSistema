from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from service.supplier import SupplierService
from schemas.supplier import Supplier 
from models.supplier import Supplier as SupplierModel
from config.database import Session

supplier_router = APIRouter()

@supplier_router.get('/suppliers', tags = ['suppliers'], status_code=200)
def get_supplier():
    db = Session()
    result = SupplierService(db).get_supplier()
    return JSONResponse(content=jsonable_encoder(result),status_code = 200)

@supplier_router.get('/supplier_for_id', tags=['suppliers'], status_code=200)
def get_supplier_for_id(id:int):
    db = Session()
    result = SupplierService(db).get_supplier_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code = 200)

@supplier_router.post('/suppliers', tags=['suppliers'], status_code=201)
def create_supplier(supplier:Supplier):
    db = Session()
    SupplierService(db).create_supplier(supplier)
    return JSONResponse(content={"message":"supplier created successfully",'status_code':201}, status_code=201)

@supplier_router.put('/suppliers{id}',tags=['suppliers'])
def update_supplier(id:int,supplier:Supplier):
    db =  Session()
    result = SupplierService(db).get_supplier(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    SupplierService(db).update_supplier(id,supplier)
    return JSONResponse(content={"message":"Se ha modificado el supplier con id: {id}"})

@supplier_router.delete('/suppliers/{id}', tags=['suppliers'], response_model=dict, status_code=200)
def delete_supplier(id: int)-> dict:
    db = Session()
    result: SupplierModel = db.query(SupplierModel).filter(SupplierModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    SupplierService(db).delete_supplier(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el supplier"})

