from util import *

# Add your import statements here
import re
import nltk.data


class SentenceSegmentation():

    def naive(self, text):
        """
        Sentence Segmentation using a Naive Approach

        Parameters
        ----------
        arg1 : str
                A string (a bunch of sentences)

        Returns
        -------
        list
                A list of strings where each string is a single sentence
        """

        segmentedText = None

        # Fill in code here
        segmentedText = re.split("[.|,|;|?|!]", text.strip())
        segmentedText = [sentence for sentence in segmentedText if sentence]
        return segmentedText

    def punkt(self, text):
        """
        Sentence Segmentation using the Punkt Tokenizer

        Parameters
        ----------
        arg1 : str
                A string (a bunch of sentences)

        Returns
        -------
        list
                A list of strings where each strin is a single sentence
        """

        segmentedText = None

        # Fill in code here
        punk_sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        segmentedText = punk_sent_tokenizer.tokenize(text.strip())

        return segmentedText
