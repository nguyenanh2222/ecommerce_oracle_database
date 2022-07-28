from repo.product import ProductRepo
from schema import ProductReq


class ProductService(ProductRepo):
    def insert_product_service(self, product: ProductReq):
        product = ProductRepo().insert_product_repo(ProductReq(
            created_at=product.created_at,
            created_by=product.created_by,
            updated_at=product.updated_at,
            updated_by=product.updated_by,
            name=product.name,
            description=product.description,
            brand=product.brand,
            category_id=product.category_id,
            quantity=product.quantity,
            images=product.images,
            color=product.color,
            price=product.price,
            size_product=product.size_product))

        return product
