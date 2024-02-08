import random
from time import *
import os

os.system("cls")

test=["My name is Pradip Kumar Madheshiya.",
      "I am an Aspiring Full Stack Web Developer.",
      "This Project will help us to measure Typing Speed."]

while True:

    print()
    print("***** Typing Test *****")
    print()

    print("Choose time among 1, 2, 3, 4, 5 (minutes)")
    print("Your time choice: ",end="")
    try:
        userChoice=int(input())
    except:
        print("You have pressed the wrong key")
        continue
    print()

    paragraph=random.choice(test)
    paragraph=paragraph.split()

    for i in paragraph:
        print(i,end=" ")

    print()
    print()
    print("***** Start Typing *****")
    print()

    time1=time()
    type=list(input().split())
    time2=time()
    timeT=round(time2-time1)
    print()

    error=0
    cnt=1
    corWords=0
    for i in range(len(type)):
        if cnt>len(paragraph):
            break
        if paragraph[i]!=type[i]:
            error+=1
        else:
            corWords+=1
        cnt+=1
        if userChoice*60==timeT:
            break
 
    try:
        accuracy=round((corWords/len(paragraph))*100)
    except:
        accuracy=0

    print()
    print("Taken time: ",timeT,"seconds")
    print("Total words typed:",len(type),"words")
    print("Correct words typed:",corWords,"words")
    print("Errors:",error,"words")
    print("accuracy:",str(accuracy)+"%")
    mint=timeT/60
    wpm=round(len(type)/mint)
    print("Typing Speed:",wpm,"wpm")

    print()
    print("If you want to continue the test, press c else press q.")
    inp=input()
    if inp=="q" or inp=="Q":
        print()
        print("Thank You!")
        print()
        break
    elif inp=="c" or inp=="C":
        pass
    else:
        print("You have pressed the wrong key.")
        print()

    # ThankYou!