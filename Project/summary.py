import re
import nltk
import pandas as pd
import math
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def tokenize_text(text):
    article = sent_tokenize(text)
    sentences = []
    # removing special characters and extra whitespaces
    for sentence in article:
        sentence = re.sub('[\s+]', ' ', sentence)
        sentences.append(sentence)
    sentences.pop() 
    display = "".join(sentences)
    print('\n')
    return sentences

# counting the number of words in the document (sentence)
def cnt_words(sent):
    cnt = 0
    words = word_tokenize(sent)
    for word in words:
        cnt = cnt + 1
    return cnt
   
# getting data about each sentence (frequency of words) 
def cnt_in_sent(sentences):
    txt_data = []
    i = 0
    for sent in sentences:
        i = i + 1
        cnt = cnt_words(sent)
        temp = {'id' : i, 'word_cnt' : cnt}
        txt_data.append(temp)
    return txt_data

# creating a dictionary of words for each document (sentence)
def freq_dict(sentences):
    i = 0
    freq_list = []
    for sent in sentences:
        i = i + 1
        freq_dict = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            if word in freq_dict:
                freq_dict[word] = freq_dict[word] + 1
            else:
                freq_dict[word] = 1
            temp = {'id' : i, 'freq_dict' : freq_dict}
        freq_list.append(temp)
    return freq_list
   
# calculating the term frequency 
def calc_TF(text_data, freq_list):
    tf_scores = []
    for item in freq_list:
        ID = item['id']
        for k in item['freq_dict']:
            temp = {
                'id': item['id'],
                'tf_score': item['freq_dict'][k]/text_data[ID-1]['word_cnt'],
                'key': k
                }
            tf_scores.append(temp)
    return tf_scores
    
#calculating the inverse document frequency
def calc_IDF(text_data, freq_list):
    idf_scores =[]
    cnt = 0
    for item in freq_list:
        cnt = cnt + 1
        for k in item['freq_dict']:
            val = sum([k in it['freq_dict'] for it in freq_list])
            temp = {
                'id': cnt, 
                'idf_score': math.log(len(text_data)/(val+1)), 
                'key': k}
            idf_scores.append(temp)
    return idf_scores

# calculating TFIDF value
def calc_TFIDF(tf_scores, idf_scores):
    tfidf_scores = []
    for j in idf_scores:
        for i in tf_scores:
            if j['key'] == i['key'] and j['id'] == i['id']:
                temp = {
                    'id': j['id'],
                    'tfidf_score': j['idf_score'] * i['tf_score'],
                    'key': j['key']
                    }
                tfidf_scores.append(temp)
    return tfidf_scores

# giving each sentence a score
def sent_scores(tfidf_scores, sentences, text_data):
    sent_data = []
    for txt in text_data:
        score = 0
        for i in range(0, len(tfidf_scores)):
            t_dict = tfidf_scores[i]
            if txt['id'] == t_dict['id']:
                score = score + t_dict['tfidf_score']
        temp = {
            'id': txt['id'],
            'score': score,
            'sentence': sentences[txt['id']-1]}
        sent_data.append(temp)
    return sent_data

# creating the summary
def summary(sent_data):
    cnt = 0
    summary = []
    for t_dict in sent_data:
        cnt  = cnt + t_dict['score']
    avg = cnt / len(sent_data)
    for sent in sent_data:
        if sent['score'] >= (avg):
            summary.append(sent['sentence'])
    summary = " ".join(summary)
    return summary

def create_summary():
    data = pd.read_csv('data.csv')
    data["summary"] = None
    for i in range(len(data)):
        sentences =  tokenize_text(data["workExp"][i])
        text_data = cnt_in_sent(sentences)
        freq_list = freq_dict(sentences)
        tf_scores = calc_TF(text_data, freq_list)
        idf_scores = calc_IDF(text_data, freq_list)
        tfidf_scores = calc_TFIDF(tf_scores, idf_scores)
        sent_data = sent_scores(tfidf_scores, sentences, text_data)
        data.summary[i] =  summary(sent_data)
    data.to_csv('./summary_data.csv', index=False)
    print("CVS file is created")

def keywords():
    data = pd.read_csv('summary_data.csv')
    top_n = 5
    model = SentenceTransformer('distilbert-base-nli-mean-tokens')
    data["keywords"] = None
    n_gram_range = (1, 1)
    stop_words = "english"
    for i in range(len(data)):
        doc = data.workExp[i]
        count = CountVectorizer(ngram_range=n_gram_range, stop_words=stop_words).fit([doc])
        candidates = count.get_feature_names()
        doc_embedding = model.encode([doc])
        candidate_embeddings = model.encode(candidates)
        distances = cosine_similarity(doc_embedding,candidate_embeddings)
        keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
        data["keywords"][i] = ','.join(keywords)
    data.to_csv('./summary_data.csv', index=False)
    data.to_csv('./static/summary_data.csv', index=False)
    print("CVS file is created")
