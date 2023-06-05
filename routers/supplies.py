from fastapi import APIRouter,Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from service.supplies import SuppliesService
from schemas.supplies import Supplies
from models.supplies import Supplies as SuppliesModel
from config.database import Session

supplies_router = APIRouter()

@supplies_router.get('/supplies', tags = ['supplies'], status_code=200)
def get_supplies():
    db = Session()
    result = SuppliesService(db).get_supplies()
    return JSONResponse(content=jsonable_encoder(result),status_code = 200)

@supplies_router.get('/supplies_for_id', tags=['supplies'], status_code=200)
def get_supplies_for_id(id:int):
    db = Session()
    result = SuppliesService(db).get_supplies_for_id(id)
    return JSONResponse(content=jsonable_encoder(result),status_code = 200)

@supplies_router.post('/supplies', tags=['supplies'], status_code=201)
def create_supplies(supplier:Supplies):
    db = Session()
    SuppliesService(db).create_supplies(supplier)
    return JSONResponse(content={"message":"supplies created successfully",'status_code':201}, status_code=201)

@supplies_router.put('/supplies{id}',tags=['supplies'])
def update_supplies(id:int,supplies:Supplies):
    db =  Session()
    result = SuppliesService(db).get_supplies(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado el registro","status_code":"404"})
    SuppliesService(db).update_supplies(id,supplies)
    return JSONResponse(content={"message":"Se ha modificado el supplies con id: {id}"})

@supplies_router.delete('/supplies/{id}', tags=['supplies'], response_model=dict, status_code=200)
def delete_supplies(id: int)-> dict:
    db = Session()
    result: SuppliesModel = db.query(SuppliesModel).filter(SuppliesModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No se encontró"})
    SuppliesService(db).delete_supplier(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el supplies"})