<img src="https://github.com/mateomartinez510/Springboard/blob/master/Household_Sounds_Capstone/images/cover_photo.png" alt="cover_poto" width="75%" height="75%"/>

# Classifying Household Sounds with Image Recognition Algorithms

In the last ten years that has been huge leaps forward in the field of computer vision, with algorithms gaining high level understanding of the digital images. 
For this project, we will apply these image classification algorithms to audio files by converting the raw audio into three feature sets: Mel-Frequency Spectrogram images,and Mel-Frequency Cepstral Coefficient images, and the mean Mel-Frequency Cepstral Coefficient values. The dataset we will investigate is comprised of a variety of typical household sounds. The goal of this project is to apply machine learning classification algorithms to our converted audio files to predict to the class label of typical household sounds.

## [The Data](https://zenodo.org/record/4060432#.X9lgPNNKgWo)

The dataset for this project is titled Freesound Dataset 50k and was curated by The Music Technology Group of Universitat Pompeu Fabra. It contains 50,000 raw audio wav files. The curators have pre-split the data set into a training set of 40,966 files and a test set of 10,231 files.The dataset contains a title, description, and tags but no class labels, which need to be wrangled. The audio files contain a wide array of sounds, from music, speech, animal,nature, city, and household sounds.

## [1. Wrangling Class Labels](https://github.com/mateomartinez510/Springboard/blob/master/Household_Sounds_Capstone/notebooks/01_Wrangling_Class_Labels.ipynb)

In the first notebook we will wrangle class labels for each of audio files. The dataset includes metadata that contains tags describing the audio events in each track. There are over 20,000 unique audio tags in this dataset, which requires initial step EDA on these audio tags as part of determinig class labels.

## [2. Data Wrangling and Feature Engineering](https://github.com/mateomartinez510/Springboard/blob/master/Household_Sounds_Capstone/notebooks/02_Wrangling_Spectrograms_MFCC_Features.ipynb)

In this notebook we will extract three sets of features: Mel-Frequency Spectrograms, MFCC Spectrograms, and mean MFCC values. Additionally, there is significant imbalanced classes in the training dataset. This will be addressed by random over sampling and random under sampling. For the audio files that are randomly oversampled, we will add data augmentation by adding gaussian noise and shifting the pitch of the audio.

## [3. Exploratory Data Analysis](https://github.com/mateomartinez510/Springboard/blob/master/Household_Sounds_Capstone/notebooks/03_EDA.ipynb)

In this notebook we will investigate in more depth the audio tags, class labels, and class imbalance in the train and test sets. We will analyze each of the three sets of features as well as the raw audio files.

## [4. Pre-Processing](https://github.com/mateomartinez510/Springboard/blob/master/Household_Sounds_Capstone/notebooks/04_Pre_Processing.ipynb)

In this notebook the Mean MFCC values will be scaled with a zero mean and unit variance. The test data for the neural networks will be split 50-50 into validation and test sets for neural network hyperparameter tuning. Images will be scaled in the modeling notebook with a Keras ImageDataGenerator to a min-max range of zero to one. 

## [5. Modeling](https://github.com/mateomartinez510/Springboard/blob/master/Household_Sounds_Capstone/notebooks/05_Modeling.ipynb)

In this notebook we will train a total of seven classification models using the three feature sets:
1a. Convolutional Neural Network with Mel-Frequency Spectrograms
2a. CNN with MFCC Spectrograms
2b. CNN with ResNet50 Transfer Learning with MFCC Spectrograms
3a. Neural Network with Mean MFCC Values
3b. Logistic Regression with Mean MFCC Values
3c. Random Forest with Mean MFCC Values
3d. Support Vector Classifier with Mean MFCC Values

## [6. Model Analysis](https://github.com/mateomartinez510/Springboard/blob/master/Household_Sounds_Capstone/notebooks/06_Model_Analysis.ipynb)

In this notebook we will review the model performance of the best model. The evaluation metric we are using is the F1-score, to place equal consideration on false postives and false negatives. We will review where the model's shortcomings as well as business implications and recommendations that can be derived from the best model and the models with interpretable model coefficients and feature importance.

