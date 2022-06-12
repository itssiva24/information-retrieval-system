from util import *

# Add your import statements here
import nltk
from nltk.corpus import stopwords


class StopwordRemoval():

    def fromList(self, text):
        """
        Sentence Segmentation using the Punkt Tokenizer

        Parameters
        ----------
        arg1 : list
                A list of lists where each sub-list is a sequence of tokens
                representing a sentence

        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of tokens
                representing a sentence with stopwords removed
        """

        stopwordRemovedText = None

        # Fill in code here
        stopwordRemovedText = [[word for word in tokenized_sent if word not in stopwords.words('english')] for tokenized_sent in text]

        return stopwordRemovedText
