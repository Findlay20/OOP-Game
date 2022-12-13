class Character:
    def __init__(self, name, hp, dp, ap):
        self.name = name
        self.HP = hp
        self.DP = dp
        self.AP = ap
        self.stamina = 100

    def __str__(self):
        return f"{self.name} has {self.HP} health, {self.DP} defence and {self.AP} attack power"

    def attack(self, opponent):
        opponent.HP = opponent.HP - self.AP
        self.HP = self.HP - opponent.DP


class Warrior(Character):        
    def slash(self, opponent):
        opponent.HP = opponent.HP - 35
    
    def strike(self, opponent):
        opponent.HP = opponent.HP - 20 

class Tank(Character):        
    def sword(self, opponent):
        opponent.HP = opponent.HP - 30

class Mage(Character):        
    def sword(self, opponent):
        opponent.HP = opponent.HP - 30

class Pyro(Character):        
    def flamethrower(self, opponent):
        opponent.HP = opponent.HP - 30

class Marksman(Character):
    def shoot(self, opponent):
        opponent.HP = opponent.HP - 40

while True:

    warrior = Warrior("Warrior", 60, 30, 20)
    tank = Tank("Tank", 100, 20, 5)
    mage = Mage("Mage", 40, 30, 10)
    pyro = Pyro("Pyro", 40, 10, 30)
    marksman = Marksman("Marksman", 50, 15, 15)

    print(f"\nWelcome to Terminal Brawl! There are 4 classes to choose from with varying stats: \n\n {warrior} \n {tank} \n {mage} \n {pyro} \n {marksman} \n")

    player1choice = input("\nPlayer 1! Choose your character: Warrior | Tank | Mage | Pyro | Marksman \n")
 
    while True:
        match player1choice.lower():
                case "warrior":
                    player1 = warrior
                    break
                case "tank":
                    player1 = tank
                    break
                case "mage":
                    player1 = mage
                    break
                case "pyro":
                    player1 = pyro
                    break
                case "marksman":
                    player1 = marksman
                    break
        player1choice = input("Unkown input. Player 1! Choose your character from the following options: Warrior | Tank | Mage | Pyro | Marksman \n")


    player2choice = input("\nPlayer 2! Choose your character: Warrior | Tank | Mage | Pyro | Marksman \n")
    
    while True:
        match player2choice.lower():
            case "warrior":
                player2 = warrior
                break
            case "tank":
                player2 = tank
                break
            case "mage":
                player2 = mage
                break
            case "pyro":
                player2 = pyro
                break
            case "marksman":
                player2 = marksman
                break
        player2choice = input("Unkown input. Player 2! Choose your character from the following options: Warrior | Tank | Mage | Pyro | Marksman \n")

    print("\n----------------------------------------------------------")
    print("\n Player 1 has choosen", player1.name)
    print("\n Player 2 has choosen", player2.name)


    while player1.HP > 0 and player2.HP > 0:
        print("\n----------------------------------------------------------")
        
        player1_move = input("\nIt's Player 1's turn. Which move would you like to make? ( Attack | other options ) \n")

        while True:
            match player1_move.lower():
                case "attack":
                    player1.attack(player2)
                    print(f"\n Nice attack! \n")
                    break
                case "slash":
                    player1.slash(player2)
                    break
            player1_move = input("Move not available. Here are your options: Attack, slash ")


            

        print(f" Player 1 is now on {player1.HP if player1.HP > 0 else 0} health. \n Player 2 is now on {player2.HP  if player2.HP > 0 else 0} health")

        if player1.HP <= 0 or player2.HP <= 0:
            break
        
        player2_move = input("\n It's Player 2's turn. Which move would you like to make? ( Attack | other options ) \n")

        while True:
            match player1_move.lower():
                case "attack":
                    player2.attack(player1)
                    print(f"\n Nice attack! \n")
                    break
                case "slash":
                    player2.slash(player1)
                    break
            player1_move = input("Move not available. Here are your options: Attack, slash ")

        print(f" Player 1 is now on {player1.HP if player1.HP > 0 else 0} health. \n Player 2 is now on {player2.HP  if player2.HP > 0 else 0} health")

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