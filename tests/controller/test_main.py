from flask.ext.testing import TestCase
import mock

from flask import Flask, json
from app.controllers.main import main

class MainTest(TestCase):
    """Test for `main.py`."""

    render_templates = False  

    def create_app(self):
        app = Flask(
            __name__,
            template_folder="../../app/static/templates"
        )
        app.config["TESTING"] = True
        app.register_blueprint(main)

        return app      

    def test_api_base(self):
        """Does it successfully return index.html when base is called?"""
        response = self.client.get("/")

        self.assert_template_used("index.html")

    def test_api_summary_with_invalid_method(self):
        """Does it successfully return 405 when request method is not `POST`"""
        get_response = self.client.get("/api/summary")
        put_response = self.client.put("/api/summary")        
        
        self.assertEqual(405, get_response.status_code) 
        self.assertEqual(405, put_response.status_code)      

    def test_api_summary_with_invalid_request(self):
        """Does it successfully return 400 when post request does not contain `text` attribute"""
        response = self.client.post("/api/summary")
        
        self.assertEqual(400, response.status_code)      

    @mock.patch('app.controllers.main.LexrankSummarizer')
    def test_api_summary(self, MockClass):
        """Does it successfully return summary?"""
        dummy_text = "dummy text"
        dummy_length = 1
        dummy_data = json.dumps({"text": dummy_text, "length": dummy_length})
        dummy_response = ["mock", "value"]

        instance = MockClass.return_value
        instance.summarize.return_value = dummy_response

        response = self.client.post(
            "/api/summary", 
            data=dummy_data,
            content_type="application/json"
        )
        
        instance.summarize.assert_called_once_with(dummy_text, dummy_length)
        self.assertIn(json.dumps(dummy_response), response.data)

    def test_api_keywords_with_invalid_method(self):
        """Does it successfully return 405 when request method is not `POST`"""
        get_response = self.client.get("/api/keywords")
        put_response = self.client.put("/api/keywords")        
        
        self.assertEqual(405, get_response.status_code) 
        self.assertEqual(405, put_response.status_code)      

    def test_api_keywords_with_invalid_request(self):
        """Does it successfully return 400 when post request does not contain `text` attribute"""
        response = self.client.post("/api/keywords")
        
        self.assertEqual(400, response.status_code)      

    @mock.patch('app.controllers.main.KeywordsExtractor')
    def test_api_keywords(self, MockClass):
        """Does it successfully return summary?"""
        dummy_text = "dummy text"
        dummy_data = json.dumps({"text": dummy_text})
        dummy_response = ["mock", "value"]

        instance = MockClass.return_value
        instance.extract.return_value = dummy_response

        response = self.client.post(
            "/api/keywords", 
            data=dummy_data,
            content_type="application/json"
        )
        
        instance.extract.assert_called_once_with(dummy_text)
        self.assertIn(json.dumps(dummy_response), response.data)