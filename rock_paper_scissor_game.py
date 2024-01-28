import random
cChoice={1:"⛰️",2:"📃",3:"✂️"}
i=1
yourPoints,computerPoints=0,0
tCnt=0
while True:
    if i==1:
        print("Rock Paper Scissor Game:-")
    print()
    if i>1:
        print("If you want to continue the Game, Press 1")
        print("Else press 0")
        game=int(input())
        if game==1:
            pass
        elif game==0:
            if yourPoints>computerPoints:
                print("👏 You wins this Game")
            elif yourPoints<computerPoints:
                print("😔 You lose this Game")
            else:
                print("Game drawn")
            print("Totol number of Your points:",yourPoints)
            print("Totol number of Computer points:",computerPoints)
            print("Total number of Ties:",tCnt)
            print()
            print("Thanks! for playing...")
            break
        else:
            print("Invalid key")
    print("Round",i,"start:")
    print()
    print("Please select any one option-")
    print(str(1)+" for ⛰️",str(2)+" for 📃",str(3)+" for ✂️",sep="\n")
    print()

    yourChoice=int(input())
    if yourChoice==1:
        print("You selected: ⛰️")
    elif yourChoice==2:
        print("You selected: 📃")
    elif yourChoice==3:
        print("You selected: ✂️")
    else:
        print("Invalid selection")
        continue
    c=["⛰️","📃","✂️"]
    computerChoice=random.choice(c)
    
    if computerChoice==cChoice[yourChoice]:
        tCnt+=1
        print("Computer selected:",computerChoice)
        print("Tie")
        print("Computer points:",computerPoints)
        print("Your points:",yourPoints)

    elif (yourChoice==1 and computerChoice==cChoice[3]) or (yourChoice==2 and computerChoice==cChoice[1]) or (yourChoice==3 and computerChoice==cChoice[2]):
        yourPoints+=1
        print("Computer selectd:",computerChoice)
        print("You wins this round")
        print("Computer points:",computerPoints)
        print("Your points:",yourPoints)
    else:
        computerPoints+=1
        print("Computer selected:",computerChoice)
        print("You lose this round")
        print("Computer points:",computerPoints)
        print("Your points:",yourPoints)
    print()
    i+=1