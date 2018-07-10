"""
This script loads collected PDFs and saves them in .txt format

Created on: Do 21. Jun 15:06:21 CEST 2018
"""
import os
import sys
from timeit import default_timer as timer
from read_pdf import pdf2text

if sys.platform == "linux":
    studies_path = "/home/wiktor/git/MasterThesis/Literature/Competition_Studies_Database/studies.json"
    authors_path = "/home/wiktor/git/MasterThesis/Literature/Competition_Studies_Database/authors.json"
    studies_location = "/home/wiktor/Dropbox/Git/MasterThesis/Literature/Competition_Studies_Database/"
else:
    studies_path = "/Users/Wiktor/Dropbox/Git/MasterThesis/Literature/Competition_Studies_Database/studies.json"
    authors_path = "/Users/Wiktor/Dropbox/Git/MasterThesis/Literature/Competition_Studies_Database/authors.json"
    studies_location = "/Users/Wiktor/Dropbox/Git/MasterThesis/Literature/Competition_Studies_Database/"


def read_and_transform(studies_path):
    """
    Function to read all .pdf files from given location and transform them into .txt files

    Argumens:
     - studies_path: path to .json file, database with collected competition studies
     - studies_location: location of the directory where the collected documents are located

    Returns:
     - .txt files in given directory that correspond to the matching .pdfs
    """

    # Load studies labels
    study_labels = [x for x in os.listdir(studies_location)]

    # Creating paths to the documents
    study_paths = [studies_location + x for x in study_labels]

    # Excluding not .pdf files
    study_labels = [pdf for pdf in study_labels if '.pdf' in pdf]
    study_paths = [pdf for pdf in study_paths if '.pdf' in pdf]

    # Creating list of doubles study label and its path
    reading_list = zip(study_labels, study_paths)

    # Start time
    start = timer()

    # Loading each study and converting it to txt file
    for label, text in reading_list:

        print("Loading paper: {}".format(label))

        # Creating .txt file with label as a name
        write_file = label.split('.')[0] + '.txt'

        with open(write_file, 'w+') as text_file:
            # Writing converted pdf to .txt format
            text_file.write(pdf2text(text))
            text_file.close()

        print("Study saved to: {}".format(write_file))

    end = timer()

    print("Process took: {} seconds".format(end - start))


if __name__ == '__main__':
    read_and_transform(studies_path=studies_path)
