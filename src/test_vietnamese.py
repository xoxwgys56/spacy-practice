import spacy

from sentencizer import sentencizer


def get_nlp_client():
    """
    test using multilanguage
    """
    nlp = spacy.load('xx_ent_wiki_sm')
    config = {"punct_chars": None}
    nlp.add_pipe("sentencizer", config=config)

    return nlp


def test_vietnamese():
    """
    use translation result from google-translator.
    include dot (end of sentence)

    eng: "Hello nice to meet you. I am baby yoda."
    """

    print("🏁 inlcude dot case.")
    sentencizer(get_nlp_client(), 'Xin chào Hân hạnh được gặp bạn. Tôi là baby yoda.')

    """
    include dot

    kor: "안녕하세요 반갑습니다. 저는 아기 요다입니다."
    """

    print("🏁 inlcude dot case.")
    sentencizer(get_nlp_client(), 'Xin chào Hân hạnh được gặp bạn. Tôi là bé Yoda.')

    """
    exclude dot

    eng: Hello nice to meet you I am baby yoda
    """

    print("\n🏁 exlcude dot case.")
    sentencizer(get_nlp_client(), 'Xin chào, rất vui được gặp bạn, tôi là baby yoda')

    """
    exclude dot

    kor: 안녕하세요 반갑습니다 저는 아기 요다입니다
    """

    print("\n🏁 exlcude dot case.")
    sentencizer(get_nlp_client(), 'xin chào, rất vui được gặp bạn, tôi là baby yoda')