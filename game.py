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

    player1choice = input("Player 1! Choose your character: Warrior | Tank | Mage | Pyro \n")
 
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


    player2choice = input("Player 2! Choose your character: Warrior | Tank | Mage | Pyro \n")
 
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


    print("Player 1 has choosen", player1.name)
    print("Player 2 has choosen", player2.name)


    while player1.HP & player2.HP > 0:
        player1_move = input("It's Player 1's turn. Which move would you like to make? ( Attack | other options ) \n")

        match player1_move.lower():
            case "attack":
                player1.attack(player2)
                print("Nice attack! \n ")
    
   

    # print(warrior)
    # print(tank)
    # print(mage)
    # print(pyro)

    # warrior.attack(tank)

    # print(warrior)
    # print(tank)

    exit = input("Thanks for playing! Enter anything to play again or exit to stop. \n")

    match exit.lower():
        case "exit":
            break
        case "stop":
            break