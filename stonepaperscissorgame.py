import random

print("Welcome to Game Stone Paper Scissor.\nIn this game, You have three options and you are playing against "
      "computer. \n You have to choose from three options 1.Stone 2.Paper 3. Scissor \nStone wins over scissor, "
      "Scissor wins over paper and paper wins over stone. \nYou will have ten chances. \nLet's go and Enjoy the "
      "game.")
count = 0
win = 0
loose = 0
tie = 0
i = "stone"
p = "paper"
s = "scissor"
list1 = [i, p, s]
while count < 10:
    choice = random.choice(list1)
    n = input().lower()
    count = count+1
    print("Tries left:", 10-count)
    if choice == i:
        if n == i:
            print("Machine Choice:", choice)
            print("Match Tie")
            tie = tie+1
        elif n == p:
            print("Machine Choice:", choice)
            print("Hurray! You won")
            win = win+1
        elif n == s:
            print("Machine Choice:", choice)
            print("Alas! You Lost against a machine.")
            loose = loose+1
    elif choice == p:
        if n == p:
            print("Machine Choice:", choice)
            print("Match Tie")
            tie = tie + 1
        elif n == s:
            print("Machine Choice:", choice)
            print("Hurray! You won")
            win = win + 1
        elif n == i:
            print("Machine Choice:", choice)
            print("Alas! You Lost against a machine.")
            loose = loose + 1
    elif choice == s:
        if n == i:
            print("Machine Choice:", choice)
            print("Hurray! You won")
            win = win + 1
        elif n == p:
            print("Machine Choice:", choice)
            print("Alas! You Lost against a machine.")
            loose = loose + 1
        elif n == s:
            print("Machine Choice:", choice)
            print("Match Tie")
            tie = tie + 1
    else:
        print("Error")
    continue
print("Your Score:", win)
print("Machine Score:", loose)
print("Matches Tied:", tie)
print("Hope You enjoyed.")
