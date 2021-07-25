import simOnegame
import getInputs
def simNgames():
    finallA, finallB = 0, 0
    for onegame in range(getInputs.getgamenums()):
        proA, proB = getInputs.unirange()  # 改成选手的能力值在一定范围内随机
        scoreA,scoreB=simOnegame.simOnegame(proA,proB)
        if scoreA>scoreB:
            finallA+=1
        else:
            finallB+=1
    return finallA,finallB       