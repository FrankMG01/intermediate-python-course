import random
def main():
  dice_rolls = 2
  dicesum = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1,6)
    dicesum += roll
    print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dicesum}')

if __name__== "__main__":
  main()