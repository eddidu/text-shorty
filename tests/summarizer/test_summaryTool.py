# -*- coding: utf8 -*-

import unittest
import numpy

from app.summarizer.summaryTool import LexrankSummarizer

class LexrankSummarizerTest(unittest.TestCase):
    """Test for `lexrank.py`."""

    def setUp(self):
        self.treshold = 0.1
        self.epsilon = 0.001
        self.summarizer = LexrankSummarizer()

    def test_normalize_matrix(self):
        """Does it successfully normalize matrix?"""
        input_matrix = [
            [0, 1.0],
            [1.0, 1.0]
        ]

        expected = [
            [0, 1],
            [0.5, 0.5]
        ]

        result = self.summarizer.normalize_matrix(input_matrix)

        self.assertEqual(expected, result)

    def test_normalize_matrix_with_only_zeros(self):
        """Does it successfully normalize matrix containing only zeros?"""
        input_matrix = [
            [0, 0],
            [0, 0]
        ]

        expected = [
            [0, 0],
            [0, 0]
        ]

        result = self.summarizer.normalize_matrix(input_matrix)

        self.assertEqual(expected, result)        

    def test_pick_best_sentences(self):
        """Does it successfully pick sentences repecting the ratings and orders?"""        
        input_sentences = (
            "first sentence",
            "second sentence",
            "third sentence",
            "fourth sentence"
        )

        input_ratings = [0.01, 0.015, 0.02, 0.005]

        input_length = 2

        expected = ["second sentence", "third sentence"]

        result = self.summarizer.pick_best_sentences(input_sentences, input_ratings, input_length)
        self.assertListEqual(expected, result)

    def test_pick_best_sentences_with_request_zero_sentences(self):
        """Does it successfully raise ValueError when 0 sentences are requested?"""        
        input_sentences = (
            "first sentence",
            "second sentence",
            "third sentence",
            "fourth sentence"
        )

        input_ratings = [0.01, 0.015, 0.02, 0.005]

        input_requested_numSentences = 0

        self.assertRaises(
            ValueError, 
            lambda: self.summarizer.pick_best_sentences(input_sentences, input_ratings, input_requested_numSentences)
        )

    def test_pick_best_sentences_with_request_more_sentences(self):
        """Does it successfully raise ValueError when requested sentences are greater than available sentences?"""        
        input_sentences = (
            "first sentence",
            "second sentence",
            "third sentence",
            "fourth sentence"
        )

        input_ratings = [0.01, 0.015, 0.02, 0.005]

        input_requested_numSentences = len(input_sentences) + 1

        self.assertRaises(
            ValueError,
            lambda: self.summarizer.pick_best_sentences(input_sentences, input_ratings, input_requested_numSentences)
        )     

    def test_summarize(self):
        """Does it successfully summarize given document?"""

        input_text = (
            """Lior Degani, the Co-Founder and head of Marketing of Swayy, pinged me last week when I was in California to tell me about his startup and give me beta access. I heard his pitch and was skeptical. I was also tired, cranky and missing my kids – so my frame of mind wasn’t the most positive.

            I went into Swayy to check it out, and when it asked for access to my Twitter and permission to tweet from my account, all I could think was, “If this thing spams my Twitter account I am going to bitch-slap him all over the Internet.” Fortunately that thought stayed in my head, and not out of my mouth.

            One week later, I’m totally addicted to Swayy and glad I said nothing about the spam (it doesn’t send out spam tweets but I liked the line too much to not use it for this article). I pinged Lior on Facebook with a request for a beta access code for TNW readers. I also asked how soon can I write about it. It’s that good. Seriously. I use every content curation service online. It really is That Good.

            What is Swayy? It’s like Percolate and LinkedIn recommended articles, mixed with trending keywords for the topics you find interesting, combined with an analytics dashboard that shows the trends of what you do and how people react to it. I like it for the simplicity and accuracy of the content curation. Everything I’m actually interested in reading is in one place – I don’t have to skip from another major tech blog over to Harvard Business Review then hop over to another major tech or business blog. It’s all in there. And it has saved me So Much Time



            After I decided that I trusted the service, I added my Facebook and LinkedIn accounts. The content just got That Much Better. I can share from the service itself, but I generally prefer reading the actual post first – so I end up sharing it from the main link, using Swayy more as a service for discovery.

            I’m also finding myself checking out trending keywords more often (more often than never, which is how often I do it on Twitter.com).



            The analytics side isn’t as interesting for me right now, but that could be due to the fact that I’ve barely been online since I came back from the US last weekend. The graphs also haven’t given me any particularly special insights as I can’t see which post got the actual feedback on the graph side (however there are numbers on the Timeline side.) This is a Beta though, and new features are being added and improved daily. I’m sure this is on the list. As they say, if you aren’t launching with something you’re embarrassed by, you’ve waited too long to launch.

            It was the suggested content that impressed me the most. The articles really are spot on – which is why I pinged Lior again to ask a few questions:

            How do you choose the articles listed on the site? Is there an algorithm involved? And is there any IP?

            Yes, we’re in the process of filing a patent for it. But basically the system works with a Natural Language Processing Engine. Actually, there are several parts for the content matching, but besides analyzing what topics the articles are talking about, we have machine learning algorithms that match you to the relevant suggested stuff. For example, if you shared an article about Zuck that got a good reaction from your followers, we might offer you another one about Kevin Systrom (just a simple example).

            Who came up with the idea for Swayy, and why? And what’s your business model?"""
        )

        input_length = 5

        result = self.summarizer.summarize(input_text, input_length)

        self.assertIsInstance(result, tuple)
        self.assertEqual(input_length, len(result))