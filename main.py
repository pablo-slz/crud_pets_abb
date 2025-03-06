from fastapi import FastAPI
from controllers.pet_controller import router as pet_router

app = FastAPI()

app.include_router(pet_router)
