import random
randNo= random.randint(1,100)
print("WELCOME TO THE GUESSING NUMBER ZONE")
print("The Game Begins: All the Best")
print("The Computer has chosen a number")
num= None
guesses=0
while(randNo!= num):
    num=int(input("Enter a number: "))
    guesses= guesses+1
    if (num==randNo):
        print("Bravo! You guessed the perfect number")
    else:
        if (num>randNo):
            print("Wrong choice! Enter a smaller number: ")
        else:
            print("Wrong Choice! Enter a larger number: ")

print(f'You guessed the number in {guesses} guesses')
with open("hiscore.txt","r") as f:
    hiscore= int(f.read())
if(guesses<hiscore):
    print("Wow! you just broke the highscore! ")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))
