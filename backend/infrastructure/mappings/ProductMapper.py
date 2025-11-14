from backend.infrastructure.entities.ProductBdo import ProductBdo
from backend.infrastructure.model.ProductDto import ProductDto

class ProductMapper:

    @staticmethod
    def to_product_bdo(product_dto) -> ProductBdo:
        return ProductBdo(
            id = product_dto.id,
            name = product_dto.name,
            cost = product_dto.cost,
            fxRateId = product_dto.fxRateId
        )

    @staticmethod
    def to_product_dto(product_bdo) -> ProductDto:
        return ProductDto(
            id = product_bdo.id,
            name = product_bdo.name,
            cost = product_bdo.cost,
            fxRateId = product_bdo.fxRateId
        )

