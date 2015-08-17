import unittest

from app.summarizer import analysisTool
from app.summarizer.document import Document, Sentence

class AnalysisToolTest(unittest.TestCase):
    """Test for `AnalysisTool.py`."""

    def test_compute_tf(self):
        """Does it successfully compute tf for a given sentence?"""
        input_item = Sentence("I never stop at the stop sign")

        expected = {"i": 1, "never": 1, "stop": 2, "at": 1, "the": 1, "sign": 1}

        result = analysisTool.compute_tf(input_item)

        self.assertDictEqual(expected, result)

    def test_commpute_idf(self):
        """Does it successfully compute idf for given sentences?"""
        input_item = Document("This is a sample. This is another example.")

        result = analysisTool.compute_idf(input_item.sentences)

        expected_keys = ["this", "is", "a", "sample", "another", "example"]

        for key in expected_keys:
            self.assertIn(key, result.keys())

        self.assertEqual(0, result["this"])
        self.assertEqual(0, result["is"])
