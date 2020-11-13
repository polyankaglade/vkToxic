from nltk.corpus import stopwords

stop_words = set(stopwords.words('russian'))

def delete_stop_words(text_data: str, add_stop = []):
  text_data = text_data.lower()
  words = [i for i in text_data if i not in stop_words and i not in add_stop]
  return " ".join(words)
 
"""
usage:
import delete_stop_words from ....
string_without_stop_words = delete_stop_words(text_string)
"""
