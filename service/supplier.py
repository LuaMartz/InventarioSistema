from models.supplier import Supplier as SupplierModel

class SupplierService():
    def __init__(self, db):
        self.db = db

    def get_supplier(self):
        result = self.db.query(SupplierModel).all()
        return result
        
    def create_supplier(self,supplier:SupplierModel):
        new_supplier = SupplierModel(
            supplier_name=supplier.supplier_name.upper(),
            supplier_address=supplier.supplier_address,
            supplier_phone=supplier.supplier_phone
        )
        self.db.add(new_supplier)
        self.db.commit()
        return
    
    def get_supplier_for_id(self,id:int):
        result = self.db.query(SupplierModel).filter(SupplierModel.id == id).first()
        return result