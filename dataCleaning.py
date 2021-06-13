from nltk import data
import pandas as pd 
import numpy as np
import datetime
import csv
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize, RegexpTokenizer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import re

dataframe = pd.read_csv('data.csv')

def remove_punctuation(text):
    no_punct = "".join([c for c in text if c not in  string.punctuation])
    return no_punct

tokenizer = RegexpTokenizer(r'\w+')
def text_cleaner(text):
    rules = [
        {r'>\s+': u'>'},  # remove spaces after a tag opens or closes
        {r'\s+': u' '},  # replace consecutive spaces
        {r'\s*<br\s*/?>\s*': u'\n'},  # newline after a <br>
        {r'</(div)\s*>\s*': u'\n'},  # newline after </p> and </div> and <h1/>...
        {r'</(p|h\d)\s*>\s*': u'\n\n'},  # newline after </p> and </div> and <h1/>...
        {r'<head>.*<\s*(/head|body)[^>]*>': u''},  # remove <head> to </head>
        {r'<a\s+href="([^"]+)"[^>]*>.*</a>': r'\1'},  # show links instead of texts
        {r'[ \t]*<[^<]*?/?>': u''},  # remove remaining tags
        {r'^\s+': u''}  # remove spaces at the beginning
    ]
    for rule in rules:
        for (k, v) in rule.items():
            regex = re.compile(k)
            text = regex.sub(v, text)
        text = text.rstrip()
    return text

lemmatizer = WordNetLemmatizer()
def word_lemmatizer(text):
    lem_text = " ".join([lemmatizer.lemmatize(i) for i in text])
    return lem_text

def process_data():
    dataframe['processed_text'] = None
    tokenizer = RegexpTokenizer(r'\w+')
    dataframe.processed_workExp = dataframe.workExp.apply(lambda x: text_cleaner(x))
    dataframe.processed_workExp = dataframe.processed_workExp.apply(lambda x: remove_punctuation(x), 1)
    dataframe.processed_workExp = dataframe.processed_workExp.apply(lambda x: tokenizer.tokenize(x.lower()))
    dataframe.processed_workExp = dataframe.processed_workExp.apply(lambda x: word_lemmatizer(x))
    # Convert into a single CSV file.
    dataframe.to_csv('./clean_data.csv', index=False)
    print("CVS file is created")