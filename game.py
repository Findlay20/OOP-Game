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

    warrior = Character("Warrior", 60, 30, 20)
    tank = Character("Tank", 100, 20, 5)
    mage = Character("Mage", 40, 30, 10)
    pyro = Character("Pyro", 40, 10, 30)

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


    while player1.HP > 0 and player2.HP > 0:
        player1_move = input("It's Player 1's turn. Which move would you like to make? ( Attack | other options ) \n")

        match player1_move.lower():
            case "attack":
                player1.attack(player2)
                print(f"Nice attack! \n Player 1 is now on {player1.HP if player1.HP > 0 else 0} health. \n Player 2 is now on {player2.HP  if player2.HP > 0 else 0} health")
            
        if player1.HP <= 0 or player2.HP <= 0:
            break
        
        player2_move = input("It's Player 2's turn. Which move would you like to make? ( Attack | other options ) \n")

        match player2_move.lower():
            case "attack":
                player2.attack(player1)
                print(f"Nice attack! \n Player 1 is now on {player1.HP if player1.HP > 0 else 0} health. \n Player 2 is now on {player2.HP if player2.HP > 0 else 0} health")


    if player1.HP > player2.HP:
        print("Congratulations, Player 1 has won the game!")
    elif player1.HP == player2.HP:
        print("Congratulations to both players. The game has finished in a draw!")
    else:
        print("Congratulations, Player 2 has won the game!")

    exit = input("Thanks for playing! Enter anything to play again or exit to stop. \n")

    match exit.lower():
        case "exit":
            break
        case "stop":
            break