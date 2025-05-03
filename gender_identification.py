import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

def predict_gender(img_path):
    MODEL_PATH = r"D:\DESKTOP\AI proj\project\models\finalgender_savedmodel5"
    # IMAGE_DIR  = r'D:\DESKTOP\AI proj\project\data'

    model=load_model(MODEL_PATH)

    img=image.load_img(img_path, target_size=(100, 100))
    img_array = image.img_to_array(img)
    img_array=np.expand_dims(img_array, axis=0)
    img_array/=255.0

    prediction = model.predict(img_array,verbose=0)
    if prediction[0][0]>0.5:
        return "Male"
    else:
        return "Female"
