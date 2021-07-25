import random
downA = eval(input('输入A的下限:'))#A下限
upA = eval(input('输入A的上限:'))#A上限
downB=eval(input('输入B的下限:'))#B下限
upB=eval(input('输入B的上限:'))#B上限
def getInputs():
    proA=eval(input('请输入A运动员的能力值:'))
    proB=eval(input('请输入B运动员的能力值:'))
    return proA,proB
def getgamenums():
    num=eval(input('请输入比赛场数:'))
    return num
def unirange():
    proA=random.uniform(downA,upA)
    proB=random.uniform(downB,upB)
    return proA,proB