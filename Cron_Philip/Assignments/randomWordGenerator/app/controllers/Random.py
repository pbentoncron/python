from system.core.controller import *
import string
string.letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
random.choice(string.letters)

class Random(Controller):
    def __init__(self, action):
        super(Random, self).__init__(action)

        # self.load_model('WelcomeModel')
        # self.db = self._app.db
        
    def index(self):

        try:
            session['count']
        except:
            session['count'] = 1

        return self.load_view('index.html')

    def generate(self):
        session['word'] = ''.join([random.choice(string.ascii_letters + string.digits) for int in xrange(14)])
        session['count'] += 1
        return redirect('/')
