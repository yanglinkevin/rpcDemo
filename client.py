import rpcclient

c = rpcclient.RPCClient()
c.connect('127.0.0.1', 8880)
res = c.add(1, 2, c=3)
print(res)
