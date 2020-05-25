# server.py

import rpcserver

def add(a, b, c=10):
    sum = a + b + c
    return sum

s = rpcserver.RPCServer()
s.register_function(add) 
s.loop(8880) 

