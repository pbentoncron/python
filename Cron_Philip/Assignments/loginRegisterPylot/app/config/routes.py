from system.core.router import routes

routes['default_controller'] = 'Users'
routes['POST']['/login'] = 'Users#login'
routes['POST']['/register'] = 'Users#register'
routes['/success'] = 'Users#success'
routes['/logout'] = 'Users#logout'
