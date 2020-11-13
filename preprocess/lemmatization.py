from pymorphy2 import MorphAnalyzer

morph = MorphAnalyzer()

def lemmatizer(text_data: str):
  text_data = text_data.split()
  lemms = [morph.parse(i.text)[0].normal_form for i in text_data]
  return " ".join(lemms)


"""
usage:
lemms_string = lemmatizer(text_string)
"""
