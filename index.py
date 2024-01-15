import random
import time
p1points = 0
p2points = 0
p1c = input("Player 1, select your player: ")
p2c = input("Player 2, select your player: ")

while p1points < 20 and p2points < 20:
  if p1points >= 20:
    print(p1c + " won!")
  if p2points >= 20:
    print(p2c + " won!")
  print("What would you like to do")
  print("1. Dunk in his face")
  print("2. Shoot a three")
  print("3. Drive to the basket")
  p1move = input("+")
  if p1move == "1":
    joe = random.randint(1, 10)
    if joe > 4:
      zach = random.randint(1, 10)
      if zach >= 8:
        print("Through the legs dunk")
      if zach == 7:
        print("Double windmill")
      if zach == 6:
        print("Posterized")
      if zach == 5:
        print("360 backwards dunk")
      if zach <= 4:
        print("Jammed in")
      p1points += 2
      print("Score is: " + str(p1points) + " to " + str(p2points) + "")
    if joe <= 4:
      print("YOU GOT STUFFED.")
      print("Score is: " + str(p1points) + " to " + str(p2points) + "")
  if p1move == "2":
    joe = random.randint(1, 10)
    if joe >= 6:
      zach = random.randint(1, 10)
      if zach >= 8:
        print("In his eyes")
      if zach == 7:
        print("From the logo")
      if zach == 6:
        print("From deep")
      if zach == 5:
        print("He looks like Kobe")
      if zach == 4:
        print("Uncle Drew")
      if zach <= 3:
        print("Drained it again")
      p1points += 3
      print("Score is: " + str(p1points) + " to " + str(p2points) + "")
    if joe < 6:
      print("Airball.")
      print("Score is: " + str(p1points) + " to " + str(p2points) + "")
  if p1move == "3":
    joe = random.randint(1, 10)
    if joe > 5:
      zach = random.randint(1, 10)
      if zach >= 8:
        print("AND ONE")
        p1points += 3
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
      if zach == 7:
        print("Smooth drive to the basket")
        p1points += 2
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
      if zach == 6:
        print("Hang time")
        p1points += 2
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
      if zach == 5:
        print("What a move!")
        p1points += 2
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
      if zach == 4:
        print("MVP, MVP, MVP")
        p1points += 2
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
      if zach <= 3:
        print("Finished with his left hand.")
        p1points += 2
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
    if joe <= 5:
      print("Blocked from behind!")
      print("Score is: " + str(p1points) + " to " + str(p2points) + "")
      
  p2move = input("+")
  if p2move == "1":
    joe = random.randint(1, 10)
    if joe > 4:
      zach = random.randint(1, 10)
      if zach >= 8:
        print("Through the legs dunk")
      if zach == 7:
        print("Double windmill")
      if zach == 6:
        print("Posterized")
      if zach == 5:
        print("360 backwards dunk")
      if zach <= 4:
        print("Jammed in")
      p2points += 2
      print("Score is: " + str(p1points) + " to " + str(p2points) + "")
    if joe <= 4:
      print("YOU GOT STUFFED.")
      print("Score is: " + str(p1points) + " to " + str(p2points) + "")
  if p2move == "2":
    joe = random.randint(1, 10)
    if joe >= 6:
      zach = random.randint(1, 10)
      if zach >= 8:
        print("In his eyes")
      if zach == 7:
        print("From the logo")
      if zach == 6:
        print("From deep")
      if zach == 5:
        print("He looks like Kobe")
      if zach == 4:
        print("Uncle Drew")
      if zach <= 3:
        print("Drained it again")
      p2points += 3
      print("Score is: " + str(p1points) + " to " + str(p2points) + "")
    if joe < 6:
      print("Airball.")
      print("Score is: " + str(p1points) + " to " + str(p2points) + "")
  if p2move == "3":
    joe = random.randint(1, 10)
    if joe > 5:
      zach = random.randint(1, 10)
      if zach >= 8:
        print("AND ONE")
        p2points += 3
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
      if zach == 7:
        print("Smooth drive to the basket")
        p2points += 2
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
      if zach == 6:
        print("Hang time")
        p2points += 2
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
      if zach == 5:
        print("What a move!")
        p2points += 2
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
      if zach == 4:
        print("MVP, MVP, MVP")
        p2points += 2
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
      if zach <= 3:
        print("Finished with his left hand.")
        p2points += 2
        print("Score is: " + str(p1points) + " to " + str(p2points) + "")
    if joe <= 5:
      print("Blocked from behind!")
      print("Score is: " + str(p1points) + " to " + str(p2points) + "")
    
    
  