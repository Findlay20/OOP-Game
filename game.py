class Character:
    def __init__(self, name, hp, dp, ap):
        self.name = name
        self.HP = hp
        self.DP = dp
        self.AP = ap

    def __str__(self):
        return f"{self.name} has {self.HP} health, {self.DP} defence and {self.AP} attack power"

    def attack(self, opponent):
        opponent.HP = opponent.HP - self.AP

player = input("")

warrior = Character("Warrior", 60, 30, 20)
tank = Character("Tank", 100, 40, 10)
mage = Character("Mage", 40, 30, 20)
pyro = Character("Pyro", 40, 10, 60)


print(player1)