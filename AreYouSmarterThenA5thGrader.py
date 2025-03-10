global score 
score = 0
def go():
    start = input("hi welcome to are you smarter then a 5th grader quiz!are you ready?")
    if start == "yes":
        run()
    else:
        go()




def run():
    global score 
    guess = input("Density describes the mass of an object divided by what?")
    if guess == "volume":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("true or false: Crawfish are fish")
    if guess == "false":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("Costa Rica borders two countries. Nicaragua is one of the countries. What is the other")
    if guess == "panama":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("What is the capital of Russia?")
    if guess == "moscow":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("What is the process of water turning into vapor called?")
    if guess == "evaporation":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("What is the capital of France?")
    if guess == "paris":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("On the periodic table, which element is represented by the letter N?")
    if guess == "nitrogen":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("What gas do humans need in order to live")
    if guess == "oxygen":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("What is the hardest mineral")
    if guess == "diamond":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("Who invented the lightbulb")
    if guess == "thomas edison":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("How many inches are in a foot")
    if guess == "12":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("How many adjectives are in this sentence: Billy made a rude noise in class")
    if guess == "1":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("What is the plural form of the word deer")
    if guess == "deer":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("Maine borders which U.S. state")
    if guess == "new hampshire":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("What country has the longest border with the United States")
    if guess == "canada":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    guess = input("What is the capital of New York")
    if guess == "albany":
        score = score + 1000
        print("congrats thats right! your score is now",score)
    else:
        "wowww thats wrong"
    print("you finished with a score of",score)
        





go()
