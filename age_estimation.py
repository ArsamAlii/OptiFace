import tensorflow as tf
import numpy as np
import pathlib

modelpath=pathlib.Path(r"D:\DESKTOP\AI proj\project\models\age_classifier_imfdb.h5")
img_sz=(64,64)
LABELS={0:"YOUNG (age<18)",1:"Adult (18-45) ",2:"OLD(age>45)"}

model_age=tf.keras.models.load_model(str(modelpath),compile=False)

def predict_age_group(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_jpeg(img,channels=3)
    img = tf.image.resize(img,img_sz)
    img = tf.expand_dims(img, 0)/255.0 # shape(1, 64, 64, 3) array shape is made here with such dimentions

    probs = model_age.predict(img, verbose=0)[0]# e.g.[0.1,0.7,0.2] the threshold is between 0-1 (normalised)
    return LABELS[int(np.argmax(probs))]

