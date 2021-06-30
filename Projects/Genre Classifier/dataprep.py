# from dataprep import extract_features_song
import numpy as np
import librosa 
import librosa.feature
import librosa.display
import glob 
# import matplotlib.pyplot as plt
# import torch
# import torchvision
# from torch.utils.data import Dataset, DataLoader, dataloader, sampler



def extract_features_song(self,f):
    y,_ = librosa.load(f)
    mfcc = librosa.feature.mfcc(y)
    mfcc /= np.amax(np.absolute(mfcc))

    return np.ndarray.flatten(mfcc)[:25000]

#     def generate_features_and_labels(self,root_path):
#         self.all_features = []
#         self.all_labels = []

#         genres = ["blues", "classical", "country", "disco", "hiphop","jazz","metal","pop","reggae","rock"]
#         for genre in genres:
#             sound_files = glob.glob(root_path + genre + "/*.wav")
#             print("Processing %d songs in %s genre..." % (len(sound_files), genres))
#             for f in sound_files:
#                 features = extract_features_song(f)
#                 self.all_features.append(features)
#                 self.all_labels.append(genre)

#     def data_splitter(self,features,labels):
#         training_split = 0.8
#         alldata = np.column_stack((features,labels))

#         np.random.shuffle(alldata)
#         # splitidx

# rdir = "sampleFolder/genres/"

# dataset = AudioDataset(root_path = rdir)
# dataloader = DataLoader(dataset,32,True)
# samples = iter(dataloader)
# features,labels = samples.next()

