from system.core.controller import *
from time import strftime

class Times(Controller):

    def __init__(self, action):
        super(Times, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):

        current_time = strftime("%c")
        return self.load_view('index.html', time=current_time)
