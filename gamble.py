import random as rd
global money
money = 20 


#bulk code of input
def run():
    global money
    pick = input("would you like to gamble to 1/3,1/2 or 2/1 ")
    if pick == "1/2":
        gam = int(input("how much would you like to gamble"))
        
        if gam > money:
            print("cant gamble that much!")
            run()
        else:
            money = money - gam
            cpu = rd.randint(1,3)
            if cpu == 1 or cpu == 3:
                money = (gam *1.5)+money
                print("congrate you won! you now have")
            else:
                print("you lost! you now have")
    elif pick == "1/3":
        gam = int(input("how much would you like to gamble"))
        
        if gam > money:
            print("cant gamble that much!")
            run()
        else:
            cpu = rd.randint(1,4)
            if cpu == 2 :
                print("you lost! you now have")
                money = money - gam
            else:
                money = (gam *1.3)+money
                print("you won! you now have")
    elif pick == "2/1":
        gam = int(input("how much would you like to gamble"))
        if gam > money:
            print("cant gamble that much!")
            run()
        else:
            money = money - gam
            cpu = rd.randint(1,4)
            if cpu == 1 or cpu == 2:
                print("congrats you won! you now have")
                money = (gam *2)+money
            else:
                print("you lost! you now have")
    elif pick == "lukey":
        money = 99999999 
    else:
        print("not valid try again")
        run()
    money = round(money,0)
    check()

def check():
    if money > 0:
        print(money)
        run()
    else:
        print("0")
        print("you have lost all your money! better luck next time")



#start text

print("hello! welcome to gambling! you start with 20$ can you profit your way to 1000?")
run()
