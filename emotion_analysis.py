import tensorflow as tf
import numpy as np
import pathlib

model_path = pathlib.Path(r"D:\DESKTOP\AI proj\project\models\emotion_cnn_model.h5") 
IMG_SIZE = (64,64)

EMOTIONS = {0: "happy",1: "neutral",2: "sad"}

load_model = tf.keras.models.load_model(str(model_path),compile=False)


def predict_emotion(img_path):

    img = tf.io.read_file(img_path)
    img = tf.image.decode_jpeg(img,channels=3)
    img = tf.image.resize(img,IMG_SIZE)
    img = tf.expand_dims(img,0) / 255.0 # example shape (1,64,64,3)

    probs = load_model.predict(img, verbose=0)[0] # e.g. [0.8,0.1,0.1]
    return EMOTIONS[int(np.argmax(probs))]