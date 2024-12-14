class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if value in Pet.PET_TYPES:
            self._pet_type = value
        else:
            raise Exception
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if value is None or isinstance(value, Owner):
            self._owner = value
        else:
            raise Exception

class Owner:

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception


brooke = Pet("Brooke", "cat")
buster = Pet("Buster", "cat")
baxter = Pet("Baxter", "reptile")

lola = Pet("Lola", "dog")

jacqueline = Owner("Jacqueline")
kevin = Owner("Kevin")
ally = Owner("Ally")

jacqueline.add_pet(brooke)
kevin.add_pet(buster)
kevin.add_pet(baxter)
ally.add_pet(lola)

print(jacqueline.pets)
print(kevin.get_sorted_pets())

owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)

print(owner.get_sorted_pets())