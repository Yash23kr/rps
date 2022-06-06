import random

user=input("Enter r for rock, p for paper, s for scissors.\n")
comp=random.choice(['r','p','s'])
if user==comp:
    print('Computer chose ',comp, ' so its a Tie')
elif (user=='r' and comp=='s') or(user=='p' and comp=='r') or (user=='s' and comp=='p'):
    print('Computer chose ',comp,' so You win')
else:
    print('Computer chose ',comp,' so Computer wins')
