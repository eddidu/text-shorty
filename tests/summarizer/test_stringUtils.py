# -*- coding: utf8 -*-

import unittest
from app.summarizer import stringUtils

class StringUtilsTest(unittest.TestCase):
    """Test for `stringUtils.py`."""    

    def test_sent_tokenize(self):
        """Does it successfully tokenize sentences?"""
        input_text = """
            A first line.
            Next line.
        """

        expected = (
            "A first line.",
            "Next line."
        )

        result = stringUtils.sent_tokenize(input_text)

        self.assertTupleEqual(expected, result)

    def test_sent_tokenize_string_with_tabs(self):
        """Does it successfully tokenize sentences containing tabs?"""        
        input_text = """
            A first \t\tline. \t\t
            Next line.
        """

        expected = (
            "A first line.",
            "Next line."
        )

        result = stringUtils.sent_tokenize(input_text)

        self.assertTupleEqual(expected, result)        

    def test_sent_tokenize_string_with_newlines(self):
        """Does it successfully tokenize sentences containing newlines?"""        
        input_text = """
            A first \n\nline. \n\n
            Next line.
        """

        expected = (
            "A first line.",
            "Next line."
        )

        result = stringUtils.sent_tokenize(input_text)

        self.assertTupleEqual(expected, result)

    def test_sent_tokenize_string_with_single_quotation_marks(self):
        """Does it successfully tokenize sentence containing ‘ and ’ ?"""        
        input_text = """
            A first line.
            I’ve next line here.
        """

        expected = (
            "A first line.",
            "I've next line here."
        )

        result = stringUtils.sent_tokenize(input_text)

        self.assertTupleEqual(expected, result)        

    def test_sent_tokenize_string_with_double_qutation_marks(self):
        """Does it successfully tokenize sentences containing “ and ” ?"""    
        input_text = """
            A first line.
            Next line is, 
            “inside non ascii double quotes.”
        """

        expected = (
            "A first line.",
            "Next line is, inside non ascii double quotes."
        )

        result = stringUtils.sent_tokenize(input_text)

        self.assertTupleEqual(expected, result)

    def test_word_tokenize(self):
        """Does it successfully tokenize words?"""        
        input_text = """
            How do you choose the articles listed on the site?
        """

        expected = (
            "how", 
            "do",
            "you",
            "choose",
            "the",
            "articles",
            "listed",
            "on",
            "the",
            "site",
            "?"
        )

        result = stringUtils.word_tokenize(input_text)

        self.assertTupleEqual(expected, result)