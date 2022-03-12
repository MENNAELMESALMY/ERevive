from NlpUtilityFunctions import *
from TF_IDF import *
from SQLSUGG_ReadFiles import *
import pandas as pd
import re
import copy
import csv
#Store topics[topic].update({'attributes':headers,'attributes_files':files_names})

def get_topics_vocab(sql_topics,datafiles_path):
    topics_vocab = {}
    attributes_and_files = open('attributes_and_files.txt','w')
    for topic in sql_topics.keys():
        topic_path = datafiles_path+topic
        topic_files = os.listdir(topic_path)
        headers = []
        attributes_values=[]
        files_names=[]
        for filename in topic_files:
            header_clean=[]
            with open(topic_path+"/"+filename, 'r') as file:
                csvreader = pd.read_csv(file,on_bad_lines='skip',sep=',|;|[|]')
                csvreader.dropna(inplace=True)
                header_cols = list(csvreader.columns)
                for header in header_cols:
                    header_clean.append(header.replace('"',''))
                    attributes_values.append(csvreader[header].tolist())
                    files_names.append(filename)
                headers.extend(header_clean)
        topics_vocab[topic] = headers
        print('topic',topic)
        attributes_and_files.write('--topic--'+topic+'\n')
        attributes_and_files.write(str(headers)+'\n')
        attributes_and_files.write(str(files_names)+'\n')
    attributes_and_files.close()
    return topics_vocab

#Store topics[topic]['attributes_words'].append(attributes)
def clean_topics_vocab(topics_vocab):
    topics_vocab_clean = {}
    attributes_words = open('attributes_words.txt','w')
    for topic,vocab in topics_vocab.items():
        topics_vocab_clean[topic] = []
        #topics[topic]['attributes_words'] = []
        attributes_words.write('--topic--'+topic+'\n')
        for word in vocab:
            word = word.replace('"','')
            attributes = cleanAttribute(word)
            topics_vocab_clean[topic].extend(attributes)
            attributes_words.write(str(attributes)+'\n')
            #topics[topic]['attributes_words'].append(attributes)
    attributes_words.close()
    return topics_vocab_clean

#Store topics[topic].update({'attributes':headers,'attributes_files':files_names})

def get_topics_vocab(sql_topics,datafiles_path):
    topics_vocab = {}
    attributes_and_files = open('attributes_and_files.txt','w')
    for topic in sql_topics.keys():
        topic_path = datafiles_path+topic
        topic_files = os.listdir(topic_path)
        headers = []
        attributes_values=[]
        files_names=[]
        for filename in topic_files:
            header_clean=[]
            with open(topic_path+"/"+filename, 'r') as file:
                dialect = csv.Sniffer().sniff(file.readline())
                file.seek(0)
                csvreader = pd.read_csv(file,error_bad_lines=False,sep=dialect.delimiter)
                csvreader.dropna(inplace=True)
                header_cols = list(csvreader.columns)
                for header in header_cols:
                    header_clean.append(header.replace('"',''))
                    attributes_values.append(csvreader[header].tolist())
                    files_names.append(filename)
                headers.extend(header_clean)
        topics_vocab[topic] = headers
        print('topic',topic)
        attributes_and_files.write('--topic--'+topic+'\n')
        attributes_and_files.write(str(headers)+'\n')
        attributes_and_files.write(str(files_names)+'\n')
        
    attributes_and_files.close()
    return topics_vocab

#Store topics[topic]['attributes_words'].append(attributes)
def clean_topics_vocab(topics_vocab):
    topics_vocab_clean = {}
    attributes_words = open('attributes_words.txt','w')
    for topic,vocab in topics_vocab.items():
        topics_vocab_clean[topic] = []
        #topics[topic]['attributes_words'] = []
        attributes_words.write('--topic--'+topic+'\n')
        for word in vocab:
            word = word.replace('"','')
            attributes = cleanAttribute(word)
            topics_vocab_clean[topic].extend(attributes)
            attributes_words.write(str(attributes)+'\n')
            #topics[topic]['attributes_words'].append(attributes)
    attributes_words.close()
    return topics_vocab_clean

def get_corpus(topics_vocab):
    corpus = []
    for _,vocab in topics_vocab.items():
        corpus.append(vocab)
    return corpus

def format_TF_IDF(topics_tfidf,threshold):
    topics_tfidf_copy = copy.deepcopy(topics_tfidf)
    for topic_name,topic in topics_tfidf_copy.items():
        for word,val in topic.items():
            if val<=threshold : topics_tfidf[topic_name].pop(word)

def generateTopicsVocab(vocab,topics_names):
  corpus= get_corpus(vocab)  
  UniqueWords = getUniqueWords(corpus)
  idf_dict = IDF(corpus, UniqueWords)
  topics_tfidf = TF_IDF(corpus,topics_names,idf_dict)
  format_TF_IDF(topics_tfidf,0.0079)
  return topics_tfidf

# ######################################################################
# datafiles_path = './Test/'
# schemasfiles_path = './schemas/'
# sql_topics = get_sql_topics('TopicsTest.txt')
# topics_list = list(sql_topics.keys())
# print("sql_topics",topics_list)
# #######################################################################
# print("------------------------get vocab-----------------------------------")
# topics_vocab = get_topics_vocab(sql_topics,datafiles_path)
# print("-------------------------cleaning----------------------------------")
# topics_vocab = clean_topics_vocab(topics_vocab)
# print("-------------------------create corpus---------------------------------")
# corpus= get_corpus(topics_vocab)     
# print("-------------------------fit---------------------------------")
# Vocabulary, idf_of_vocabulary=fit(corpus) 
# print("-------------------------transform---------------------------------")
# TF_IDF_output = transform(corpus,Vocabulary,idf_of_vocabulary)
# print("-------------------------create dicts---------------------------------")
# Vocabulary_Inverse = {v: k for k, v in Vocabulary.items()}
# topics_tfidf = format_TF_IDF(TF_IDF_output,Vocabulary_Inverse)
# print("--------------------filtering-------------------------------------")
# filter_low_tfidf(topics_tfidf,0.00999,len(topics_list),topics_list)
# print("--------------------writing vocal-------------------------------------")
# #write vocab of each topic after TFIDF filtering
# topics_vocab_filtered = open('topics_vocab_filtered.txt','w')
# for index,topic in enumerate(topics_list):
#     topics_vocab_filtered.write("--topic--"+topic+'\n')
#     for topic_filtered_key,_ in topics_tfidf[index].items():
#         topics_vocab_filtered.write(topic_filtered_key+'\n')
#     print(topic,'done')
# topics_vocab_filtered.close()
# print("-----------------------------------------------------------")

