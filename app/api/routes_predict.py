from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.dependencies import get_api_key, get_current_user
from app.services.model_service import predict_car_price

router = APIRouter()


class CarFeatures(BaseModel):
    company: str
    year: int
    owner: str
    fuel: str
    seller_type: str
    transmission: str
    km_driven: float
    mileage_mpg: float
    engine_cc: float
    max_power_bhp: float
    torque_nm: float
    seats: float


@router.post("/predict")
def car_price_prediction(
    data: CarFeatures,
    api_key: str = Depends(get_api_key),
    current_user: str = Depends(get_current_user),
):
    data_dict = data.model_dump()
    prediction = predict_car_price(data_dict)
    return {"predicted_price": f"Rs. {prediction:,}"}  # {prediction}
