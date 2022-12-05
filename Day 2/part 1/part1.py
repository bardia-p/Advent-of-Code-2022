'''
A is rock
B is paper 
C is scissors

X is rock
Y is paper 
Z is scissor

1 for rock 
2 for paper
3 for scissors

0 for losing
3 for draw
6 for win
'''

f = open("Day 2\input.txt", "r")

lines = f.readlines()

moves = {"A":1, "B":2, "C":3, "X":1, "Y":2, "Z":3}

points = 0 

for line in lines:
    currMove = line.strip().split()

    otherHand = moves[currMove[0]]
    yourHand = moves[currMove[1]]

    if (otherHand > yourHand and (otherHand - yourHand == 1)) or (otherHand == 1 and yourHand == 3):
        result = 0
    elif otherHand == yourHand:
        result = 3
    else:
        result = 6

    points += yourHand + result

print(points)

f.close()