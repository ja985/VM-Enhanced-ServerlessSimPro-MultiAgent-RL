# -*- coding: utf-8 -*-
# Extended for VM-aware MAPPO-based serverless scheduling framework

import random


def EarliestKilled(spareCon2ThisReq):
    bestContainer = None
    for c in spareCon2ThisReq:
        if bestContainer is None or bestContainer.killedTime > c.killedTime:
            bestContainer = c
    return bestContainer


def LatestKilled(spareCon2ThisReq):
    bestContainer = None
    for c in spareCon2ThisReq:
        if bestContainer is None or bestContainer.killedTime < c.killedTime:
            bestContainer = c
    return bestContainer


def RandomSelection(spareCon2ThisReq):
    bestContainer = None
    if len(spareCon2ThisReq) > 0:
        index = random.randint(0, len(spareCon2ThisReq)-1)
        bestContainer = spareCon2ThisReq[index]
    return bestContainer