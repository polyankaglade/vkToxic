from tokenization import * # tokenize
from punctuation import * # del_punct
from lemmatization import * # lemmatize
from stopwords import * # del_stop_words, badwords
from emojis import * # del_emoji, replace_all_emoji, replace_emoji_by_class
from ner_preproc import * #delete_ner, replace_ner

def preprocess(text, params={'punctuation_deletion': 'no',
                             'lemmatization': 'no',
                             'stopwords_deletion': 'no', 
                             'emojis_processing': 'no', 
                            'preprocess_ner': 'no'}):
    
    if params['punctuation_deletion'] == 'no':
        pass 
    elif params['punctuation_deletion'] == 'yes':
        text = del_punct(text)
    else:
        raise ValueError('такой опции нет')
        
    
    if params['lemmatization'] == 'no':
        pass 
    elif params['lemmatization'] == 'yes':
        text = lemmatize(text)
    else:
        raise ValueError('такой опции нет')
        
    if params['stopwords_deletion'] == 'no':
        pass 
    elif params['stopwords_deletion'] == 'yes':
        text = del_stop_words(text, add_stop=badwords)
    else:
        raise ValueError('такой опции нет')
        
    
    if params['emojis_processing'] == 'no':
        pass 
    elif params['emojis_processing'] == 'del':
        text = del_emoji(text)
    elif params['emojis_processing'] == 'replace':
        text = replace_all_emoji(text)
    elif params['emojis_processing'] == 'label':
        text = replace_emoji_by_class(text)
    else:
        raise ValueError('такой опции нет')
    
    if params['preprocess_ner'] == 'no':
        pass 
    elif params['preprocess_ner'] == 'del':
        text = delete_ner(text)
    elif params['preprocess_ner'] == 'replace':
        text = replace_ner(text)
    else:
        raise ValueError('такой опции нет')
      
    return text
