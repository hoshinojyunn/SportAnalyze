import random
def simOnegame(proA,proB):
    serving='A'
    scoreA,scoreB=0,0
    while not gameover(scoreA,scoreB):
        if serving=='A':
            #if random.random()<proA:#算法有缺陷 比较的是A与随机的关系 而不是A与B的关系
            if proA>proB:
                scoreA+=1
            else:
                serving='B'
        else:
            #if random.random()<proB:
            if proA<proB:
                scoreB+=1
            else:
                serving='A'
    return scoreA,scoreB
def gameover(scoreA,scoreB):
    if scoreA==15:
        return True
    elif scoreB==15:
        return True
    else:
        return False