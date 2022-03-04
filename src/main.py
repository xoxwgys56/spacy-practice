import spacy

# spacy.prefer_gpu()
# nlp = spacy.load("en_core_web_sm")

from test_chinese import test_chinese
from test_vietnamese import test_vietnamese
from test_english import test_english


if __name__ == '__main__':
    print('get english test result before test vietnamese')
    test_english()

    print('test vietnamese using multi-language')
    test_vietnamese()

