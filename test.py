import math
import random


def main():
    def simOneGame(pa, pb):
        return (pa*random.uniform(0, 100), pb*random.uniform(0, 100))

    def simNGames(probA, probB):
        winsA = 0
        winsB = 0
        while (winsA < 15 and winsB < 15):
            scoreA, scoreB = simOneGame(probA, probB)
            if scoreA > scoreB:
                winsA = winsA + 1
            else:
                winsB = winsB + 1
        return (winsA, winsB)

    def aWin(pa, pb):
        a = 0
        b = 1
        n = 0
        while a < b:
            n += 1
            a, b = simNGames(pa, pb)
            print('a:b=', str(a)+":"+str(b))
        print('n场比赛:', n)
        return n
    aWin(0.4, 0.6)


main()
