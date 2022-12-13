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

    print(f"Welcome to Terminal Brawl! There are 5 classes to choose from with varying stats: \n {warrior} \n {tank} \n {mage} \n {pyro}")

    player1choice = input("Player 1! Choose your character: Warrior | Tank | Mage | Pyro ")
 
    match player1choice.lower():
        case "warrior":
            player1 = warrior
        case "tank":
            player1 = tank
        case "mage":
            player1 = mage
        case "pyro":
            player1 = pyro
        case other:
            print("Unkown choice, exiting...")
            break


    player2choice = input("Player 2! Choose your character: Warrior | Tank | Mage | Pyro ")
 
    match player2choice.lower():
        case "warrior":
            player2 = warrior
        case "tank":
            player2 = tank
        case "mage":
            player2 = mage
        case "pyro":
            player2 = pyro
        case other:
            print("Unkown choice, exiting...")
            break


    print(player1)
    print(player2)

    # print(warrior)
    # print(tank)
    # print(mage)
    # print(pyro)

    # warrior.attack(tank)

    # print(warrior)
    # print(tank)