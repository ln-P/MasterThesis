"""
This script loads collected PDFs and saves them in .txt format

Created on: Do 21. Jun 15:06:21 CEST 2018
"""
import json
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

# Reading studies database
with open(os.path.join(studies_path)) as file:
    studies = json.load(file)

# Load studies labels
study_labels = [x for x in os.listdir(studies_location)]

# Excluding problematic texts this lead to removing study 17
# exclude = ['p017.pdf']
# study_labels = [text for text in study_labels if text not in exclude]

study_paths = [studies_location + x for x in study_labels]

# Excluding not .pdf files
study_labels = [pdf for pdf in study_labels if '.pdf' in pdf]
study_paths = [pdf for pdf in study_paths if '.pdf' in pdf]


reading_list = list(zip(study_labels, study_paths))

start = timer()

for label, text in zip(study_labels, study_paths):

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
