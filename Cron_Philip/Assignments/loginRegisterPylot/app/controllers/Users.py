from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        
    def index(self):

        return self.load_view('index.html')

    def register(self):
        register_data = {
            'first_name': request.form['fname'],
            'last_name': request.form['lname'],
            'email': request.form['email'],
            'password': request.form['password'],
            'Cpassword': request.form['Cpassword']
        }

        add_response = self.models['User'].add_user(register_data)

        # check for errors first
        if len(add_response['errors']) > 0:
            for error in add_response['errors']:
                # change category if using bootstrap class
                flash(error, 'regError')
            return redirect('/')

        #if no errors, overwrite user_id with user record
        #then login and redirect
        get_response = self.models['User'].get_user_by_id(add_response['user_id'])

        session['user'] = get_response['user'][0]

        return redirect('/success')

    def login(self):
        login_data = {
            'email': request.form['email'],
            'password': request.form['password']
        }

        #query for user with supplied email
        response = self.models['User'].get_user_by_email(login_data)

        #verify user exist with that email, otherwise errors
        if len(response['errors']) > 0:
            for error in response['errors']:
                # change category if using bootstrap class
                flash(error, 'logError')
            return redirect('/')

        #login user
        session['user'] = response['user'][0]

        return redirect('/success')

    def success(self):

        if not 'user' in session:
            flash('Not logged in, please login!')
            return redirect('/')

        return self.load_view('success.html', user=session['user'])

    def logout(self):
        session.clear()
        return redirect('/')
