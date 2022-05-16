from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import database
from .routers import products, sellers, user
from app.api.routes.api import router as api_router
from app.core.events import create_start_app_handler, create_stop_app_handler


def get_application() -> FastAPI:
    #settings = get_app_settings()

    settings.configure_logging()

    application = FastAPI(**settings.fastapi_kwargs)



    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings),
    )
    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application),
    )

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=settings.api_prefix)

    application.mount("/", StaticFiles(directory="templates"))


    return application


app = get_application()


# async def get_token_header(x_token: str = Header(...)):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token header invalid")


@app.get("/")
async def main():
    return {"message": "Backend works"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# app.include_router(
#     auth.router,
#     prefix="/auth",
#     tags=["Auth"],
# )

app.include_router(
    products.router,
    prefix="/product",
    tags=["products"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "no products"}},
)

app.include_router(
    sellers.router,
    prefix="/seller",
    tags=["sellers"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "no sellers"}},
)
app.include_router(
    user.router,
    prefix="/user",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "no users"}},
)
origins = [
    "http://localhost",
    "http://localhost:3000",
]
