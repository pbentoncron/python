from system.core.controller import *
class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        # Note that we have to load the model before using it
        self.load_model('Course')

    def index(self):
        course = self.models['Course'].get_all_courses()
        print course
        return self.load_view('index.html', course=course)

    def add(self):
        if len(request.form['name']) < 1:
            flash("Name cannot be empty!", 'flash')
            return redirect('/')

        self.models['Course'].add_course(request.form)
        return redirect('/')

    def delete(self, course_id):
        print course_id
        self.models['Course'].delete_course(course_id)
        return redirect('/')
