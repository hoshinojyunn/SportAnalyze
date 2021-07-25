from simNgames import *
def printSummary(finalA,finalB):
    finalnum=finalA+finalB
    print('共模拟了{}场比赛'.format(finalnum))
    print('A运动员获胜{}场,胜率{:0.1%}'.format(finalA,finalA/finalnum))
    print('B运动员获胜{}场,胜率{:0.1%}'.format(finalB,finalB/finalnum))