from model.pet import Pet

class NodeABB:
    def __init__(self, pet: Pet):
        self.data = pet
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, pet: Pet):
        if not self.root:
            self.root = NodeABB(pet)
        else:
            self._add(self.root, pet)

    def _add(self, node, pet):
        if pet.id_pet < node.data.id_pet:
            if node.left is None:
                node.left = NodeABB(pet)
            else:
                self._add(node.left, pet)
        else:
            if node.right is None:
                node.right = NodeABB(pet)
            else:
                self._add(node.right, pet)

    def remove(self, id_pet):
        self.root = self._remove(self.root, id_pet)

    def _remove(self, node, id_pet):
        if node is None:
            return node
        if id_pet < node.data.id_pet:
            node.left = self._remove(node.left, id_pet)
        elif id_pet > node.data.id_pet:
            node.right = self._remove(node.right, id_pet)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
        return node

    def list_pets(self):
        pets = []
        self._in_order(self.root, pets)
        return pets

    def _in_order(self, node, pets):
        if node:
            self._in_order(node.left, pets)
            pets.append(node.data)
            self._in_order(node.right, pets)
