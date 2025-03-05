from model.pet import Pet
from model.abb import BinarySearchTree

class PetService:
    def __init__(self):
        self.pets = []
        self.tree = BinarySearchTree()

    def add_pet(self, pet: Pet):
        self.pets.append(pet)
        self.tree.add(pet)
        return {"message": "Pet added"}

    def list_pets(self):
        return self.pets

    def get_pet(self, id_pet: int):
        for pet in self.pets:
            if pet.id_pet == id_pet:
                return pet
        return None

    def edit_pet(self, id_pet: int, name: str, age: int, owner: str):
        for pet in self.pets:
            if pet.id_pet == id_pet:
                pet.name = name
                pet.age = age
                pet.owner = owner
                return {"message": "Pet updated"}
        return {"message": "Pet not found"}

    def remove_pet(self, id_pet: int):
        self.pets = [pet for pet in self.pets if pet.id_pet != id_pet]
        self.tree.remove(id_pet)
        return {"message": "Pet removed"}

    def list_pets_tree(self):
        return self.tree.list_pets()
