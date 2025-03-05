from fastapi import FastAPI
from controller.pets_controller import router as pet_router

app = FastAPI()
app.include_router(pet_router)
