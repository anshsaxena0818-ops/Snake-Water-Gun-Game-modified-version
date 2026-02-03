import random
"""
1 for Snake
-1 for Water
0 for Gun
 """

Computer_score = 0
Your_score = 0

for i in range (5):
    computer = random.choice([-1, 0, 1])
    youstr = input("Enter your choice:")
    youDict = {"s": 1, "w": -1, "g":0}
    reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
    if youstr not in youDict:
        print("Invalid Choice")

    you = youDict[youstr]
    
    if(computer == you):
        print("Its a draw")
        
    else:
        if((computer - you) == -1 or (computer - you) == 2):
            print("You Lose!")
            Computer_score += 1
        
        else:
            print("You Win!")
            Your_score += 1

    def final_winner():
        if (Computer_score == Your_score):
            print("There is no final winner")
            
        else:
            if(Computer_score > Your_score):
                print("The final winner is the Computer:",Computer_score)
                
            else:
                print("The final winner is you:",Your_score)

    print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}\n")

final_winner()

with open ("Scores.txt", "w") as f:
    f.write("Snake Water Gun Game final Scores\n")
    f.write("-----------------------------------------\n")
    f.write(f"Computer Scores are:{Computer_score}\n")
    f.write(f"Your Scores are:{Your_score}\n")

    if (Computer_score == Your_score):
        f.write("Match is draw")

    elif(Computer_score > Your_score):
        f.write("Computer wins")

    else:
        f.write("You win")

    

