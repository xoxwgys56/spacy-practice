import spacy

# spacy.prefer_gpu()
# nlp = spacy.load("en_core_web_sm")

from test_chinese import test_chinese
from test_vietnamese import test_vietnamese


if __name__ == '__main__':
    print('test vietnamese using multi-language')
    test_vietnamese()