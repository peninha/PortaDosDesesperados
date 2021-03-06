# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:32:01 2020

@author: Pena

Chance do Serginho Malandro saber a porta do prêmio, dado que
ele não estragou o quadro (não revelou o prêmio) "n" vezes seguidas
"""
import timeit


def ProbKnowGivenDontScrewUp(n):
    if n == 0:
        return 1/2
    else:
        return 1/(1/3 + 2/(3*ProbKnowGivenDontScrewUp(n-1)))


def SameFunctionButNotRecursive(n):
    P0 = 0
    for i in range(n+1):
        if i == 0:
            P1 = 1/2
        else:
            P1 = 1/(1/3 + 2/(3*P0))
        P0 = P1
    return P1


def CompareRunTimeOnBothFunctions(runs=10000):
    # Run time measure ----------------------------------
    code = """
def ProbKnowGivenDontScrewUp(n):
    if n == 0:
        return 1/2
    else:
        return 1/(1/3 + 2/(3*ProbKnowGivenDontScrewUp(n-1)))
n = 100
ProbKnowGivenDontScrewUp(n)
"""
    print("Recursive Function: {}" .format(timeit.timeit(code, number=runs)))
    code = """
def SameFunctionButNotRecursive(n):
    P0 = 0
    for i in range(n+1):
        if i == 0:
            P1 = 1/2
        else:
            P1 = 1/(1/3 + 2/(3*P0))
        P0 = P1
    return P1
n = 100
SameFunctionButNotRecursive(n)
"""
    print("Iterative Function: {}" .format(timeit.timeit(code, number=runs)))

if __name__ == "__main__":
    for n in range(10):
        print(ProbKnowGivenDontScrewUp(n))
