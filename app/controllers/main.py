from flask import Blueprint, request, Response, abort, url_for, redirect, json, render_template
from app.summarizer.summaryTool import LexrankSummarizer
from app.summarizer.keywordsTool import KeywordsExtractor

main = Blueprint("main", __name__)

@main.route("/", methods=["GET"])
def index():
    """Return main page"""
    return render_template("index.html")

@main.route("/api/summary", methods=["POST"])
def getSummary():
    """Return sentences summarizing the document"""
    if not request.json or "text" not in request.json or len(request.json["text"].strip()) == 0:
        abort(400)

    text = request.json["text"]    
    length = 5
    if "length" in request.json:
        length = request.json["length"]

    summary = LexrankSummarizer().summarize(text, length)
    result = {"result": summary}

    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json")

@main.route("/api/keywords", methods=["POST"])
def getKeywords():
    """Return extracted keywords"""

    if not request.json or "text" not in request.json or len(request.json["text"].strip()) == 0:
        abort(400)

    text = request.json["text"]       
    keywords = KeywordsExtractor().extract(text)
    result = {"result": keywords}

    return Response(json.dumps(result, ensure_ascii=False), mimetype="application/json")
