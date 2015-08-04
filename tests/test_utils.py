# -*- coding: utf8 -*-
"""Test of utils for summarizer"""
import unittest

from app.summarizer import utils

class UtilsTest(unittest.TestCase):

    def test_to_sentences(self):
        input_text = '''
            This is a simple paragrraph for testing sentence tokenization.
            It only contains alpha numeric characters, and every sentence finishes property with proposition.
        '''

        expected = [
            'This is a simple paragrraph for testing sentence tokenization.',
            'It only contains alpha numeric characters, and every sentence finishes property with proposition.'
        ]

        result = utils.to_sentences(input_text)

        self.assertListEqual(expected, result)

    def test_to_words(self):
        input_text = 'I will go to swim, and you can come to swim with me.'

        expected = ['go', 'swim', 'come', 'swim']

        result = utils.to_words(input_text)

        self.assertListEqual(expected, result)        