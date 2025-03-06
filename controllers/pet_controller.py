from fastapi import APIRouter
from models.pet_models import Pet
from services.pet_service import create_pet, get_pets, get_pet_by_id, update_pet, delete_pet, pets_bst

router = APIRouter()

@router.post("/pets/")
def add_pet(pet: Pet):
    return create_pet(pet)

@router.get("/pets/")
def list_pets():
    return get_pets()

@router.get("/pets/{id_pet}")
def retrieve_pet(id_pet: int):
    pet = get_pet_by_id(id_pet)
    if pet:
        return pet
    return {"error": "Pet not found"}

@router.put("/pets/{id_pet}")
def edit_pet(id_pet: int, pet: Pet):
    updated_pet = update_pet(id_pet, pet)
    if updated_pet:
        return updated_pet
    return {"error": "Pet not found"}

@router.delete("/pets/{id_pet}")
def remove_pet(id_pet: int):
    return delete_pet(id_pet)

@router.get("/pets/sorted/")
def get_sorted_pets():
    return pets_bst.inorder_traversal()

@router.get("/pets/tree/log/")
def get_tree_log():
    return {"Construcción del Árbol": pets_bst.get_insertion_log()}

