"""
Analysis helper functions

Author: Wiktor
Created on: Sun 16 Sep 2018 18:52:59 CEST
"""

import pandas as pd
import os


def read_txt_studies(studies_location):
    """
    Reads all of the .txt files from given location

    Returns:
    - pd.DataFrame of all texts and their labels
    """

    # Get .txt files from the directory
    study_files = [file for file in os.listdir(studies_location) if '.txt' in file]

    # Remove extensions
    study_labels = [x.split('.')[0] for x in study_files]

    # Create file paths from files and their location
    study_paths = [studies_location + x for x in study_files]

    studies = []
    for text in study_paths:

        with open(text, 'r') as file:
            studies.append(file.read().replace('\n', ' '))

    df_studies = pd.DataFrame()
    df_studies['document'] = studies
    df_studies['label'] = study_labels
    return df_studies


def convert_list(content):
    """
    Function transforms list of vectorized documents into list of strings (one per document)

    Arguments:
    - list of vectorized texts (list of lists)
    """
    # Empty list of to collect strings
    converted_content = []
    for index, str_list in enumerate(content):
        converted_content.append('')
        for item in str_list:
            converted_content[index] = converted_content[index] + ' ' + item
    return converted_content
