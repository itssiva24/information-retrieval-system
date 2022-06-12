from util import *

# Add your import statements here
import re
from nltk.tokenize import TreebankWordTokenizer

punctuations = ['?', ':', '!', '.', ',', ';']

class Tokenization():

    def naive(self, text):
        """
        Tokenization using a Naive Approach

        Parameters
        ----------
        arg1 : list
                A list of strings where each string is a single sentence

        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of tokens
        """

        tokenizedText = None

        # Fill in code here
        tokenizedText = [sentence.split() for sentence in text]

        return tokenizedText

    def pennTreeBank(self, text):
        """
        Tokenization using the Penn Tree Bank Tokenizer

        Parameters
        ----------
        arg1 : list
                A list of strings where each string is a single sentence

        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of tokens
        """

        tokenizedText = None

        # Fill in code here
        tokenizedText = []
        for sentence in text:
                treebank_tokenizer = TreebankWordTokenizer()
                tokenized = treebank_tokenizer.tokenize(sentence)
                for word in tokenized:
                        if word in punctuations:
                                tokenized.remove(word)
                tokenizedText.append(tokenized)

        return tokenizedText
