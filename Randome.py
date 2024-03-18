import random

print(random.randint(1000,9999))
l=[1,2,3,1.1,10,"tops",True,"python",101]
print(random.choice(l))



num=random.randint(1,20)

while True:
    guess=int(input("Guess A Number Between 1 to 20 :"))
    if guess==num:
        print(" You Guessed A Correct Number")
        break
    elif guess>num:
        print(" you Guessed A Grater Number")
    elif guess<num:
        print("You Guessed A smaller Number")
