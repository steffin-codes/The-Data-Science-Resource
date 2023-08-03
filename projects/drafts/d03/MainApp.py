import numpy as np
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential, load_model
from keras.layers import Embedding, LSTM, Dense
import joblib

def loadPreBuiltModel():
    model_path = 'projects/p02/100epoch_next_word_predictor_model.h5'
    model = load_model(model_path)
    return model

def App():
    # loadDataAndBuildModel()
    model = loadPreBuiltModel()
    
    return