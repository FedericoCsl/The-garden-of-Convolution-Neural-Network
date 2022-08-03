# The-garden-of-Convolution-Neural-Network 

The general idea of this project was born thinking of my roots and my family. I was born and raised in Italy, in a house in the country side  with a large garden and my niece always came to visit me with my sister. My niece really likes flowers and she knows how to use the Ipad well, even though she is only six years old, so I decided to make an app that can recognize flower's species so that she can use it.

# Dataset and useful informations

On Kaggle, I found and downloaded the suitable dataset for this project, here the link: https://www.kaggle.com/code/rajmehra03/flower-recognition-cnn-keras/data

The dataset is made up of five folders, each with the name of a species of flower for a total of 3680 photos.
To simplify the process, I have manually divided the train and test set.
In train set I copied the overall photos, from which I extracted 20% of photos and transferred to test_set.
As last step, I created a folder in which I collected some photos of flowers that I found on the internet, which I then processed.

This was my first experience in computer vision and I found the explanations and cheat sheets on standford.edu really useful, here is the link: https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-convolutional-neural-networks

# Goal of the project

The goal of this project is to be able to create a system that can recognize up to five types of flower, including: Rose, Sunflower, Dandelion, Daisy and Tulip.

To make this possible, I combined my knowledge in convolutional neural network and image recognition and as last step I created a very simple app using Streamlit.

# Model development

To build the model I used Keras API which works very well with neural network models, specifically I chose the Sequential model.
A bit more complicated part is deciding what kind of layers to use, as they affect the final accuracy. In my case I have chosen some including for example Convolution2D and Max pooling operation.

I found the information on TensorFlow very useful, here the link: https://www.tensorflow.org/api_docs/python/tf/keras/layers

# Streamlit app

The last step was building a streamlit app.
The accuracy is not 100% but the app can recognize some flowers.
Here attached you will find the link: https://federicocsl-the-garden-of-convolution-neural-flowers-app-4zgxrx.streamlitapp.com/

