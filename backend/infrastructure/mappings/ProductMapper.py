from backend.infrastructure.entities.ProductBdo import ProductBdo
from backend.infrastructure.model.ProductDto import ProductDto

class ProductMapper:

    @staticmethod
    def to_product_bdo(product_dto) -> ProductBdo:
        return ProductBdo(
            id = product_dto.id,
            name = product_dto.name,
            price = product_dto.price,
            weight = product_dto.weight
        )

