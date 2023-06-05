from models.supplies import Supplies as SuppliesModel

class SuppliesService():
    def __init__(self, db):
        self.db = db

    def get_supplies(self):
        result = self.db.query(SuppliesModel).all()
        return result
        
    def create_supplies(self,supplies:SuppliesModel):
        new_supplies = SuppliesModel(
            supplier_id = supplies.supplier_id,
            product_id = supplies.product_id,
            purchase_price = supplies.purchase_price,
        )
        self.db.add(new_supplies)
        self.db.commit()
        return
    
    def get_supplies_for_id(self,id:int):
        result = self.db.query(SuppliesModel).filter(SuppliesModel.id == id).first()
        return result