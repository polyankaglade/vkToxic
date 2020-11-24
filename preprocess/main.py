import json

from punctuation import * # del_punct
from lemmatization import * # lemmatize
from stopwords import * # del_stop_words, badwords
from emojis import * # del_emoji, replace_all_emoji, replace_emoji_by_class
from ner_preproc import * #delete_ner, replace_ner
from vulgars import * # replace_vulgar

best_params = {'punctuation_deletion': 'no',
               'ner_processing': 'replace',
               'lemmatization': 'yes',
               'stopwords_deletion': 'no',
               'emojis_processing': 'no',
               'vulgar_processing': 'yes'}

def preprocess(text, params={'punctuation_deletion': 'no',
                             'ner_processing': 'no',
                             'lemmatization': 'no',
                             'stopwords_deletion': 'no', 
                             'emojis_processing': 'no', 
                             'vulgar_processing': 'no'}):
    
    if params['punctuation_deletion'] == 'no':
        pass 
    elif params['punctuation_deletion'] == 'yes':
        text = del_punct(text)
    else:
        raise ValueError('такой опции нет')
        
        
    if params['ner_processing'] == 'no':
        pass 
    elif params['ner_processing'] == 'del':
        text = delete_ner(text)
    elif params['ner_processing'] == 'replace':
        text = replace_ner(text)
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
        
        
    if params['vulgar_processing'] == 'no':
        pass 
    elif params['vulgar_processing'] == 'yes':
        text = replace_vulgar(text)
    else:
        raise ValueError('такой опции нет')
    return text

def make_meta():
    meta = {}

    i = 0
    for punct in ['no', 'yes']:
        for ner in ['no', 'del', 'replace']:
            for lem in ['no', 'yes']:
                for stop in ['no', 'yes']:
                    for emo in ['no', 'del', 'replace', 'label']:
                        for vulg in ['no', 'yes']:
                            meta[i] = {'punctuation_deletion': punct,
                                       'ner_processing': ner,
                                       'lemmatization': lem,
                                       'stopwords_deletion': stop,
                                       'emojis_processing': emo,
                                       'vulgar_processing': vulg}
                            i += 1

    with open('meta.json', 'w') as f:
        json.dump(meta, f, ensure_ascii=False)

    return meta