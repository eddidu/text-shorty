from flask import Blueprint, request, Response, abort, url_for, redirect, json, render_template
from app.summarizer import lexrank

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@main.route('/api/summarizer', methods=['POST'])
def summarize():

	if not request.json or 'text' not in request.json or len(request.json['text'].strip()) == 0:
		abort(400)

	text = request.json['text']	

	if 'length' in request.json:
		length = request.json['length']
	else:
		# TODO: need to check if text contains more than 5 sentences...otherwise, this will cause an error
		length = 5

	summarizer = lexrank.LexrankSummarizer()
	summary = summarizer.summarize(text, length)

	result = {'summary': summary}

	return Response(json.dumps(result, ensure_ascii=False), mimetype='application/json')
