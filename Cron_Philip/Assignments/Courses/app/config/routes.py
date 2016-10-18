from system.core.router import routes

routes['default_controller'] = 'Courses'
routes['POST']['/courses/show'] = 'Courses#show'
routes['POST']['/courses/add'] = 'Courses#add'
routes['POST']['/courses/update'] = 'Courses#update'
routes['/courses/destroy/<int:course_id>'] = 'Courses#delete'
