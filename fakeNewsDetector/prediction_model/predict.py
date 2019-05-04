from keras.models import load_model
import numpy as np
import tensorflow as tf

loaded_model = None
graph = None


def prediction(headline):
    global loaded_model, graph
    graph = tf.get_default_graph()
    str = ''
    model = load_model('/home/tanu/Desktop/django_ai/fakeNewsDetector/prediction_model/sarcasm_detection.h5')
    sentiment = model.predict(headline,batch_size=1,verbose = 2)[0]
    if(np.argmax(sentiment) == 0):
        str = 'Non-Sarcastic'
        print("Non-sarcastic")
        return(str)
    elif (np.argmax(sentiment) == 1):
        str = 'Sarcasm'
        print("Sarcasm")
        return(str)