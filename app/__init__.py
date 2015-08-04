from flask import Flask

from app.controllers.main import main

def create_app(object_name):
	'''
	Arguments:
	    object_name: path of the config
	'''

	app = Flask(__name__, static_folder='static', template_folder='static/templates')

	# register blueprints
	app.register_blueprint(main)

	return app