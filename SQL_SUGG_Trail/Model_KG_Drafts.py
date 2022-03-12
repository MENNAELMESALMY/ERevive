word2vec_sample = api.load("word2vec-google-news-300", return_path=True)
model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=True)
file_to_store = open('/content/drive/MyDrive/DataSets_GP/Model.pickle', "wb")
pickle.dump(model, file_to_store)

file_to_load= open('/content/drive/MyDrive/DataSets_GP/subjects.pickle', "rb")
kg_subjects = pickle.load(file_to_load)