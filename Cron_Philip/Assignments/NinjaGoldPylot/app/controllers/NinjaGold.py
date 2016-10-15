
from system.core.controller import *
import random, datetime

class NinjaGold(Controller):
    def __init__(self, action):
        super(NinjaGold, self).__init__(action)

        self.load_model('NinjaGoldModel')
        self.db = self._app.db
        
    def index(self):
        if not 'gold' in session:
            session['gold'] = 0
        if not 'activities' in session:
            session['activities'] = []
        return self.load_view('index.html', goldCount=session['gold'], activity=session['activities'])

    def process(self):
        locations = {
        'farm':random.randint(10, 20),
        'cave':random.randint(5, 10),
        'house':random.randint(2, 5),
        'casino':random.randint(-50, 50)
        }
        if request.form['location'] in locations:
            result = locations[request.form['location']]
            session['gold'] = session['gold'] + result
            session['activities'].append("{} {} golds from the {} ({})".format(('lost', 'Earned')[result > 0], abs(result), request.form['location'], datetime.datetime.now()))
        return redirect('/')

    def reset(self):
        session.clear()
        return redirect('/')


