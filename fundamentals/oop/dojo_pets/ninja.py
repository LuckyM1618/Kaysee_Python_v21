from pet import Cat, Dog

class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()

        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()

        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()

        return self

salem = Cat("Salem", "doesn't do tricks", 50, 15)
legion = Ninja("Lucky","Maker",salem,"Cat-O's", "Check Meowt Cat Food")

mr_fluffers = Dog("Mr. Fluffers", "The best tricks", 25, 100)
robert = Ninja("Robert", "Santos", mr_fluffers, "Sweet Boi Treat", "Insanely Expensive Dog Food")

print(salem.name)
print(salem.tricks)
print(salem.health)
print(salem.energy)
salem.sleep()
print(salem.energy)
salem.eat()
print(salem.health)
print(salem.energy)
salem.play()
print(salem.health)
salem.noise()

print(legion.pet.name)
print(legion.pet.tricks)
print(legion.pet.health)
print(legion.pet.energy)
legion.pet.sleep()
print(legion.pet.energy)
legion.pet.eat()
print(legion.pet.health)
print(legion.pet.energy)
legion.pet.play()
print(legion.pet.health)
legion.pet.noise()

print(mr_fluffers.name)
print(mr_fluffers.tricks)
print(mr_fluffers.health)
print(mr_fluffers.energy)
mr_fluffers.sleep()
print(mr_fluffers.energy)
mr_fluffers.eat()
print(mr_fluffers.health)
print(mr_fluffers.energy)
mr_fluffers.play()
print(mr_fluffers.health)
mr_fluffers.noise()

print(robert.pet.name)
print(robert.pet.tricks)
print(robert.pet.health)
print(robert.pet.energy)
robert.pet.sleep()
print(robert.pet.energy)
robert.pet.eat()
print(robert.pet.health)
print(robert.pet.energy)
robert.pet.play()
print(robert.pet.health)
robert.pet.noise()
