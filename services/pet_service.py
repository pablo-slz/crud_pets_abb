from models.pet_models import Pet

# Base de datos en memoria
pets_db = []

# Definición del Nodo del Árbol Binario
class Node:
    def __init__(self, pet: Pet):
        self.pet = pet
        self.left = None
        self.right = None

# Clase del Árbol Binario de Búsqueda (BST)
class PetBST:
    def __init__(self):
        self.root = None
        self.insertion_log = []  # 📌 Registro de inserciones

    def insert(self, pet: Pet):
        self.insertion_log.append(f"Insertando {pet.name} con edad {pet.age}")
        if not self.root:
            self.root = Node(pet)
            self.insertion_log.append(f"→ {pet.name} es la raíz del árbol")
        else:
            self._insert(self.root, pet)

    def _insert(self, current: Node, pet: Pet):
        if pet.age < current.pet.age:
            if current.left:
                self._insert(current.left, pet)
            else:
                current.left = Node(pet)
                self.insertion_log.append(f"→ {pet.name} ({pet.age}) va a la IZQUIERDA de {current.pet.name} ({current.pet.age})")
        else:
            if current.right:
                self._insert(current.right, pet)
            else:
                current.right = Node(pet)
                self.insertion_log.append(f"→ {pet.name} ({pet.age}) va a la DERECHA de {current.pet.name} ({current.pet.age})")

    def inorder_traversal(self, node=None, pets_sorted=None):
        if pets_sorted is None:
            pets_sorted = []
        if node is None:
            node = self.root

        if node:
            self.inorder_traversal(node.left, pets_sorted)
            pets_sorted.append(node.pet)
            self.inorder_traversal(node.right, pets_sorted)

        return pets_sorted

    def get_insertion_log(self):
        return self.insertion_log if self.insertion_log else ["El árbol está vacío."]

# Instancia del árbol binario
pets_bst = PetBST()

# Funciones CRUD
def create_pet(pet: Pet):
    pets_db.append(pet)
    pets_bst.insert(pet)
    return pet

def get_pets():
    return pets_db

def get_pet_by_id(id_pet: int):
    for pet in pets_db:
        if pet.id_pet == id_pet:
            return pet
    return None

def update_pet(id_pet: int, pet_data: Pet):
    for i, pet in enumerate(pets_db):
        if pet.id_pet == id_pet:
            pets_db[i] = pet_data
            return pet_data
    return None

def delete_pet(id_pet: int):
    global pets_db
    pets_db = [pet for pet in pets_db if pet.id_pet != id_pet]
    return {"message": f"Pet con ID {id_pet} eliminada"}

