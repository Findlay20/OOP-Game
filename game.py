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
        self.HP = self.HP - opponent.DP


while True:

    warrior = Character("Warrior", 60, 30, 40)
    tank = Character("Tank", 100, 20, 10)
    mage = Character("Mage", 40, 30, 20)
    pyro = Character("Pyro", 40, 10, 60)

    player1choice = input("Choose your character: Warrior | Tank | Mage | Pyro ")
 
    player1 = warrior

    player2choice = input("Choose your character: Warrior | Tank | Mage | Pyro ")
 
    player2 = warrior

    print(player1)
    print(warrior)
    print(tank)
    print(mage)
    print(pyro)

    warrior.attack(tank)

    print(warrior)
    print(tank)