class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, tricks, health, energy):
        self.name = name
        self.tricks = tricks
        self.health = health
        self.energy = energy

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25

        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10

        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5

        return self

    # noise() - prints out the pet's sound
    def noise(self):
        pass

class Dog( Pet ):
    def __init__(self, name, tricks, health, energy):
        super().__init__(name, tricks, health, energy)
        self.sound = "::bark::"

    def noise(self):
        print(f"{self.sound}")

        return self



class Cat( Pet ):
    def __init__(self, name, tricks, health, energy):
        super().__init__(name, tricks, health, energy)
        self.sound = "::meow::"

    def noise(self):
        print(f"{self.sound}")

        return self
