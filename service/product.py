from models.product import Product as ProductModel
from schemas.product import Product

class ProductService():
    def __init__(self,db) -> None:
        self.db = db

    def get_product(self):
        result = self.db.query(ProductModel).all()
        return result

    def get_product(self,id:int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result

    def get_movies_by_release_contry(self,release_contry:str):
        result = self.db.query(ProductModel).filter(ProductModel.release_contry == release_contry).all()
        return result        

    def create_product(self, product:Product):
        new_product = ProductModel()
        id : id.product_id
        name : name.product_name
        brand : brand.product_brand
        description : description.product_description
        price : price.product_price
        entry_date : entry_date.product_entry_date
        availability : availability.product_availability
        available_quantity : available_quantity.product_quantity
        
        self.db.add(new_product)
        self.db.commit()
        return

    def update_product(self,id:int, data:Product):
        product = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        product.name = data.name
        product.brand = data.brand
        product.description = data.description
        product.price = data.price
        product.entry_date = data.entry_date
        product.availability = data.availability
        product.available_quantity = data.available_quantity
        self.db.commit()
        return

    def delete_product(self, id: int):
       self.db.query(ProductModel).filter(ProductModel.id == id).delete()
       self.db.commit()
       return