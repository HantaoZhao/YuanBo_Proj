# from sklearn import preprocessing
# import numpy

# Standardize data (0 mean, 1 stdev)
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

from keras.models import Sequential
from keras.utils import np_utils
from keras.layers import Dense, Dropout, GaussianNoise, Conv1D
from keras.preprocessing.image import ImageDataGenerator

import matplotlib.pyplot as plt

f=pd.read_csv("E://JI//Temp//data//data108.csv")
array = f.values
# separate array into input and output components
# size:200000 (can be adjusted)
X = array[:200000]

# Normalization
scaler = StandardScaler().fit(X)
scaledX = scaler.transform(X)


# PCA and plotting
# Just for illustration
pca = PCA(n_components=108)
pca.fit(scaledX)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance')
plt.show()
#

#
# Conclusion:
# 37features: 90% accu
# 47features: 95% accu
# 68features: 99% accu
#

# Set NCOMPONENTS to 37, supposedly 90% of variance should be enough 
NCOMPONENTS = 37

pca = PCA(n_components=NCOMPONENTS,copy=False)
X_pca_train = pca.fit_transform(scaledX)

print(X_pca_train.shape)

# Saving the Results
# np.savetxt("data200000_accu90.csv", X_pca_train, delimiter=",")
pd.DataFrame(X_pca_train).to_csv("E://JI//Temp//data//data200000_accu90.csv")