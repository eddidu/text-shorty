from flask import Flask, redirect

from app.controllers.main import main

def create_app(object_name):
	'''
	Arguments:s
	    object_name: path of the config
	'''

	APP_ROOT = '/text-shorty'

	app = Flask(__name__, static_folder='static', template_folder='static/templates')

	@app.route('/', methods=['GET'])
	def redirect_to_main():
		return redirect(APP_ROOT, code=302)

	# register blueprints
	app.register_blueprint(main, url_prefix=APP_ROOT)

	return app