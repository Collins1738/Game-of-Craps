import random


def roll_dice():
  x=random.randint(1, 6)
  y=random.randint(1, 6)
  return [x, y]

def get_bet(string):
  if string == "A":
    return "Pass Line Bet"
  elif string == "B":
    return "Any Craps"
  elif string =="C":
    return "Any Seven"
  elif string=="D":
    return "Any Eleven"
  elif string =="E":
    return "Ace Duece"
  elif string =="F":
    return "Aces or Boxcars"


class Craps():
  def __init__(self, player_number):
    self.point=False
    self.player_number=player_number
    self.winnings=[]
    self.money=1000
    self.dict_bets={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0}
    return 
  
  def check_bets(self):
    return

  def bets_edit(self, bet, answer, price=0):     
    if answer==False:
      self.dict_bets[bet]=0
      # print("Player "+str(self.player_number)+" bets are \n", self.dict_bets)
      return

    elif answer==True:
      if bet =="A":
        self.money+=(self.dict_bets[bet]+(self.dict_bets[bet]*1))
        self.winnings.append(self.dict_bets[bet]*1)
        self.dict_bets[bet]=0

      if bet=="B":
        self.money+=(self.dict_bets[bet]+(self.dict_bets[bet]*8))
        self.winnings.append(self.dict_bets[bet]*8)
        self.dict_bets[bet]=0

      if bet =="C":
        self.money+=(self.dict_bets[bet]+(self.dict_bets[bet]*5))
        self.winnings.append(self.dict_bets[bet]*5)
        self.dict_bets[bet]=0

      if bet=="D":
        self.money+=(self.dict_bets[bet]+(self.dict_bets[bet]*16))
        self.winnings.append(self.dict_bets[bet]*16)
        self.dict_bets[bet]=0

      if bet =="E":
        self.money+=(self.dict_bets[bet]+(self.dict_bets[bet]*16))
        self.winnings.append(self.dict_bets[bet]*16)
        self.dict_bets[bet]=0

      if bet=="F":
        self.money+=(self.dict_bets[bet]+(self.dict_bets[bet]*30))
        self.winnings.append(self.dict_bets[bet]*30)
        self.dict_bets[bet]=0


  def natural_bets_edit(self, bet, answer, price=0):     
    if answer==False:
      self.dict_bets[bet]=0
      print("Player "+str(self.player_number)+" bets are \n", self.dict_bets)
      return

    elif answer==True:
      if bet =="A":
        self.dict_bets[bet]=self.dict_bets[bet]+(self.dict_bets[bet]*1)

      # if bet=="B":
      #   self.money+=(self.dict_bets[bet]+(self.dict_bets[bet]*8))
      #   self.winnings.append(self.dict_bets[bet]*8)
      #   self.dict_bets[bet]=0

      # if bet =="C":
      #   self.money+=(self.dict_bets[bet]+(self.dict_bets[bet]*5))
      #   self.winnings.append(self.dict_bets[bet]*5)
      #   self.dict_bets[bet]=0

      # if bet=="D":
      #   self.money+=(self.dict_bets[bet]+(self.dict_bets[bet]*16))
      #   self.winnings.append(self.dict_bets[bet]*16)
      #   self.dict_bets[bet]=0

      # if bet =="E":
      #   self.money+=(self.dict_bets[bet]+(self.dict_bets[bet]*16))
      #   self.winnings.append(self.dict_bets[bet]*16)
      #   self.dict_bets[bet]=0

      # if bet=="F":
      #   self.money+=(self.dict_bets[bet]+(self.dict_bets[bet]*30))
      #   self.winnings.append(self.dict_bets[bet]*30)
      #   self.dict_bets[bet]=0


# Main Program Begins
print("Welcome to The Game Of Craps!!")
print("----------------------")
print("There are 4 players on the table. Each player starts off with $1000 each. You are Player 1 and you would be the first shooter")
print("----------------------")
p1=Craps(1)
p2=Craps(2)
p3=Craps(3)
p4=Craps(4)

round_num=1
while p1.money>0 and round_num<5:
  print ("Round "+ str(round_num)+"!!!")
  print("You have $"+str(p1.money))
  print("You may place your bets!!! \n")
  print("Bets: \n[A] Pass Line Bets (Evens) \n[B] Any Craps \n[C] Any Seven \n[D] Any Eleven \n[E] Ace Duece \n[F] Aces or Boxcars")
  bets=input("Type either A, B, C, D, E or F; if you want to make more than one bet, type in the letters seperated by commas e.g. 'A, C, F'\n")
  
  #This mechanism puts the different bets in a list when from an array seperated with commas or commas and spaces
  array_bets=bets.split(" ")
  array_bets="".join(array_bets)
  array_bets=array_bets.split(",")
  

  for i in array_bets:
    price=int(input("How much do you wish to bet for "+str(get_bet(i))+" "))
    p1.money-=price
    if p1.money<0:
      print("Sorry, You do not have enough money for that bet \nBet will not be placed")
      p1.money+=price
      continue
    p1.dict_bets[i]+=price
  print("Player 1 bets", p1.dict_bets)
  print("----------------------")


  # Here the players 2, 3, and 4 pick their bets which are random and computer picked
  i=random.choice(["A", "B", "C", "D", "E", "F"])
  price=random.randint(0, p2.money)
  p2.dict_bets[i]+=price
  p2.money-=price
  i=random.choice(["A", "B", "C", "D", "E", "F"])
  price=random.randint(0, p2.money)
  p2.dict_bets[i]+=price
  p2.money-=price
  print("Player 2 bets", p2.dict_bets)
  print("----------------------")

  i=random.choice(["A", "B", "C", "D", "E", "F"])
  price=random.randint(0, p3.money)
  p3.dict_bets[i]+=price
  p3.money-=price
  i=random.choice(["A", "B", "C", "D", "E", "F"])
  price=random.randint(0, p3.money)
  p3.dict_bets[i]+=price
  p3.money-=price
  print("Player 3 bets", p3.dict_bets)
  print("----------------------")

  i=random.choice(["A", "B", "C", "D", "E", "F"])
  price=random.randint(0, p4.money)
  p4.dict_bets[i]+=price
  p4.money-=price
  i=random.choice(["A", "B", "C", "D", "E", "F"])
  price=random.randint(0, p4.money)
  p4.dict_bets[i]+=price
  p4.money-=price
  print("Player 4 bets", p4.dict_bets)
  print("----------------------")

  
  while True:
  # SHOOTING TIME
    input(print("\n\n\nShooting time!! (Press Enter to shoot)"))
    array_dice=roll_dice()
    x=array_dice[0]
    y=array_dice[1]
    print("Shooter shoots \n"+str(x)+"\n"+str(y))
    total_roll=x+y
    # total_roll=11
    print("Total roll is "+str(total_roll))
    

    #Prepositional Bets
    print("Prepositional Bets: \n")
    #Any craps
    if total_roll in [2, 3, 12]:
      print("All "+str(get_bet("B"))+" WINS!!")
      p1.bets_edit("B", True)
      p2.bets_edit("B", True)
      p3.bets_edit("B", True)
      p4.bets_edit("B", True)
    else:
      print("All "+str(get_bet("B"))+" loses")
      p1.bets_edit("B", False)
      p2.bets_edit("B", False)
      p3.bets_edit("B", False)
      p4.bets_edit("B", False)

    #Any Seven
    if total_roll in [7]:
      print("All "+str(get_bet("C"))+" WINS!!")
      p1.bets_edit("C", True)
      p2.bets_edit("C", True)
      p3.bets_edit("C", True)
      p4.bets_edit("C", True)
    else:
      print("All "+str(get_bet("C"))+" loses")
      p1.bets_edit("C", False)
      p2.bets_edit("C", False)
      p3.bets_edit("C", False)
      p4.bets_edit("C", False)

    #Eleven
    if total_roll in [11]:
      print("All "+str(get_bet("D"))+" WINS!!")
      p1.bets_edit("D", True)
      p2.bets_edit("D", True)
      p3.bets_edit("D", True)
      p4.bets_edit("D", True)
    else:
      print("All "+str(get_bet("D"))+" loses")
      p1.bets_edit("D", False)
      p2.bets_edit("D", False)
      p3.bets_edit("D", False)
      p4.bets_edit("D", False)

    # Ace Duece
    if total_roll in [3]:
      print("All "+str(get_bet("E"))+" WINS!!")
      p1.bets_edit("E", True)
      p2.bets_edit("E", True)
      p3.bets_edit("E", True)
      p4.bets_edit("E", True)
    else:
      print("All "+str(get_bet("E"))+" loses")
      p1.bets_edit("E", False)
      p2.bets_edit("E", False)
      p3.bets_edit("E", False)
      p4.bets_edit("E", False)

    # Aces or Boxcars
    if total_roll in [2, 12]:
      print("All "+str(get_bet("F"))+" WINS!!")
      p1.bets_edit("F", True)
      p2.bets_edit("F", True)
      p3.bets_edit("F", True)
      p4.bets_edit("F", True)
    else:
      print("All "+str(get_bet("F"))+" loses")
      p1.bets_edit("F", False)
      p2.bets_edit("F", False)
      p3.bets_edit("F", False)
      p4.bets_edit("F", False)


    # PASS LINE BETS
    print("Passline Bets: /n")
    if total_roll in [2, 3, 12]:
      print("All "+str(get_bet("A"))+" loses")
      p1.bets_edit("A", False)
      p2.bets_edit("A", False)
      p3.bets_edit("A", False)
      p4.bets_edit("A", False)
      print("\nRound "+str(round_num)+" ends\n\n\n\n\n")
      round_num+=1
      break
    
    if total_roll in [7, 11]:
      print("All "+str(get_bet("A"))+" WINS!!")
      p1.natural_bets_edit("A", True)
      p2.natural_bets_edit("A", True)
      p3.natural_bets_edit("A", True)
      p4.natural_bets_edit("A", True)
      continue

    if total_roll in [4, 5, 6, 8, 9, 10]:
      point=total_roll
      print("Point is "+str(point))
      while True:
        input(print("\nShooting time!! (Press Enter to shoot)"))
        array_dice=roll_dice()
        x=array_dice[0]
        y=array_dice[1]
        print("Shooter shoots \n"+str(x)+"\n"+str(y))
        total_roll=x+y
        # total_roll=5
        print("Total roll is "+str(total_roll))

        if total_roll==point:
          print("Total roll equal to point \nAll Passline bets WIN!!")
          p1.bets_edit("A", True)
          p2.bets_edit("A", True)
          p3.bets_edit("A", True)
          p4.bets_edit("A", True)
          break

        elif total_roll==7:
          print("Seven Out \nAll Passline bets lose")
          p1.bets_edit("A", False)
          p2.bets_edit("A", False)
          p3.bets_edit("A", False)
          p4.bets_edit("A", False)
          break

        else:
          print("Shoot again")
          continue
      
      round_num+=1
      break
  continue

print("Your winnings are ", p1.winnings)
print("All players winnings:\n", [p1.winnings, p2.winnings, p3.winnings, p4.winnings])

if p1.money<=0:
  input(print("You ran out of money :(.. \nGoodbye"))
if round_num==5:
  input(print("After "+str(round_num-1)+" rounds, we are done for today. Goodbye!!"))
