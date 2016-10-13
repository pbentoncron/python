class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        print 'walking'
        self.health -= 1
        return self
    def run(self):
        print 'running'
        self.health -= 5
        return self
    def displayHealth(self):
        print ('Name: {}'.format(self.name))
        print ('Health: {}'.format(self.health))
        return self

animal = Animal('Animal')
animal.walk().walk().walk().run().run().displayHealth()
