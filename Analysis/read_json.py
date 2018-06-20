"""
Script to read data from json databases and save them as DataFrames

Creates:
- get_author_institution(): pd.DataFrame (flat json) with author and institution
he/she is affliated to. One author can have multiple entries.

- get_study_author(): pd.DataFrame with author and study index, that will allow
to map study to author affiliation from get_author_institution() based on author_index

Created on: Tue May 5 23:02:40 CEST 2018
@author: Wiktor

"""

import pandas as pd
import json
from pprint import pprint
import os
import sys


if sys.platform == "linux":
    studies_path = "/home/wiktor/git/MasterThesis/Literature/Competition_Studies_Database/studies.json"
    authors_path = "/home/wiktor/git/MasterThesis/Literature/Competition_Studies_Database/authors.json"
else:
    studies_path = "/Users/Wiktor/Dropbox/Git/MasterThesis/Literature/Competition_Studies_Database/studies.json"
    authors_path = "/Users/Wiktor/Dropbox/Git/MasterThesis/Literature/Competition_Studies_Database/authors.json"


# Reading authors database
with open(os.path.join(authors_path)) as file:
    authors = json.load(file)


def get_author_institution(json_authors):
    """
    Function that reads in the database .json file and returns flat pd.DataFrame with author and her/his institutions
    """

    # Load authors and list of their affiliations as DataFrame
    institutions = pd.DataFrame.from_dict(json_authors, orient='index')['affiliations']

    # List of authors that will be mapped to institutions
    # (necessary since there can be more than one institution per author)
    authors_index = institutions.index.values

    # Merge all institutions into single list and to each institution append corresponding author (dict)
    authors_institutions = [dict(affiliation, **{'author': author}) for ls_affiliations, author in zip(institutions, authors_index)
                                                                    for affiliation in ls_affiliations]

    # Convert authors institutions to DataFrame
    authors_institutions = pd.DataFrame(authors_institutions)

    return authors_institutions


# Reading studies database
with open(os.path.join(studies_path)) as file:
    studies = json.load(file)


def get_study_author(json_studies):

    # Load articles and their authors as a list
    articles = pd.DataFrame.from_dict(studies, orient='index')['authors']

    # Create index of aticles
    articles_index = articles.index.values

    # Join all authors into a single list and to each author assign corresponding article
    studies_authors = [dict(author, **{'study': article}) for ls_articles, article in zip(articles, articles_index)
                                                          for author in ls_articles]

    # Get only author and study index (ignore name and surname)
    studies_authors = pd.DataFrame(studies_authors)[['index', 'study']]

    studies_authors.columns = ['author_index', 'study_index']

    return studies_authors
