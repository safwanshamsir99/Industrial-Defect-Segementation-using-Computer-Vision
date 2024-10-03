from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import tensorflow as tf
from pathlib import Path

IMG_SIZE = (256, 256)
MODEL_PATH = Path() / "models" / "classifier-resnet-nut.h5"
def loading_model():
    loaded_model = load_model(
        MODEL_PATH
    )
    return loaded_model


def get_image(pth, img_size=IMG_SIZE):
    img = load_img(pth, target_size=img_size)
    img = img_to_array(img) / 255.0
    return img

def classify(path:str)->str:
    model = loading_model()
    img = get_image(path, img_size=IMG_SIZE)
    my_image = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    y_pred = model.predict(my_image)
    y_true = np.argmax(y_pred, axis=1)
    if y_true == 0:
        output = "No defect, Perfecto!"
    else:
        output = "Warning, you have defect!"
    return output
