import random as rd

fortune = ["do not be afriad of competition","An exciting opportunity lies ahead of you","You love peace","Get your mind set…confidence will lead you on","You will always be surrounded by true friends","You should be able to undertake and complete anything","You are kind and friendly","Attitude is a little thing that makes a big difference","Eat chocolate to have a sweeter life","Life is what happens to you while you are busy making other plans.","A beautiful, smart, and loving person will be coming into your life","A funny coincidence will make your day","Failure is the path of lease persistence","Welcome change","Don’t confuse recklessness with confidence","Do not let ambitions overshadow small success","Don’t just spend time. Invest it","Feeding a cow with roses does not get extra appreciation","Fearless courage is the foundation of victory.","Good to begin well, better to end well","Happiness will bring you good luck","Living with a commitment to excellence shall take you far","Miles are covered one step at a time","Now is a good time to buy stock","what are your thinking of doing tn, dont do it","gary and topher are the goats ","henry hogard and liam tesmer are coding geniuses ","mhm no fortune for you"]



def run():
    go = input("Welcome to fortune cookie! would you like a fortune?")
    if go == "yes":
        cpu = rd.choice(fortune)
        print(cpu)
    else:
        run()
    run()

run()