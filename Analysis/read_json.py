import pandas as pd
import json
from pprint import pprint
import os

studies_path = "/Users/Wiktor/Dropbox/Git/MasterThesis/Literature/Competition_Studies_Database/studies.json"
authors_path = "/Users/Wiktor/Dropbox/Git/MasterThesis/Literature/Competition_Studies_Database/authors.json"

# Reading studies database
with open(os.path.join(studies_path)) as file:
    studies = json.load(file)

# Reading authors database
with open(os.path.join(authors_path)) as file:
    authors = json.load(file)

for paper in studies:
    for author in studies[paper]["authors"]:
        print(paper, author['index'])
