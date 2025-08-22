from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# custom imports
from app.api import routes_predict, routes_auth
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(
    title="Car Price Prediction API",
    description="This API predicts the price of a car based on its features.",
)

# link mdiddleware
app.add_middleware(LoggingMiddleware)

# link api endpoints
app.include_router(routes_predict.router, tags=["prediction"])
app.include_router(routes_auth.router, tags=["Authorization"])


# monitoring with prometheus
Instrumentator().instrument(app).expose(app)

# add exeception handler
register_exception_handlers(app)
