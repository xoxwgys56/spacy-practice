import spacy
# from spacy.lang.zh.examples import sentences

# spacy.prefer_gpu()
# nlp = spacy.load("en_core_web_sm")

def sentencizer(input_sentence: str):
    print(f"original sentence before sentencizer :{input_sentence}")

    doc = nlp(input_sentence)

    for idx, sent in enumerate(doc.sents):
        print(f'{idx} {sent}')


if __name__ == '__main__':
    global nlp

    nlp = spacy.load('zh_core_web_sm')
    config = {"punct_chars": None}
    nlp.add_pipe("sentencizer", config=config)
    
    """
    use translation result from google-translator.
    include dot (end of sentence)

    kor: "안녕하세요 반갑습니다. 저는 아기 요다입니다."
    eng: "Hello nice to meet you. I am baby yoda."
    """

    print("🏁 inlcude dot case.")
    sentencizer('''
        你好，很高兴认识你。我是宝贝尤达。
    ''')

    """
    exclude dot

    eng: Hello nice to meet you I am baby yoda
    """

    print("🏁 exlcude dot case.")
    sentencizer('''
        你好很高兴认识你我是宝贝尤达
    ''')

    """
    exclude dot

    kor: 안녕하세요 반갑습니다 저는 아기 요다입니다
    """

    print("🏁 exlcude dot case.")
    sentencizer('''
        你好很高兴认识你我是尤达宝贝
    ''')