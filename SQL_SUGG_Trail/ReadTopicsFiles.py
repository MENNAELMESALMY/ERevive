
from GenerateTopicsClasses import *
import ast


def read_topics_vocab_filtered(filename,topics):
    topics_vocab_filtered = open(filename,'r')
    Lines = topics_vocab_filtered.readlines()
    for l in Lines:
        if l.find('--topic--') != -1:
            topic = l[9:-1]
            topics[topic]['vocab'] = []
            continue
        topics[topic]['vocab'].append(l[:-1])
    topics_vocab_filtered.close()

def read_attributes_words(filename,topics):
    attributes_words = open(filename,'r')
    Lines = attributes_words.readlines()
    for l in Lines:
        if l.find('--topic--') != -1:
            topic = l[9:-1]
            topics[topic]['attributes_words'] = []
            continue
        l_list = ast.literal_eval(l)
        topics[topic]['attributes_words'].append(l_list)
    attributes_words.close()

def read_attributes_and_files(filename,topics):
    attributes_and_files = open(filename,'r')
    Lines = attributes_and_files.readlines()
    line_data = 0
    for l in Lines:
        if l.find('--topic--') != -1:
            topic = l[9:-1]
            line_data = 1
            continue
        l_list = ast.literal_eval(l)
        if line_data == 1: 
            field = 'attributes' 
            line_data = 2
        else: 
            field = 'attributes_files'
        topics[topic][field] = l_list
    print(topics)
    attributes_and_files.close()

# sql_topics = get_sql_topics('TopicsTest.txt')
# topics_list = list(sql_topics.keys())
# topics = {'Entertainment':{},'Financial':{}}
# topics_vocab = read_topics_vocab_filtered('topics_vocab_filtered.txt',topics_list)
# read_attributes_and_files('attributes_and_files.txt',topics)
# print(topics)
# read_attributes_words('attributes_words.txt',topics)

