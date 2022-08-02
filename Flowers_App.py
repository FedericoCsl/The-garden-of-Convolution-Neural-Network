import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from PIL import Image



st.title("The garden of Convolutional Neural Network")

st.write("A simple app that can recognize up to five flower's species: Daisy, Dandelion, Rose, Sunflower and Tulip")

st.write("App created by Federico Casula as part of the final project for WBS coding school")



# Prediction
def predict_class(image):
    classify_model = tf.keras.models.load_model('cnn.h5')
    
# Display Image    
    img_t = image.resize((64,64))
    img_t = tf.keras.preprocessing.image.img_to_array(img_t)
    img_t = np.expand_dims(img_t, axis=0)
    img_t /= 255.
    
    prediction = classify_model.predict(img_t)
    flower_species = ["Daisy", "Dandelion", "Rose", "Sunflower", "Tulip"]
    
    
    pred = flower_species[np.argmax(prediction)]
    all_preds = prediction[0]
    predicted_class = f"Type of flower   {pred}"
    
    
    return predicted_class, all_preds


#Display the bar
file_upl = st.file_uploader("Upload the image here", type=['png','jpeg','jpg'])
if file_upl is not None:
    image = Image.open(file_upl)
    
    
    figure = plt.figure()
    plt.imshow(image)
    plt.axis('off')
    result, all_preds = predict_class(image)
    st.write(result)
    st.pyplot(figure) 


