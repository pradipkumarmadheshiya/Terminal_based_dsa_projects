import random
from time import *

test=[["My", "name", "is", "Pradip", "Kumar", "Madheshiya."],
      ["I","am","a","Aspiring","Full","Stack","Web","Developer."],
      ["This","Project","will","help","to", "measure","typing","speed."]]

while True:

    print()
    print("***** Typing Test *****")
    print()

    print("Choose time among 1, 2, 3, 4, 5 (minutes)")
    print("Your time choice: ",end="")
    userChoice=int(input())
    print()

    paragraph=random.choice(test)

    for i in range(len(paragraph)):
        print(paragraph[i],end=" ")

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
    for i in range(len(type)):
        if cnt>len(paragraph):
            break
        if paragraph[i]!=type[i]:
            error+=1
        cnt+=1
        if userChoice*60==timeT:
            break

    print()
    print("Error: ",error)
    print("taken time",timeT)
    temp=len(type)/timeT
    wpm=round(temp*60)
    print("Typing Speed:",wpm,"wpm")