import unittest

from app.summarizer import analysisTool

class AnalysisToolTest(unittest.TestCase):
    """Test for `AnalysisTool.py`."""

    def test_compute_tf(self):
        """Does it successfully compute tf for a given sentence?"""
        input_tokens = [
            "never", 
            "stop",
            "stop",
            "sign"
        ]

        expected = {"never": 1, "stop": 2, "sign": 1}

        result = analysisTool.compute_tf(input_tokens)

        self.assertDictEqual(expected, result)

    def test_commpute_idf(self):
        """Does it successfully compute idf for given sentences?"""
        input_vectors = [
            ["this", "is", "a", "sample"],
            ["this", "is", "another", "example"]
        ]

        result = analysisTool.compute_idf(input_vectors)

        expected_keys = ["this", "is", "a", "sample", "another", "example"]

        for key in expected_keys:
            self.assertIn(key, result.keys())
        self.assertEqual(0, result["this"])
        self.assertEqual(0, result["is"])