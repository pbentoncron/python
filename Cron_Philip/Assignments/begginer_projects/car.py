class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
    def display_all(self):
        print self.price
        print self.speed
        print self.fuel
        print self.mileage
        print self.tax

a = Car(2000, '15mph', 'half full', '15mpg')
b = Car(1000, '25mph', 'empty', '25mpg')
c = Car(7000, '28mph', 'full', '56mpg')
d = Car(10000, '35mph', 'empty', '45mpg')
e = Car(20000, '35mph', 'half full', '25mpg')
f = Car(200000, '35mph', 'full', '15mpg')

a.display_all()
b.display_all()
c.display_all()
d.display_all()
e.display_all()
f.display_all()