import spacy
# from spacy.lang.zh.examples import sentences

from sentencizer import sentencizer


def get_nlp_client():
    nlp = spacy.load('zh_core_web_sm')
    config = {"punct_chars": None}
    nlp.add_pipe("sentencizer", config=config)

    return nlp
    

def test_chinese():
    """
    use translation result from google-translator.
    include dot (end of sentence)

    kor: "안녕하세요 반갑습니다. 저는 아기 요다입니다."
    eng: "Hello nice to meet you. I am baby yoda."
    """

    print("🏁 inlcude dot case.")
    sentencizer(get_nlp_client(), '你好，很高兴认识你。我是宝贝尤达。')

    """
    exclude dot

    eng: Hello nice to meet you I am baby yoda
    """

    print("\n🏁 exlcude dot case.")
    sentencizer(get_nlp_client(), '你好很高兴认识你我是宝贝尤达')

    """
    exclude dot

    kor: 안녕하세요 반갑습니다 저는 아기 요다입니다
    """

    print("\n🏁 exlcude dot case.")
    sentencizer(get_nlp_client(), '你好很高兴认识你我是尤达宝贝')