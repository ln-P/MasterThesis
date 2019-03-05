# Code Overview

The Project is divided into two main directories:

1. **Analysis** directory with all files that were created to analyse text
    - **Python (helper) files**
        - `analysis_helper_functions.py`: useful functions used in text analysis
        - `clean_txt.py`: funcions used to transform raw text strings into NLP analysis ready format
        - `pdf_to_txt.py`: function that loads all PDF files in location and combined them into collection of strings
        - `read_json.py`: functions to extract information from the author/studies .json files
        - `read_pdf.py`: function allows to transform .PDF file it into a string
    - **Jupyter Notebooks**
        - `Cleaning Wikipedia data.ipynb`: notebook that transforms wikipedia data into  NLP analysis ready format
        - `EDA.ipynb`
        - `Hedging.ipynb`: notebook used for hedging analysis and classification
        - `NPL_Analysis_all_texts.ipynb`: notebook that preforms topic clustering and modelling.
        - `Statistics_Analysis.ipynb`: notebook that analyses the reported statistics.
    - **Wikipedia Data**
        - `wiki_data.txt`: raw wikipedia data
        - `wiki_data_clean.csv`: cleaned wiki data
    - **Words Lists**
        - `hedge_words.txt`: list of hedge words
        - `hypothesis_testing_words.txt`: list of words related to the statistic

2. **Literature** directory with files related to the collected literature and its content
    - **References**: folder with all bibliography used in the thesis
    - **Competition_Studies_Database**: folder with all PDF files and .txt files of the Competition papers. Includes also authors.json and studies.json: files about collected articles and their authors
    - **Statistics**: raw collected statistics data
