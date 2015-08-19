# -*- coding: utf8 -*-

import unittest
from app.summarizer import stringUtils

class StringUtilsTest(unittest.TestCase):
    """Test for `stringUtils.py`."""    

    def test_sent_tokenize(self):
        """Does it successfully tokenize sentences?"""
        input_text = (
            "A first line.\n"
            "Next line."
        )

        expected = (
            "A first line.",
            "Next line."
        )

        result = stringUtils.sent_tokenize(input_text)

        self.assertTupleEqual(expected, result)

    def test_sent_tokenize_string_with_tabs(self):
        """Does it successfully tokenize sentences containing tabs?"""        
        input_text = (
            "A first \t\tline. \t\t\n"
            "\t\t\n"
            "Next line."
        )

        expected = (
            "A first line.",
            "Next line."
        )

        result = stringUtils.sent_tokenize(input_text)

        self.assertTupleEqual(expected, result)        

    def test_sent_tokenize_string_with_newlines(self):
        """Does it successfully tokenize sentences containing newlines?"""        
        input_text = (
            "A first \n\nline. \n\n"
            "\n\n"
            "Next line."
        )

        expected = (
            "A first line.",
            "Next line."
        )

        result = stringUtils.sent_tokenize(input_text)

        self.assertTupleEqual(expected, result)

    def test_sent_tokenize_string_with_single_quotation_marks(self):
        """Does it successfully tokenize sentence containing ‘ and ’ ?"""        
        input_text = (
            """A first line.
            I’ve next line here."""
        )

        expected = (
            "A first line.",
            "I've next line here."
        )

        result = stringUtils.sent_tokenize(input_text)

        self.assertTupleEqual(expected, result)        

    def test_sent_tokenize_string_with_double_qutation_marks(self):
        """Does it successfully tokenize sentences containing “ and ” ?"""    
        input_text = (
            "A first line.\n"
            "Next line is, "
            "“inside non ascii double quotes.”"
        )

        expected = (
            "A first line.",
            "Next line is, \"inside non ascii double quotes.\""
        )

        result = stringUtils.sent_tokenize(input_text)

        self.assertTupleEqual(expected, result)

    def test_word_tokenize(self):
        """Does it successfully tokenize words?"""        
        input_text = "This is a sample."

        expected = (
            "this",
            "is",
            "a",
            "sample"
        )

        result = stringUtils.word_tokenize(input_text, filter_stopwords=False, stem=False)

        self.assertTupleEqual(expected, result)      

    def test_word_tokenize_with_stopwords_filter(self):
        """Does it successfully tokenize words with stopwords filter option?"""        
        input_text = "How do you choose the article that's listed on the site."

        expected = (
            "choose",
            "article",
            "listed",
            "site"
        )

        result = stringUtils.word_tokenize(input_text, filter_stopwords=True)

        self.assertTupleEqual(expected, result)

    def test_word_tokenize_with_stem(self):
        """Does it successfully tokenize words with stem option?"""        
        input_text = "crying buying"

        expected = (
            "cry",
            "buy"
        )

        result = stringUtils.word_tokenize(input_text, filter_stopwords=False, stem=True)

        self.assertTupleEqual(expected, result)