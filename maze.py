def name():
    nam = input("Enter name:")
    return nam
def score(lim):
    print("your final score is:",lim)
def win(a):
    if a == 12:
        print("You Won!!!")
    else:
        print("Sorry Try Again")
    score(a)
def mole():
    print("name:"+name())
    print("Finish the maze in minimum steps")
    print("Finish the Maze in 12 steps")
    print("Score: XX")
    print(" _____________________________")
    print("|  _____  |_____________|   __ Finish")
    print("| |     | |  _____   |   __|")
    print("| |     | | |     |  |  |")
    print("| |     | | |     |_____|")
    print("| |     |___|  ")
    print("Start")
def mode():
    st = 0
    step = 0
    z = 5
    pro = 5
    p = 5
    q = 5
    r = 5
    s = 5
    t = 5
    u = 5
    v = 5
    w = 5
    x = 5
    y = 5
    while pro!=0:
        step1 = int(input("enter correct number to move forward"))
        if step1==5:
            print(" _____________________________")
            print("|* _____  |_____________|   __ Finish")
            print("| |     | |  _____   |   __|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |_____|")
            print("| |     |___|  ")
            print("Start")
            pro = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(pro))
            pro = pro-1
        step+=1
    while p!=0:
        step2 = int(input("enter correct number to move right"))
        if step2==7:
            print(" _____________________________")
            print("|  _____ *|_____________|   __ Finish")
            print("| |     | |  _____   |   __|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |_____|")
            print("| |     |___|  ")
            print("Start")
            p = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(p))
            p = p-1
        step+=1
    while q!=0:
        step3 = int(input("enter correct number to move down"))
        if step3==4:
            print(" _____________________________")
            print("|  _____  |_____________|   __ Finish")
            print("| |     | |  _____   |   __|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |_____|")
            print("| |     |*__|  ")
            print("Start")
            q = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(q))
            q = q-1
        step+=1
    while r!=0:
        step4 = int(input("enter correct number to move right"))
        if step4==2:
            print(" _____________________________")
            print("|  _____  |_____________|   __ Finish")
            print("| |     | |  _____   |   __|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |_____|")
            print("| |     |__*|  ")
            print("Start")
            r = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(r))
            r = r-1
        step+=1
    while s!=0:
        step5 = int(input("enter correct number to move up"))
        if step5==3:
            print(" _____________________________")
            print("|  _____  |_____________|   __ Finish")
            print("| |     | |* _____   |   __|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |_____|")
            print("| |     |___|  ")
            print("Start")
            s = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(s))
            s = s-1
        step+=1
    while t!=0:
        step6 = int(input("enter correct number to move forward"))
        if step6==7:
            print(" _____________________________")
            print("|  _____  |_____________|   __ Finish")
            print("| |     | |  _____  *|   __|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |_____|")
            print("| |     |___|  ")
            print("Start")
            t = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(t))
            t = t-1
        step+=1
    while u!=0:
        step7 = int(input("enter correct number to move forward"))
        if step7==2:
            print(" _____________________________")
            print("|  _____  |_____________|   __ Finish")
            print("| |     | |  _____   |   __|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |*____|")
            print("| |     |___|  ")
            print("Start")
            u = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(u))
            u = u-1
        step+=1
    while v!=0:
        step8 = int(input("enter correct number to move right"))
        if step8==5:
            print(" _____________________________")
            print("|  _____  |_____________|   __ Finish")
            print("| |     | |  _____   |   __|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |____*|")
            print("| |     |___|  ")
            print("Start")
            v = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(v))
            v = v-1
        step+=1
    while w!=0:
        step9 = int(input("enter correct number to move forward"))
        if step9==2:
            print(" _____________________________")
            print("|  _____  |_____________|   __ Finish")
            print("| |     | |  _____   |*  __|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |_____|")
            print("| |     |___|  ")
            print("Start")
            w = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(w))
            w = w-1
        step+=1
    while x!=0:
        step10 = int(input("enter correct number to move forward"))
        if step10==3:
            print(" _____________________________")
            print("|  _____  |_____________|   __ Finish")
            print("| |     | |  _____   |   _*|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |_____|")
            print("| |     |___|  ")
            print("Start")
            x = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(x))
            x = x-1
        step+=1
    while y!=0:
        step11 = int(input("enter correct number to move forward"))
        if step11==1:
            print(" _____________________________")
            print("|  _____  |_____________|*  __ Finish")
            print("| |     | |  _____   |   __|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |_____|")
            print("| |     |___|  ")
            print("Start")
            y = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(y))
            y = y-1
        step+=1
    while z!=0:
        step12 = int(input("enter correct number to move forward"))
        if step12==3:
            print(" _____________________________")
            print("|  _____  |_____________|   __ *")
            print("| |     | |  _____   |   __|")
            print("| |     | | |     |  |  |")
            print("| |     | | |     |_____|")
            print("| |     |___|  ")
            print("Start")
            z = 0
        else:
            print("sorry that is not correct, you have %s chances left"%(z))
            z = z-1
        step+=1
    st = win(step)
if __name__=="__main__":
    mole()
    mode()
