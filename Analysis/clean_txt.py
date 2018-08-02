import re
import sys
import nltk
#nltk.download("stopwords")
from nltk.stem import WordNetLemmatizer

sys.path.append('../..')
sys.path.append('..')


class CleanString:

    def __init__(self, text, extra_stopwords):
        self.text = text
        self.extra_stopwords = extra_stopwords

    # FUNCTIONS OPERATING ON STRINGS #

    def to_lowercase(self, text=None):
        """
        Convert all characters in a string to lowercase
        """

        if not text:
            text = self.text

        low_text = text.lower()

        return low_text

    def remove_references(self, text=None):
        """
        Function removes reference from the input text

        !Assumes that text is already lowercase!
        """

        if not text:
            text = self.text

        # Match 'references' starting from the end of the text (assumes text is already lowercase)
        idx = text.rfind('references')

        # Catching no references texts
        if (idx == -1):
            return text
        else:
            return text[:idx]

    def tokenize_text(self, text=None):

        if not text:
            text = self.text

        # Transform documents: tokenize and make lower case
        words = text.split(' ')

        return words

    # FUNCTIONS OPERATING ON VECTORIZED TEXTS #

    def remove_nonunicode(self, words=[]):

        if not words:
            words = self.tokenize_text()

        # Exclude non unicode characters
        clean_words = [re.sub(r'\W+', '', word) for word in words]

        return clean_words

    def remove_nummeric(self, words=[]):

        if not words:
            words = self.tokenize_text()

        # Exclude nummeric
        clean_words = [re.sub(r'[0-9]+', '', word) for word in words]

        return clean_words

    def remove_stopwords(self, words=[], extra_stopwords=[]):
        """
        Remove stop words from list of tokenized words

        extra_stopwords: list of context specific stopwords

        ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't",'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

        """
        if not words:
            words = self.tokenize_text()

        # List of stopwords
        stopwords = nltk.corpus.stopwords.words('english') + extra_stopwords

        # List of words that should not be removed
        not_stopwords = ['about', 'between', 'few', 'more', 'most', 'other', 'some']

        stopwords = [stop for stop in stopwords if stop not in not_stopwords]

        # Remove stop words
        clean_words = [word for word in words if (word not in stopwords)]

        return clean_words

    def stem_words(self, words=[]):
        """
        Stem words in list of tokenized words
        """

        if not words:
            words = self.tokenize_text()

        stemmer = LancasterStemmer()
        stems = []
        for word in words:
            stem = stemmer.stem(word)
            stems.append(stem)
        return stems

    def lemmatize_verbs(self, words=[]):
        """
        Lemmatize verbs in list of tokenized words
        """

        if not words:
            words = self.tokenize_text()

        lemmatizer = WordNetLemmatizer()
        lemmas = []
        for word in words:
            lemma = lemmatizer.lemmatize(word, pos='v')
            lemmas.append(lemma)
        return lemmas

    def normalize(self, text=None):
        if not text:
            text = self.text

        words = self.to_lowercase(text)
        words = self.remove_references(words)
        words = self.tokenize_text(words)
        words = self.remove_nonunicode(words)
        words = self.remove_nummeric(words)
        words = self.remove_stopwords(words, self.extra_stopwords)
        # Exclude empty
        words = [word for word in words if word != '']
        # Exclude single and two letter words
        words = [word for word in words if len(word) > 2]

        words = self.lemmatize_verbs(words)

        return words
