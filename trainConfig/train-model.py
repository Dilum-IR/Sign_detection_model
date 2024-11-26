from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard
import cv2
import numpy as np
import os

from Utils import FILE_PATH_NAME, Actions, no_sequences, sequence_length, start_folder

# Preprocess Data and Create Labels and Features

label_map = {label:num for num, label in enumerate(Actions)}
# label_map result {'hello': 0, 'thanks': 1, 'i love you': 2, ...}

sequences, labels = [], []
for action in Actions:
    for sequence in range(no_sequences):
        window = []
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(FILE_PATH_NAME, action, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
        sequences.append(window)
        labels.append(label_map[action])

print(np.array(sequences).shape)
print(np.array(labels).shape)

X = np.array(sequences)
print("X: "+X)
y = to_categorical(labels).astype(int)
print("y: "+y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)
print(X_train.shape)


# Build and Train LSTM Nural Network

# monitor the training model accuracy and in-details
log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)

model = Sequential()
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30,1662)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
# model.add(LSTM(256, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu')) # return false beacuse next layer is Dense layer
model.add(Dense(64, activation='relu')) # fully connected layer
model.add(Dense(32, activation='relu'))
model.add(Dense(Actions.shape[0], activation='softmax')) # final layer have final set of outputs (Actions.shape[0])

print("Actions Shape: "+Actions.shape[0])
print("X Shape: "+X.shape)

# example how to work it
res = [0.7,.02,0.1] # this results are given for each final layer actions. more posibility 0.7 then output pass for it.
np_res = np.argmax(res)
print(Actions[np_res])

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.fit(X_train, y_train, epochs=1000, callbacks=[tb_callback])

model.summary()

# make Predicitons
res = model.predict(X_test)
Actions[np.argmax(res[1])]

Actions[np.argmax(y_test[1])]
Actions[(y_test[4])]