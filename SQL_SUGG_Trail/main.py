import os
import csv
import pandas as pd
import math
import numpy as np 
import re
import nltk
#import gensim.downloader as api
from nltk.data import find
#import gensim
from nltk.stem import WordNetLemmatizer
import spacy
from SchemaGraph import *
from DataGraph import *
from GenerateTopicsClasses import *
from NlpUtilityFunctions import *
from TF_IDF import *
from ClassifySchema import *
from SQLSUGG_ReadFiles import *
from SQLSUGG_Probabilties import *
from SQLSUGG_GenerateTemplates import *
from SQLSUGG_pipeline import * 
from ReadTopicsFiles import *


nlp = spacy.load('en_core_web_sm')
inputSchemaFolderPath = './TestSchema/'
##################

topics_names = get_topics_names('TopicsDataBases.txt')
topics = {topic:{} for topic in topics_names }
read_attributes_and_files('attributes_and_files.txt',topics)
read_topics_vocab_filtered('topics_vocab_filtered.txt',topics)
read_attributes_words('attributes_words.txt',topics)

inputSchemaFilesPaths = [ inputSchemaFolderPath+f for f in os.listdir(inputSchemaFolderPath)]
schema_input_graph,schemaTopic,topic = inputSchema(inputSchemaFilesPaths,topics)

print("Schema Topic:",schemaTopic)
# print(topics['Sports'])

