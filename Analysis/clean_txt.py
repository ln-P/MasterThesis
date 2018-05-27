import nltk
import re
import sys

sys.path.append('../..')
sys.path.append('..')

from read_pdf import PDF2Text as p2t

# Loading a file
test = p2t.convert_pdf_to_txt('/Users/Wiktor/Dropbox/Git/MasterThesis/Literature/Competition_Studies_Database/p001.pdf')


class CleanText(object):

    def remove_references(text):
        """
        Function removes reference from the input text
        """

        # Convert capital letters to lower
        text_low = text.lower()

        # Match 'references' starting from the end of the text
        idx = text_low.rfind('references')

        # Catching no references texts
        if (idx == -1):
            return text
        else:
            return text[:idx]

    def remove_numeric(text):

        # Remove numbers
        clean_text = re.sub('1|2|3|4|5|6|7|8|9|0', '', text)

        return clean_text

    def remove_strange(text):

        # Remove strange characters
        clean_text = re.sub('.|/|,|!|@|#|$|%|^|*|~|?|[|]|"|}|{||;|:|§|£|+|=', '', test)

        return clean_text
