class Animal:

    name:str
    species:str

    def __init__(self,name,species):

        self.name=name
        self.species=species

    def __str__(self):

        return self.name

class lion(Animal):

    def _init_(self,name,species):
        super()._init_(name,species)

    def sound(self):
        print("roar")

lion_instance=lion("lion","carnivorus")

print(lion_instance)
print(lion_instance.sound())