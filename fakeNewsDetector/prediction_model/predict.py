import numpy as np
#for importing our keras model
import keras.models
#for regular expressions, saves time dealing with string data
import re

#system level operations (like loading files)
import sys 
#for reading operating system data
import os
from keras.models import model_from_json
import tensorflow as tf
from keras import backend as K
global model, graph


def prediction(headline):
    json_file = open('/home/tanu/Desktop/django_ai/fakeNewsDetector/prediction_model/model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    #load woeights into new model
    loaded_model.load_weights("/home/tanu/Desktop/django_ai/fakeNewsDetector/prediction_model/model.h5")
    print("Loaded Model from disk")

    #compile and evaluate loaded model
    loaded_model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    #loss,accuracy = model.evaluate(X_test,y_test)
    #print('loss:', loss)
    #print('accuracy:', accuracy)
    graph = tf.get_default_graph()

    model = loaded_model
    # global loaded_model, graph
    # graph = tf.get_default_graph()
    str = ''
    # model = load_model('/home/tanu/Desktop/django_ai/fakeNewsDetector/prediction_model/sarcasm_detection.h5')
    # sentiment = model.predict(headline,batch_size=1,verbose = 2)[0]

    with graph.as_default():
        sentiment = model.predict(headline, batch_size=1, verbose =2)[0]
        if(np.argmax(sentiment) == 0):
            str = 'Non-Sarcastic'
            print("Non-sarcastic")
            return(str)
        elif (np.argmax(sentiment) == 1):
            str = 'Sarcasm'
            print("Sarcasm")
            return(str)
        K.clear_session()

