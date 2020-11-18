import nltk
import string

def tokenize_and_punct_del(file_text):
    # nltk tokenization
    tokens = nltk.word_tokenize(file_text)

    # delete punctuation symbols
    tokens = [i for i in tokens if ( i not in string.punctuation )]

    return " ".join( tokens )
