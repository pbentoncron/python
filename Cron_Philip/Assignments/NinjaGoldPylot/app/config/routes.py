from system.core.router import routes

routes['default_controller'] = 'NinjaGold'
routes['POST']['/process_money'] = 'NinjaGold#process'
routes['/reset'] = 'NinjaGold#reset'
