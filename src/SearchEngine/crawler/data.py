from abc import ABCMeta, abstractmethod
import pickle
import json
import os

class DatasetInterface(metaclass=ABCMeta):
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = []
        self.preprocess()
    
    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def preprocess(self):
        pass

class CoSqlDataset(DatasetInterface):
 
    def read_data(self):
        data_files = [self.data_path + '/' + f for f in os.listdir(self.data_path) if f.endswith('.json')]
        for data_file in data_files:
            with open(data_file) as f:
                data_object = json.load(f)
                queries = [data['query'] for data in data_object]
                self.data.extend(queries)

    def preprocess(self):
        self.read_data()
        #start with self.data

class SedeDataset(DatasetInterface):
 
    def read_data(self):
        data_files = [self.data_path + '/' + f for f in os.listdir(self.data_path) if f.endswith('.jsonl')]
        for data_file in data_files:
            with open(data_file) as f:
                file_lines = f.readlines()
                for line in file_lines:
                    data_object = json.loads(line)
                    self.data.append(data_object['QueryBody'])

    def preprocess(self):
        self.read_data()
        #start with self.data


class SparcDataset(DatasetInterface):
 
    def read_data(self):
        data_files = [self.data_path + '/' + f for f in os.listdir(self.data_path) if f.endswith('.json')]
        for data_file in data_files:
            with open(data_file) as f:
                data_object = json.load(f)
                interactions = [data['interaction'] for data in data_object]
                for interaction  in interactions:
                    for query in interaction:
                        self.data.append(query['query'])

    def preprocess(self):
        self.read_data()
        #start with self.data

class SplashDataset(DatasetInterface):
 
    def read_data(self):
        data_files = [self.data_path + '/' + f for f in os.listdir(self.data_path) if f.endswith('.json')]
        for data_file in data_files:
            with open(data_file) as f:
                data_object = json.load(f)
                queries = [data['gold_parse'] for data in data_object]
                self.data.extend(queries)

    def preprocess(self):
        self.read_data()
        #start with self.data

class NVBenchDataset(DatasetInterface):
 
    def read_data(self):
        with open(self.data_path) as f:
            data_object = json.load(f)
            queries = [data['vis_query']['data_part']['sql_part'] for data in data_object.values()]
            self.data.extend(queries)

    def preprocess(self):
        self.read_data()
        #start with self.data

class TopicsDataset(DatasetInterface):
 
    def read_data(self):
        data_files = [self.data_path + '/' + f for f in os.listdir(self.data_path) if f.endswith('.json')]
        for data_file in data_files:
            with open(data_file) as f:
                data_object = json.load(f)
                queries = [data['sql'] for data in data_object]
                for q in queries:
                    self.data.extend(q)

    def preprocess(self):
        self.read_data()
        #start with self.data

def main():
    base_path="/home/nada/GP/search engine/datasets/new/"
    data_sets = [CoSqlDataset(base_path+'cosql_dataset/cosql_dataset/system_response_generation'), SedeDataset(base_path+"sede-main/data/sede"), SparcDataset(base_path+"sparc/sparc"), SplashDataset(base_path+"Splash-master/data"), NVBenchDataset(base_path+"nvBench.json"), TopicsDataset(base_path+"topics")]
    outFile = open("data.pickle", "wb")
    queries=[]
    for data_set in data_sets:
        queries.extend(data_set.data)
    pickle.dump(queries, outFile)
    
def load_data():
    
    inFile = open("data.pickle", "rb")
    queries=pickle.load(inFile)
    return queries
load_data()

def call_after_load_data():
    pass