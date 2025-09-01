class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # keep track of pets owned by this owner

    def pets(self):
        """Return all pets belonging to this owner"""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to this owner, validating type"""
        if not isinstance(pet, Pet):
            raise Exception("add_pet() requires a Pet instance")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        """Return pets sorted alphabetically by name"""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = None  # will be set below

        # If an owner was passed, validate and set it
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("owner must be an Owner instance")
            self.owner = owner
            owner.pets().append(self)

        # Track every pet created
        Pet.all.append(self)
