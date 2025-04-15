import nltk
import random
import string
import numpy as np
from constants.constants import *
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


class Services:
    def __init__(self):

        with open(CORPORA, READ) as file:
            raw = file.read()
            raw = raw.lower()
            self.sentence_token = nltk.sent_tokenize(raw)
            self.word_token = nltk.word_tokenize(raw)
            self.lemmer = nltk.stem.WordNetLemmatizer()
            self.remove_punct_dict = dict(
                (ord(punct), None) for punct in string.punctuation
            )

    def lemmitization_token(self, tokens):
        return [self.lemmer.lemmatize(token) for token in tokens]

    def lemmitization_normalize(self, text):
        return self.lemmitization_token(
            nltk.word_tokenize(text.lower().translate(self.remove_punct_dict))
        )

    def greetings(self, sentence):
        for word in sentence.split():
            if word.lower() in GREETING_INPUTS:
                return random.choice(GREETING_RESPONSES)

    def response(self):
        tf_idf_vector = TfidfVectorizer(
            tokenizer=self.lemmitization_normalize, stop_words="english"
        )
        tf_idf = tf_idf_vector.fit_transform(self.sentence_token)
        similarity_value = cosine_similarity(tf_idf[-1], tf_idf)
        idx = similarity_value.argsort()[0][-2]
        flat = similarity_value.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if req_tfidf == 0:
            return CANT_UNDERSTAND_RESPONSE
        else:
            return self.sentence_token[idx]
