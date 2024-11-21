import json
import re
import math
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))


# function for tokenization and special character and stopword removal
def clean(data):
    # regex removes punctuation and special characters
    no_punctuation_and_specials = re.sub(r'[^\w\s]', '', str(data))

    # tokenizing step
    tokens = word_tokenize(str(no_punctuation_and_specials))

    # stopword removal
    filtered_tokens = [str(word) for word in tokens if word.lower() not in stop_words]

    # returns tokenized text in sentence format
    return " ".join(filtered_tokens)

# general function for preprocessing data
def toxicity_challenge_preprocess(data):
    # includes only needed columns: text and toxic values
    data = data[['comment_text', 'toxic']]
    data.loc[:,'comment_text'] = data['comment_text'].apply(clean) # applies preprocessing function
    data = data.reset_index(drop=True)
    data.columns = ['Text', 'Toxic'] # renames column names
    return data

# general function for preprocessing data
def sugarai_preprocess(data):
    # includes only needed columns: text and toxic values
    data = data[['text', 'is_toxic']]
    data.loc[:,'text'] = data['text'].apply(clean) # applies preprocessing function
    data = data.reset_index(drop=True)
    data.columns = ['Text', 'Toxic'] # renames column names
    return data

# general function for preprocessing data
def unintended_bias_preprocess(data):
    # includes only needed columns: text and toxic values
    data = data[['comment_text', 'toxic']]
    data.loc[:,'comment_text'] = data['comment_text'].apply(clean) # applies preprocessing function
    data = data.reset_index(drop=True)
    data.columns = ['Text', 'Toxic'] # renames column names
    return data


def check_repetition(text):
  """Counts the number of repeated words in a string."""

  words = text.lower().split()
  word_counts = Counter(words)
  repeated_words = {word: count for word, count in word_counts.items() if count > 1}
  for value in repeated_words:
    if repeated_words[value] >= 25:
      return True
  return False

