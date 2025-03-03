import random
list = ["rock","paper","scissors"]




#generator 
def run():
    if choice == "rock" or choice == "paper" or choice == "scissors":
        cpu = random.choice(list)
        if choice == cpu:
            print("tie! you both chose",cpu)
        else:
            if choice == "rock" and cpu == "paper":
                print("you chose rock... cpu chose paper you lose!")
            elif choice =="rock" and cpu == "scissors":
                print("you chose rock... cpu chose scissors you win!")
            elif choice == "paper" and cpu == "rock":
                print("you chose paper.... cpu chose rock you win!")
            elif choice == "paper" and cpu =="scissors":
                print("you chose paper... cpu chose scissors you lose!")
            elif choice == "scissors" and cpu =="paper":
                print("you chose scissors... cpu chose paper you win!")
            else:
                print("you chose scissors... cpu chose rock you lose!")
                
    else:
        print("Invalid answer try agai!")

#starting texts
print("hello! are you ready to play rock paper scissors?")
choice = input("choose rock, paper or scissors")
run()




