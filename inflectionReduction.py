from util import *

# Add your import statements here
import nltk
from nltk.stem import WordNetLemmatizer


nltk.download('wordnet')


class InflectionReduction:

    def reduce(self, text):
        """
        Stemming/Lemmatization

        Parameters
        ----------
        arg1 : list
                A list of lists where each sub-list a sequence of tokens
                representing a sentence

        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of
                stemmed/lemmatized tokens representing a sentence
        """

        reducedText = None

        # Fill in code here
        wordnet_lemmatizer = WordNetLemmatizer()
        reducedText = [[wordnet_lemmatizer.lemmatize(
            word) for word in sentence] for sentence in text]

        return reducedText
