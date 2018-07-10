import re
import sys

sys.path.append('../..')
sys.path.append('..')


def remove_references(string):
    """
    Function removes reference from the input text
    """
    text = string

    # Convert capital letters to lower
    text_low = text.lower()

    # Match 'references' starting from the end of the text
    idx = text_low.rfind('references')

    # Catching no references texts
    if (idx == -1):
        return text
    else:
        return text[:idx]


def remove_numeric(string):

    text = string

    # Remove numbers
    clean_text = re.sub('1|2|3|4|5|6|7|8|9|0', ' ', text)

    return clean_text


def remove_strange(string):
    text = string

    # Remove strange characters
    clean_text = re.sub('.|/|,|!|@|#|$|%|^|*|~|?|[|]|"|}|{||;|:|§|£|+|=|&', '', text)

    return clean_text


def clean_string(string):
    text = string

    ftext = remove_numeric(text)
    #ftext = remove_strange(ftext)

    return ftext
