"""
This script provides wide range of functions that use combination of the authors
and articles databases (.json) to extract information

Creates:
- get_author_institution(): pd.DataFrame (flat json) with author and institution
he/she is affliated to. One author can have multiple entries.

- get_study_author(): pd.DataFrame with author and study index, that will allow
to map study to author affiliation from get_author_institution() based on author_index

- central_bank_paper_label(): returns list of papers that had one of the authors affiliated with the central bank

Author: Wiktor
Created on: Tue May 5 23:02:40 CEST 2018
"""

import pandas as pd
import json
import os


class JsonHelpers:

    def __init__(self, authors_path=None, studies_path=None):

        if authors_path is None:
                authors_path = "/Users/Wiktor/Dropbox/Git/MasterThesis/Literature/Competition_Studies_Database/authors.json"

        if studies_path is None:
            studies_path = "/Users/Wiktor/Dropbox/Git/MasterThesis/Literature/Competition_Studies_Database/studies.json"

        # Reading authors database
        with open(os.path.join(authors_path)) as file:
            self.authors = json.load(file)

        # Reading studies database
        with open(os.path.join(studies_path)) as file:
            self.studies = json.load(file)

    def get_author_institution(self):
        """
        Function that reads in the database .json file and returns flat pd.DataFrame
        with author and her/his institutions
        """

        # Load authors and list of their affiliations as DataFrame
        institutions = pd.DataFrame.from_dict(self.authors, orient='index')['affiliations']

        # List of authors that will be mapped to institutions
        # (necessary since there can be more than one institution per author)
        authors_index = institutions.index.values

        # Merge all institutions into single list and to each institution append corresponding author (dict)
        authors_institutions = [dict(affiliation, **{'author': author}) for list_affiliations, author in zip(institutions, authors_index)
                                                                        for affiliation in list_affiliations]

        # Convert authors institutions to DataFrame
        authors_institutions = pd.DataFrame(authors_institutions)

        return authors_institutions

    def get_study_author(self):
        """
        Function that reads in the database .json file and returns flat pd.DataFrame
        with author and her/his studies
        """

        # Load articles and their authors as a list
        articles = pd.DataFrame.from_dict(self.studies, orient='index')['authors']

        # Create index of aticles
        articles_index = articles.index.values

        # Join all authors into a single list and to each author assign corresponding article
        studies_authors = [dict(author, **{'study': article}) for list_articles, article in zip(articles, articles_index)
                                                              for author in list_articles]

        # Get only author and study index (ignore name and surname)
        studies_authors = pd.DataFrame(studies_authors)[['index', 'study']]

        studies_authors.columns = ['author_index', 'study_index']

        return studies_authors

    def central_bank_paper_label(self):

        # Get studies and authors data
        authors_institutions = self.get_author_institution()
        studies_authors = self.get_study_author()

        # Merge both data frames
        author = pd.merge(studies_authors, authors_institutions, right_on='author', left_on='author_index')
        author.drop('author_index', inplace=True, axis=1)

        # Aggregate authors shares
        author = author.groupby(['author', 'study_index']).sum()
        author = author.groupby(['study_index']).sum().reset_index()

        # Create list of central bank paper labels
        cb_labels = author.loc[author['central bank'] > 0, :]['study_index'].tolist()

        return cb_labels
