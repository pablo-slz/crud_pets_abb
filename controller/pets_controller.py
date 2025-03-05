from fastapi import APIRouter
from model.pet import Pet
from service.pet_service import PetService

router = APIRouter()
service = PetService()

@router.post("/pets/")
def add_pet(id_pet: int, name: str, age: int, owner: str):
    pet = Pet(id_pet=id_pet, name=name, age=age, owner=owner)
    return service.add_pet(pet)

@router.get("/pets/")
def list_pets():
    return service.list_pets()

@router.get("/pets/{id_pet}")
def get_pet(id_pet: int):
    pet = service.get_pet(id_pet)
    if pet:
        return pet
    return {"message": "Pet not found"}

@router.put("/pets/{id_pet}")
def edit_pet(id_pet: int, name: str, age: int, owner: str):
    return service.edit_pet(id_pet, name, age, owner)

@router.delete("/pets/{id_pet}")
def remove_pet(id_pet: int):
    return service.remove_pet(id_pet)

@router.get("/pets/tree/")
def list_pets_tree():
    return service.list_pets_tree()
