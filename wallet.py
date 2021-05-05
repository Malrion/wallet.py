class Wallet:
    def __init__ (self, curency, name = "Unknown"):
        self.__money = 0.0
        self.curency = curency
        self.name = name

    def info (self):
        print (self.name[:-1] + " has " + str(self.__money) + " " + self.curency)


    def upMoney(self, howmoney):
        self.__money += howmoney
        print("The operation was successful!")
        return howmoney

    def downMoney (self, howmoney):
        if (0 <= self.__money - howmoney):
            self.__money -= howmoney
            print("The operation was successful!")
        else:
            print("Not enough funds, top up your account")
        return howmoney

    def __del__(self):
        return "Wallet deleted"
