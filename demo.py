from wallet import *

x = Wallet("Euro", "Name1")
x.info()

x.upMoney(1000)
x.downMoney(100)

x.info()

y = Wallet("Euro", "Name2")
y.info()

y.upMoney(x.downMoney(500))

x.info()
y.info()