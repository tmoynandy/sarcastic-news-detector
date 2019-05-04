from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

def process(headline):
    max_fatures = 2000
    tokenizer = Tokenizer(num_words=max_fatures, split=' ')
    headline = tokenizer.texts_to_sequences(headline)
    headline = pad_sequences(headline, maxlen=29, dtype='int32', value=0)
    return headline