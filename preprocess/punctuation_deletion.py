import string

def punct_del(file_text):
    tokens = file_text.split()

    # delete punctuation symbols
    tokens = [i for i in tokens if ( i not in string.punctuation )]

    return " ".join( tokens )
