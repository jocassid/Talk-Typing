
class Animal: pass

class Mammal(Animal): pass
class Dog(Mammal): pass
class Cat(Mammal): pass

class Reptile(Animal): pass
class Snake(Reptile): pass
class Turtle(Reptile): pass

def main() -> None:
    animals: list[Animal] = [Dog(), Cat(), Snake(), Turtle()]
    mammals: list[Mammal] = [Dog(), Cat()]
    not_entirely_mammals: list[Mammal] = [Dog(), Turtle()]  # TYPE ERROR Turtles are not mammals

if __name__ == "__main__":
    main()
