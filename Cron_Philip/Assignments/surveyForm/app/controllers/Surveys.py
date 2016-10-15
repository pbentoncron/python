from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

        self.load_model('SurveyModel')
        self.db = self._app.db
        
    def index(self):

        return self.load_view('index.html')

    def process(self):

        if len(request.form['name']) < 1:
            flash("Name cannot be empty!", 'flash')
            return redirect('/')

        elif len(request.form['comment']) > 120:
            flash("120 or less!", 'flash')
            return redirect('/')

        try:
            session['count']
        except:
            session['count'] = 1

        session['name'] = request.form['name']
        session['dojo_location'] = request.form['dojo_location']
        session['favorite_language'] = request.form['favorite_language']
        session['comment'] = request.form['comment']
        return redirect('/result')

    def result(self):
        session['count'] += 1
        return self.load_view('result.html')

