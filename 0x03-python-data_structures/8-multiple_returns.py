#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or len(sentence) == 0:
        prim = (0, None)
    else:
        prim = (len(sentence), sentence[0])
    return prim
