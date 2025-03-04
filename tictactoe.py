import random as rd 
global tl,tm,tr,ml,mm,mr,bl,bm,br
tl = "_"
tm = "_"
tr = "_"
ml = "_"
mm = "_"
mr = "_"
bl = "_"
bm = "_"
br = "_"
turns = 0
def run():
    global tl,tm,tr,ml,mm,mr,bl,bm,br,p
    p = rd.randint(1,4)
    if p == 1:
        tl = "X"
        check()
    elif p ==2:
        tr = "X"
        check()
    elif p == 3:
        bl = "X"
        check()
    else:
        br = "X"
        check()
    




def board():
    print(tl,tm,tr)
    print(ml,mm,mr)
    print(bl,bm,br)
    turn()


def turn():
    global tl,tm,tr,ml,mm,mr,bl,bm,br,go,turns
    go = input("where do you want to go")
    if go == "tl" and tl == "_":
        tl = "O"
        
    elif go == "tm" and tm == "_":
        tm = "O"
        
    elif go == "tr" and tr == "_":
        tr = "O"
        
    elif go == "ml" and ml == "_":
        ml = "O"
        
    elif go == "mm" and mm == "_":
        mm = "O"
        
    elif go == "mr" and mr == "_":
        mr = "O"
        
    elif go == "bl" and bl == "_":
        bl = "O"
        
    elif go == "bm" and bm == "_":
        bm = "O"
        
    elif go == "br" and br == "_":
        br = "O"

    else:
        print("cant go there!")
        turn()
    
    checkO()
 

    if turns == 0:
        turns = turns +1
        opposite()
    elif turns == 1:
        turns = turns +1
        cross()
    elif turns == 2:
        end()
        
    
def cross():
    global tl,tm,tr,ml,mm,mr,bl,bm,br,p
    p = rd.randint(1,4)
    if p == 1 and tl =="_":
        tl = "X"
        check()
    elif p ==2 and tr == "_":
        tr = "X"
        check()
    elif p == 3 and bl =="_":
        bl = "X"
        check()
    elif p ==4 and br == "_":
        br = "X"
        check()
    else:
        cross()
    
      

def opposite():
    global tl,tm,tr,ml,mm,mr,bl,bm,br
    if mm == "_":
        mm = "X"
    elif p == 1 and br == "_":
        br = "X"
    elif p == 2 and bl == "_":
        bl = "X"
    elif p == 3 and tr == "_":
        tr = "X"
    elif p == 4 and tl == "_":
        tl ="X"
    else:
        opposite()
        
    check()


def end():
    global tl,tm,tr,ml,mm,mr,bl,bm,br
    last = rd.randint(1,9)
    if last == 1 and tl == "_":
        tl = "X"
        check()
    elif last == 2 and tm == "_":
        tm = "X"
        check()
    elif last == 3 and tr == "_":
        tr = "X"
        check()
    elif last == 4 and ml == "_":
        ml = "X"
        check()
    elif last == 5 and mm == "_":
        mm = "X"
        check()
    elif last == 6 and mr == "_":
        mr = "X"
        check()
    elif last == 7 and bl == "_":
        bl = "X"
        check()
    elif last == 8 and bm == "_":
        bm = "X"
        check()
    elif last == 9 and br == "_":
        br = "X"
        check()
    else:
        end()


def check():
    if tl == "X" and tm == "X" and tr == "X":
        lose()
    elif ml == "X" and mm == "X" and mr == "X":
        lose()
    elif bl == "X" and bm == "X" and br == "X":
        lose()
    elif tl == "X" and mm == "X" and br == "X":
        lose()
    elif tr == "X" and mm == "X" and bl == "X":
        lose()
    elif tl == "X" and ml == "X" and bl == "X":
        lose()
    elif tm == "X" and mm == "X" and bm == "X":
        lose()
    elif tr == "X" and mr == "X" and br == "X":
        lose()
    elif tl == "O" and tm == "O" and tr == "O":
        win()
    elif ml == "O" and mm == "O" and mr == "O":
        win()
    elif bl == "O" and bm == "O" and br == "O":
        win()
    elif tl == "O" and mm == "O" and br == "O":
        win()
    elif tr == "O" and mm == "O" and bl == "O":
        win()
    elif tl == "O" and ml == "O" and bl == "O":
        win()
    elif tm == "O" and mm == "O" and bm == "O":
        win()
    elif tr == "O" and mr == "O" and br == "O":
        win()
    elif tl != "_" and tm != "_" and tr != "_" and ml != "_" and mm != "_" and mr != "_" and bl != "_" and bm != "_" and tr != "_":
        tie()
    else:
        board()
    
def checkO():
    global tl,tm,tr,ml,mm,mr,bl,bm,br,go,turns
    if tl == "X" and tm == "X" and tr == "X":
        lose()
    elif ml == "X" and mm == "X" and mr == "X":
        lose()
    elif bl == "X" and bm == "X" and br == "X":
        lose()
    elif tl == "X" and mm == "X" and br == "X":
        lose()
    elif tr == "X" and mm == "X" and bl == "X":
        lose()
    elif tl == "X" and ml == "X" and bl == "X":
        lose()
    elif tm == "X" and mm == "X" and bm == "X":
        lose()
    elif tr == "X" and mr == "X" and br == "X":
        lose()
    elif tl == "O" and tm == "O" and tr == "O":
        win()
    elif ml == "O" and mm == "O" and mr == "O":
        win()
    elif bl == "O" and bm == "O" and br == "O":
        win()
    elif tl == "O" and mm == "O" and br == "O":
        win()
    elif tr == "O" and mm == "O" and bl == "O":
        win()
    elif tl == "O" and ml == "O" and bl == "O":
        win()
    elif tm == "O" and mm == "O" and bm == "O":
        win()
    elif tr == "O" and mr == "O" and br == "O":
        win()

    if turns == 0:
        turns = turns +1
        opposite()
    elif turns == 1:
        turns = turns +1
        cross()
    elif turns == 2:
        end()
    




def win():
    global turns
    print(tl,tm,tr)
    print(ml,mm,mr)
    print(bl,bm,br)
    print("congrats you won")
    turns =3

def lose():
    global turns
    print(tl,tm,tr)
    print(ml,mm,mr)
    print(bl,bm,br)
    print("you lost...")
    turns = 3
def tie():
    global turns
    print(tl,tm,tr)
    print(ml,mm,mr)
    print(bl,bm,br)
    print("you tied ugh!")
    turns = 3

#start
print(tl,tm,tr)
print(ml,mm,mr)
print(bl,bm,br)
print("welcome to tictac toe! ready to start?")
run()
