"""
Script to read data from json databases and save them as DataFrames

Created on: Tue May 5 23:02:40 CEST 2018
@author: Wiktor

TO DO:
- how to deal with studies with multiple authors?
"""

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

# Load authors and list of their affiliations as DataFrame
institutions = pd.DataFrame.from_dict(authors, orient='index')['affiliations']

# List of authors that will be mapped to institutions
# (necessary since there can be more than one institution per author)
authors_index = institutions.index.values

# Merge all institutions into single list and to each institution append corresponding author (dict)
auth_aff = [dict(aff, **{'author': author}) for ls_aff, author in zip(institutions, authors_index) for aff in ls_aff]

# Convert authors affiliations to DataFrame
auth_aff = pd.DataFrame(auth_aff)
