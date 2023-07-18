import tensorflow as tf
import numpy as np
import pandas as pd
from queue import PriorityQueue

def Predictions(WordList: str):

    checkpoint_path = "training_1/cp.ckpt"

    # Calculate word length and character ratio for all words
    df = pd.read_csv('dataSets.csv')
    df['word_length'] = df['Word'].apply(lambda x: len(x))/df['Word'].apply(lambda x: len(x)).max()
    df['unique_chars'] = df['Word'].apply(lambda x: len(set(x)))/df['Word'].apply(lambda x: len(set(x))).max()

    # Defines the model's neural network
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(10, activation='relu', input_shape=(2,)),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1, activation='linear')
    ])

    # Load weights of saved model
    model.load_weights(checkpoint_path)

    # Priority queue to sort elements based on predicted complexity
    PQ = PriorityQueue()

    # Make predictions for each word and insert into priority queue to organize it
    for word in WordList:
        new_word = word
        new_word_features = np.array([[len(new_word)/df['word_length'].max(), len(set(new_word))/df['unique_chars'].max()]])
        predicted_complexity = model.predict(new_word_features)
        PQ.put((-1*predicted_complexity[0][0], new_word))
        print(f'Predicted Complexity for {new_word}: {predicted_complexity[0][0]}')
    
    # Appends into array to prepare for returning the most complex words
    RatingsWordList = []
    for i in range(0, 100):
        RatingsWordList.append(PQ.get())
    
    return RatingsWordList

    