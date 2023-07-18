import tensorflow as tf
import os
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

# Creating dataframe from csv 
df = pd.read_csv('dataSets.csv')

# Dropping the 'Number' column
df = df.drop('Number', axis=1)

# Creating features from the words
df['word_length'] = df['Word'].apply(lambda x: len(x))
df['unique_chars'] = df['Word'].apply(lambda x: len(set(x)))

# Normalizing the features
df['word_length'] = df['word_length'] / df['word_length'].max()
df['unique_chars'] = df['unique_chars'] / df['unique_chars'].max()

X = df[['word_length', 'unique_chars']].values
y = df['Rating'].values

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Defining the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')
])

# Compiling the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Create a callback and save the model's weights
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path, save_weights_only=True, verbose=1)

# Training the model
model.fit(X_train, y_train, epochs=50, batch_size=32, callbacks=[cp_callback])

# Evaluating the model
loss = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}')

os.listdir(checkpoint_dir)
