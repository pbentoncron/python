class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print self.price 
        print self.max_speed 
        print self.miles
    def ride(self):
        print 'riding'
        self.miles += 10
        return self
    def reverse(self):
        print 'Reversing'
        if self.miles >= 5:
            self.miles -= 5
        return self
bike1 = Bike(200, "25mph", 20)
bike2 = Bike(100, "30mph", 40)
bike3 = Bike(400, "75mph", 80)

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()










