class Hotel:
    def __init__(self,price=200,cutoff=1.0,bre=15):
        self.price=price
        self.cutoff=cutoff
        self.bre=bre

    def calc(self,days=1):
        return (self.price * self.cutoff + self.bre) * days

if __name__ == '__main__':
    stdroom=Hotel()
    bigred=Hotel(300,0.88)
    print(stdroom.calc())
    print(stdroom.calc(3))
    print(bigred.calc())
    print(bigred.calc(3))
