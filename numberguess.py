import random

print("Let's play some dice.")

valid = False
killswitch = 0

dicer = input("How many dice would you like to roll? (2-1000, few or many) ")

while not valid and killswitch < 2:
    if dicer.isalpha():
        diced = str(dicer)
        if diced.lower() == "few":
            dice = random.randint(2, 16)
            print(f"You have been given {dice} dice to play.")
            valid = True
        elif diced.lower() == "many":
            dice = random.randint(16, 1000)
            print(f"You have been given {dice} dice to play.")
            valid = True
        else:
            print("Invalid choice, please try again.")
            dicer = input("How many dice would you like to roll? (2-1000, few or many) ")
            killswitch += 1
    elif dicer.isdigit():
        dicey = int(dicer)
        if 1 < abs(dicey) < 1001:
            dice = dicey
            print(f"You have chosen to play {dice} dice.")
            valid = True
        else:
            print("Invalid choice, please try again.")
            dicer = input("How many dice would you like to roll? (2-1000, few or many) ")
            killswitch += 1
    else:
        print("Invalid choice, please try again.")
        dicer = input("How many dice would you like to roll? (2-1000, few or many) ")
        killswitch += 1

while not valid and killswitch >= 2:
    print("As you cannot follow instructions, we will choose for you.")
    choice = random.randint(1, 3)

    if choice == 1:
        dice = random.randint(2, 16)
        print("We have chosen a small amount of dice for you to play.")
        print(f"You have been given {dice} dice to play.")
        valid = True
    elif choice == 2:
        dice = random.randint(16, 1000)
        print("We have chosen a large amount of dice for you to play.")
        print(f"You have been given {dice} dice to play.")
        valid = True
    else:
        dice = 1000000
        print("We have given you one million dice!")
        valid = True

valid = False
killswitch = 0
irregular = False
s = 0
neo = 0
dicesides = []

sider = input("How many sides will the dice have? (8-32, uniform or irregular) ")

while not valid and killswitch < 2:
    if sider.isalpha():
        sided = str(sider)
        if sided.lower() == "uniform":
            sides = random.randint(8, 32)
            print(f"You have been given dice with {sides} sides.")
            valid = True
        elif sided.lower() == "irregular":
            while s < dice:
                neo = random.randint(8, 32)
                dicesides.extend([neo])
                s += 1
            print("You have been given a variety of dice.")
            print(dicesides)
            valid = True
            irregular = True
        else:
            print("Invalid choice, please try again.")
            sider = input("How many sides will the dice have? (8-32, uniform or irregular) ")
            killswitch += 1
    elif sider.isdigit():
        sidey = int(sider)
        if 7 < abs(sidey) < 33:
            sides = sidey
            print(f"You have been given dice with {sides} sides.")
            valid = True
        else:
            print("Invalid choice, please try again.")
            sider = input("How many sides will the dice have? (8-32, uniform or irregular) ")
            killswitch += 1
    else:
        print("Invalid choice, please try again.")
        sider = input("How many sides will the dice have? (8-32, uniform or irregular) ")
        killswitch += 1

while not valid and killswitch >= 2:
    print("As you cannot follow instructions, we will choose for you.")
    choice2 = random.randint(1, 3)

    if choice2 <= 2:
        sides = random.randint(8, 32)
        print(f"We have chosen dice with {sides} sides for you to play.")
        valid = True
    else:
        while s < dice:
            neo = random.randint(8, 32)
            dicesides.extend([neo])
            s += 1
        print("You have been given a variety of dice.")
        print(dicesides)
        valid = True
        irregular = True

q = 0
p = 0
actual = 0
guess = 0

while not irregular and q < dice:
    ultra = random.randint(1, sides)
    actual = int(actual + ultra)
    q += 1

while irregular and q < dice:
    ultra = random.randint(1, dicesides[q])
    actual = int(actual + ultra)
    q += 1

while irregular and p < dice:
    bork = dicesides[p] / 2
    guess = int(guess + bork)
    p += 1

s = 0
r = random.randint(1, 2)
x = 0
y = 0
z = 0

if not irregular and r == 1:
    print("By a flip of the (virtual) coin, the computer will go first.")
    y = round(sides / 2.0 * dice)
    print(f"The computer's guess is: {y}")
    x = int(input("What is yours? "))

elif not irregular and r == 2:
    print("By a flip of the (virtual) coin, you will go first.")
    x = int(input("What is your best guess? "))
    z = round(sides / 2.0 * dice)
    if x > z:
        y = x - 1
    elif x < z:
        y = x + 1
    else:
        z = y
    print(f"The computer's guess is: {y}")

elif irregular and r == 1:
    print("By a flip of the (virtual) coin, the computer will go first.")
    y = guess
    print(f"The computer's guess is: {y}")
    x = int(input("What is yours? "))

elif irregular and r == 2:
    print("By a flip of the (virtual) coin, you will go first.")
    x = int(input("What is your best guess? "))
    z = guess
    if x > z:
        y = x - 1
    elif x < z:
        y = x + 1
    else:
        z = y
    print(f"The computer's guess is: {y}")

print(f"The actual total is: {actual}")

xq = abs(x - actual)
yq = abs(y - actual)

if xq > yq:
    print("Computer has won.")
elif xq < yq:
    print("Player has won!")
else:
    print("A tie?")
