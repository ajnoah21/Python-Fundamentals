class Actor:
    def __init__(self, name="", health=10, attack_damage = 2):
        self.health = health
        self.attack_damage = attack_damage
        self.name = name
    def __str__(self):
        return f"{self.name} has {self.health} hitpoints and can do {self.attack_damage} damage.\n"

    def attack(self, actor2):
        actor2.health -= self.attack_damage
    
    def defend(self, actor2):
        self.health -= actor2.attack_damage

def do_something():
    print("I'm doing stuff, I promise.\n")

def main():
    corin = Actor("Corin", 20, 5)
    someoneelse = Actor("TheOtherGuy")
    print(corin)
    print(someoneelse)

    corin.defend(someoneelse)
    print(corin)
    print(someoneelse)

if __name__ == "__main__":
    main()


