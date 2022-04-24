import random
print("Welcome to Zippy Roulette.")
playerName = input(str("Please enter your name: "))
print("Welcome to the game", playerName)


def get_bet():

    bet_typ = input(
        "Enter the assigned number for your chosen bet type.\n"
        "0 = Done, 1 = Color, 2 = Odd/Even, 3 = Inside Number: "
    )

    if not bet_typ.isnumeric():
        print("Invalid Input")
        return "invalid"
    else:
        bet_typ = int(bet_typ)

    bet_choice = ""

    if bet_typ == 1:
        bet_choice = input("Enter color; red or black: ")
    elif bet_typ == 2:
        bet_choice = input("Enter odd or even: ")
    elif bet_typ == 3:
        bet_choice = input("Enter inside number; 0-36: ")
    elif bet_typ == 0:
        return "done"
    else:
        print("Invalid bet type")
        return "invalid"

    bet_amt = bet_amnt()
    
    return {"type": bet_typ, "choice": bet_choice, "amount": bet_amt}

def bet_amnt():
    bet_amount = float(input(
        "Enter bet amount for your chosen bet.\n"
        "The maximum bet amount is $5 and minimum bet amount is $100: $"
    ))
    while (bet_amount < 5) or (bet_amount > 100):
        print("Error: The bet amount is invalid.")
        bet_amount = float(input(
            "Enter bet amount for your chosen bet.\n"
            "The maximum bet amount is $5 and minimum bet amount is $100: $"
    ))
    return(bet_amount)
def get_color(num):
    red_num = [
        "1",
        "3",
        "5",
        "7",
        "9",
        "12",
        "14",
        "16",
        "18",
        "19",
        "21",
        "23",
        "25",
        "27",
        "30",
        "32",
        "34",
        "36",
    ]

    if num in red_num:
        return "red"

    else:
        return "black"


def get_odd_even(num):
    if (num % 2) == 0:
        return "even"
    else:
        return "odd"


def roll():
    return random.randint(0, 36)


def earning_bet(bet, roll):
    print(playerName, "earning_bet", bet, roll)
    print(playerName,": type of bet amount:", type(bet["amount"]))
    if bet["type"] == 1:
        color = get_color(roll)
        if bet["choice"] == color:
            return int(bet["amount"])
        else:
            return -(int(bet["amount"]))
    elif bet["type"] == 2:
        odd_even = get_odd_even(roll)
        if bet["choice"] == odd_even:
            return int(bet["amount"])
        else:
            return -(int(bet["amount"]))
    elif bet["type"] == 3:
        if bet["choice"] == roll:
            return int(bet["amount"])
        else:
            return -(int(bet["amount"]))


# start of main program
bets = []
i = 0

while 1:
    print(f"Enter bet number {i+1}: ")
    bet = get_bet()
    if bet == "done":
        break
    elif bet == "invalid":
        continue

    bets.append(bet)
    i = i + 1

# print(bets)
r = roll()

earnings = 0

for b in bets:
    e = earning_bet(b, r)
    earnings = earnings + e


print(f"Your total earnings are: ${earnings}")

