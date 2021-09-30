from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import cv2
import os
from sklearn import svm
import random
from skimage.morphology import skeletonize
from sklearn.model_selection import train_test_split
import pickle

target_img_size = (32, 32)

# def extract_hog_features(img):
#     img = cv2.resize(img, target_img_size)
#     win_size = (32, 32)
#     cell_size = (4, 4)
#     block_size_in_cells = (2, 2)

#     block_size = (block_size_in_cells[1] * cell_size[1], block_size_in_cells[0] * cell_size[0])
#     block_stride = (cell_size[1], cell_size[0])
#     nbins = 9  # Number of orientation bins
#     hog = cv2.HOGDescriptor(win_size, block_size, block_stride, cell_size, nbins)
#     h = hog.compute(img)
#     h = h.flatten()
#     return h.flatten()

# def extract_features(img):
#     return extract_hog_features(img)

def extract_features(img):
    sift = cv2.SIFT_create()
    kp, des = sift.detectAndCompute(img,None)
    if des is None:
        des = np.zeros((1,128),dtype=np.float32)
    max_size = 9216
    if des.shape[0] * des.shape[1] < max_size:
        temp_arr = np.zeros((max_size-(des.shape[0]*des.shape[1])))
        des = des.flatten()
        des = np.concatenate((des,temp_arr),axis=0)
    
    des = des.flatten()
    arr = np.zeros((1,des.shape[0]))
    arr[0,:] = des
    return list(np.array(arr,dtype=np.float32))

# def load_dataset(path_to_dataset):
#     features = []
#     labels = []
#     img_filenames = os.listdir(path_to_dataset)
#     for i, fn in enumerate(img_filenames):
#         if fn.split('.')[-1] != 'png':
#             continue

#         label = fn.split('_')[1]
#         labels.append(label)

#         path = os.path.join(path_to_dataset, fn)
#         img = cv2.imread(path, 0)
#         features.append(extract_features(img))

#         # show an update every 1,000 images
#         if i > 0 and i % 1000 == 0:
#             print("[INFO] processed {}/{}".format(i, len(img_filenames)))

#     return features, labels

def load_dataset(path_to_dataset):
    features = []
    labels = []
    img_filenames = os.listdir(path_to_dataset)
    for i, fn in enumerate(img_filenames):
        if fn.split('.')[-1] != 'png':
            continue

        label = fn.split('_')[1]
        labels.append(label)

        path = os.path.join(path_to_dataset, fn)
        img = cv2.imread(path,0)
        img = cv2.resize(img, target_img_size)
        features.append(extract_features(img)[0])

        # show an update every 1,000 images
        if i > 0 and i % 1000 == 0:
            print("[INFO] processed {}/{}".format(i, len(img_filenames)))

    return features, labels

def run_experiment(path_to_dataset,classifiers,random_seed):
    # Load dataset with extracted features
    print('Loading dataset. This will take time ...')
    features, labels = load_dataset(path_to_dataset)
    print('Finished loading dataset.')

    train_features, test_features, train_labels, test_labels = train_test_split(
        features, labels, test_size=0.2, random_state=random_seed)

 
    for model_name, model in classifiers.items():
        print('############## Training', model_name, "##############")
        # Train the model only on the training features
        model.fit(train_features, train_labels)

        # Test the model on images it hasn't seen before
        accuracy = model.score(test_features, test_labels)

        print(model_name, 'accuracy:', accuracy * 100, '%')


# def extractDigitsFeatures(img):
#     sift = cv2.SIFT_create()
#     keys, descriptors = sift.detectAndCompute(img,None)
#     if descriptors is None:
#         descriptors = np.zeros((1,128),dtype=float)
#     return descriptors.shape[1] * descriptors.shape[0]
        
def extractDigitsFeatures(img):
    return extract_features(img)

# def testMax(path_to_dataset):
#     features = []
#     labels = []
#     maxSize = 0
#     img_filenames = os.listdir(path_to_dataset)
#     for i, fn in enumerate(img_filenames):
#         if fn.split('.')[-1] != 'png':
#             continue

#         label = fn.split('_')[1]
#         labels.append(label)

#         path = os.path.join(path_to_dataset, fn)
#         img = cv2.imread(path,0)
#         v = extractDigitsFeatures(img)
#         if v > maxSize:
#             maxSize = v

#         if i > 0 and i % 1000 == 0:
#             print("[INFO] processed {}/{}".format(i, len(img_filenames)))
#     print(maxSize)

def digitsClassifier(test_img_path,features):
    path_to_dataset = r"/home/nihal/Documents/GP/newData"
    random_seed = 42
    random.seed(random_seed)
    np.random.seed(random_seed)
    classifiers = {
        # 'KNN': KNeighborsClassifier(n_neighbors=5),
        'SVM': svm.LinearSVC(random_state=random_seed),
    }
    run_experiment(path_to_dataset,classifiers,random_seed)

    nn = classifiers['SVM']
    #print(nn.predict_proba([features]))
    print(nn.predict(features))

    filename = '/home/nihal/Documents/GP/ocr_trainedModel.sav'
    pickle.dump(nn, open(filename, 'wb'))


#loaded_ocr_trainedModel = pickle.load(open('/home/nihal/Documents/GP/ocr_trainedModel.sav', 'rb'))
test_img_path = r"/home/nihal/Documents/GP/character0.png"
img = cv2.imread(test_img_path,0)
img = cv2.resize(img, target_img_size)
features = extractDigitsFeatures(img)
digitsClassifier(test_img_path, features)


# result = loaded_ocr_trainedModel.predict([features])
# print(result)

# testMax(r"/home/nihal/Documents/GP/newData")
