import re
import sys
import nltk
from nltk.stem import WordNetLemmatizer

sys.path.append('../..')
sys.path.append('..')


# FUNCTIONS OPERATING ON STRINGS #

def to_lowercase(text):
    """
    Convert all characters in a string to lowercase
    """
    low_text = text.lower()

    return low_text


def remove_references(text):
    """
    Function removes reference from the input text

    !Assumes that text is already lowercase!
    """

    # Match 'references' starting from the end of the text (assumes text is already lowercase)
    idx = text.rfind('references')

    # Catching no references texts
    if (idx == -1):
        return text
    else:
        return text[:idx]


def remove_stopwords(text, extra_stopwords):
    """
    Remove stop words from list of tokenized words

    extra_stopwords: list of context specific stopwords

    ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't",'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

    """

    # List of stopwords
    stopwords = nltk.corpus.stopwords.words('english') + extra_stopwords

    # List of words that should not be removed
    not_stopwords = ['about', 'between', 'few', 'more', 'most', 'other', 'some']

    stopwords = [stop for stop in stopwords if stop not in not_stopwords]

    # Remove stop words
    clean_words = ' '.join([word for word in text.split(' ') if word not in stopwords])

    return clean_words


def tokenize_text(text):

    # Transform documents: tokenize and make lower case
    words = text.split(' ')

    return words


# FUNCTIONS OPERATING ON VECTORIZED TEXTS #

def remove_nonunicode(words, stops=True):
    """
    Accepts list of words and removes unicode characters from them
    """

    # Exclude non unicode characters
    if stops is False:
        clean_words = [re.sub(r'[^a-zA-Z\d\.]', '', word) for word in words]
    else:
        clean_words = [re.sub(r'[^a-zA-Z\d]', '', word) for word in words]

    return clean_words


def remove_nummeric(words):

    # Exclude nummeric
    clean_words = [re.sub(r'[0-9]+', '', word) for word in words]

    return clean_words


def lemmatize_verbs(words):
    """
    Lemmatize verbs in list of tokenized words
    """

    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return lemmas


def normalize(text, extra_stopwords, exclude_stops=True):

    words = to_lowercase(text)
    words = remove_references(words)
    words = remove_stopwords(words, extra_stopwords)
    words = tokenize_text(words)
    words = remove_nonunicode(words, exclude_stops)
    words = remove_nummeric(words)
    # Exclude empty
    words = [word for word in words if word != '']
    # Exclude single and two letter words
    words = [word for word in words if len(word) > 3]

    words = lemmatize_verbs(words)

    return words
