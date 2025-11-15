from backend.infrastructure.entities.FxRateBdo import FxRateBdo
from backend.infrastructure.model.FxRateDto import FxRateDto

class FxRateMapper:

    @staticmethod
    def to_fx_rate_bdo(fx_rate_dto: FxRateDto) -> FxRateBdo:
        return FxRateBdo(
            id = fx_rate_dto.id,
            toCurrency = fx_rate_dto.toCurrency,
            fromCurrency = fx_rate_dto.fromCurrency,
            rate = fx_rate_dto.rate
        )

    @staticmethod
    def to_product_dto(fx_rate_bdo: FxRateBdo) -> FxRateDto:
        return FxRateDto(
            id = fx_rate_bdo.id,
            toCurrency = fx_rate_bdo.toCurrency,
            fromCurrency = fx_rate_bdo.fromCurrency,
            rate = fx_rate_bdo.rate
        )

