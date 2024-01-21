#!/usr/bin/python

def multiple_returns(sentence):
    return (len(sentence), None if len(sentence) == 0 else sentence[0])
