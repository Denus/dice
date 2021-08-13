from random import randint

print "Let's play some dice."

valid = False
killswitch = 0

dicer = raw_input("How many dice would you like to roll? (2-1000, few or many) ")

while valid == False and killswitch < 2:

  if dicer.isalpha() is True:
      diced = str(dicer)
      if diced.lower() == "few":
          dice = randint (2,16)
          print "You have been given {} dice to play.".format(dice)
          valid = True
      elif diced.lower() == "many":
          dice = randint (16,1000)
          print "You have been given {} dice to play.".format(dice)
          valid = True
      else:
          print "Invalid choice, please try again."
          dicer = raw_input("How many dice would you like to roll? (2-1000, few or many) ")
          killswitch += 1

  elif dicer.isdigit() is True:
      dicey = int(dicer)
      if abs(dicey) > 1 and abs(dicey) < 1001:
          dice = dicey
          print "You have chosen to play {} dice.".format(dice)
          valid = True
      else:
          print "Invalid choice, please try again."
          dicer = raw_input("How many dice would you like to roll? (2-1000, few or many) ")
          killswitch += 1

  else:
      print "Invalid choice, please try again."
      dicer = raw_input("How many dice would you like to roll? (2-1000, few or many) ")
      killswitch += 1

while valid == False and killswitch >= 2:
    print "As you cannot follow instructions, we will choose for you."
    choice = randint (1,3)

    if choice == 1:
         dice = randint (2,16)
         print "We have chosen a small amount of dice for you to play."
         print "You have been given {} dice to play.".format(dice)
         valid = True
    elif choice == 2:
        dice = randint (16,1000)
        print "We have chosen a large amount of dice for you to play."
        print "You have been given {} dice to play.".format(dice)
        valid = True
    else:
        dice = 1000000
        print "We have given you one million dice!"
        valid = True

valid = False
killswitch = 0
irregular = False
s = 0
neo = 0
dicesides = []

sider = raw_input("How many sides will the dice have? (8-32, uniform or irregular) ")

while valid == False and killswitch < 2:

 if sider.isalpha() is True:
     sided = str(sider)
     if sided.lower() == "uniform":
         sides = randint (8,32)
         print "You have been given dice with {} sides.".format(sides)
         valid = True
     elif sided.lower() == "irregular":
         while s < dice:
             neo = randint (8,32)
             dicesides.extend([neo])
             s += 1
         print "You have been given a variety of dice."
         print dicesides
         valid = True
         irregular = True
     else:
         print "Invalid choice, please try again."
         sider = raw_input("How many sides will the dice have? (8-32, uniform or irregular) ")
         killswitch += 1

 elif sider.isdigit() is True:
     sidey = int(sider)
     if abs(sidey) > 7 and abs(sidey) < 33:
         sides = sidey
         print "You have been given dice with {} sides.".format(sides)
         valid = True
     else:
         print "Invalid choice, please try again."
         sider = raw_input("How many sides will the dice have? (8-32, uniform or irregular) ")
         killswitch += 1

 else:
     print "Invalid choice, please try again."
     sider = raw_input("How many sides will the dice have? (8-32, uniform or irregular) ")
     killswitch += 1

while valid == False and killswitch >= 2:
    print "As you cannot follow instructions, we will choose for you."
    choice2 = randint (1,3)

    if choice2 <= 2:
         sides = randint (8,32)
         print "We have choses dice with {} sides for you to play.".format(sides)
         valid = True
    else:
        while s < dice:
            neo = randint (8,32)
            dicesides.extend([neo])
            s += 1
        print "You have been given a variety of dice."
        print dicesides
        valid = True
        irregular = True

q = 0
p = 0
actual = 0
guess = 0

while irregular is False and q < dice:
    ultra = randint (1,sides)
    actual = int(actual + ultra)
    q += 1

while irregular is True and q < dice:
    ultra = randint (1,dicesides[q])
    actual = int(actual + ultra)
    q += 1

while irregular is True and p < dice:
    bork = dicesides[p]/2
    guess = int(guess + bork)
    p += 1

s = 0
r = randint(1,2)
x = 0
y = 0
z = 0

if irregular is False and r == 1:
    print "By a flip of the (virtual) coin, the computer will go first."
    y = round(sides/2.0 * dice)
    print "The computer's guess is: {}".format(y)
    x = int(raw_input("What is yours? "))

elif irregular is False and r == 2:
    print "By a flip of the (virtual) coin, you will go first."
    x = int(raw_input("What is your best guess? "))
    z = round(sides/2.0 * dice)
    if x > z:
        y = x - 1
    elif x < z:
        y = x + 1
    else:
        z = y
    print "The computer's guess is: {}".format(y)

elif irregular is True and r == 1:
    print "By a flip of the (virtual) coin, the computer will go first."
    y = guess
    print "The computer's guess is: {}".format(y)
    x = int(raw_input("What is yours? "))

elif irregular is True and r == 2:
    print "By a flip of the (virtual) coin, you will go first."
    x = int(raw_input("What is your best guess? "))
    z = guess
    if x > z:
        y = x - 1
    elif x < z:
        y = x + 1
    else:
        z = y
    print "The computer's guess is: {}".format(y)
       
else:
    pass

print "The actual total is: {}".format(actual)

xq = abs(x-actual)
yq = abs(y-actual)

if xq > yq:
    print "Computer has won."

elif xq < yq:
    print "Player has won!"

else:
    print "A tie?"
