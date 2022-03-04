import spacy

from sentencizer import sentencizer


def get_effeciency_nlp_client():
    """
    test using multilanguage
    high speed. low accuracy.
    """
    nlp = spacy.load('xx_ent_wiki_sm')
    config = {"punct_chars": None}
    nlp.add_pipe("sentencizer", config=config)

    return nlp


def get_accuracy_nlp_client():
    """
    test using multilanguage
    high accuracy. low speed
    """
    nlp = spacy.load("xx_sent_ud_sm")
    config = {"punct_chars": None}
    nlp.add_pipe("sentencizer", config=config)

    return nlp


def test_vietnamese():
    """
    use translation result from google-translator.
    include dot (end of sentence)

    original text: "On August 27, 2018, in connection with the completion of the Merger, Cotiviti Corporation, a Delaware company (“Cotiviti Corporation”) and Cotiviti Internal Holdings, Inc., a Delaware corporation (together with Cotiviti Corporation, “Party”) ”, “loan”), each subsidiary of Cotiviti, has fully repaid all outstanding debts, together with interest and all other amounts due in connection with such repayment, according to Agree. The first Linked Credit Agreement has been modified and reinstated to some extent, as of September 28, 2016, by and between the Borrower, Cotiviti Intermediate Holdings, Inc., a Delaware corporation, lender and JPMorgan Chase Bank, NA as regulator of the agency lender (the “Current Credit Agreement”), and terminate all engagements therein. Termination of the existing Credit Agreement takes effect on the effective date of the Consolidation (“Effective Date”) on August 27, 2018."
    """
    print("🏁 inlcude dot case. high effeciency. 🏃🏻")
    vietnamese_sents = sentencizer(get_effeciency_nlp_client(), 'Vào ngày 27 tháng 8 năm 2018, liên quan đến việc hoàn thành Sáp nhập, Cotiviti Corporation, một công ty Delaware (“Cotiviti Corporation”) và Cotiviti Internal Holdings, Inc., một tập đoàn Delaware (cùng với Cotiviti Corporation, “Party”) ”, "Khoản vay"), mỗi công ty con của Cotiviti, đã hoàn trả đầy đủ tất cả các khoản nợ chưa thanh toán, cùng với lãi suất và tất cả các khoản khác đến hạn liên quan đến việc trả nợ đó, theo Thỏa thuận. Thỏa thuận tín dụng liên kết đầu tiên đã được sửa đổi và khôi phục ở một mức độ nào đó, kể từ ngày 28 tháng 9 năm 2016, bởi và giữa Bên vay, Cotiviti Intermediate Holdings, Inc., một công ty Delaware, bên cho vay và Ngân hàng JPMorgan Chase, NA với tư cách là cơ quan quản lý của cơ quan. người cho vay (“Hợp đồng tín dụng hiện tại”), và chấm dứt tất cả các cam kết trong đó. Việc chấm dứt Hợp đồng tín dụng hiện tại có hiệu lực vào ngày Hợp nhất có hiệu lực (“Ngày có hiệu lực”) vào ngày 27 tháng 8 năm 2018.')
    english_sents = sentencizer(get_effeciency_nlp_client(), 'On August 27, 2018, in connection with the completion of the Merger, Cotiviti Corporation, a Delaware company (“Cotiviti Corporation”) and Cotiviti Internal Holdings, Inc., a Delaware corporation (together with Cotiviti Corporation, “Party”) ”, “loan”), each subsidiary of Cotiviti, has fully repaid all outstanding debts, together with interest and all other amounts due in connection with such repayment, according to Agree. The first Linked Credit Agreement has been modified and reinstated to some extent, as of September 28, 2016, by and between the Borrower, Cotiviti Intermediate Holdings, Inc., a Delaware corporation, lender and JPMorgan Chase Bank, NA as regulator of the agency lender (the “Current Credit Agreement”), and terminate all engagements therein. Termination of the existing Credit Agreement takes effect on the effective date of the Consolidation (“Effective Date”) on August 27, 2018.')
    print(f'vietnamese {len(list(vietnamese_sents))} sentences. english {len(list(english_sents))} sentences.')

    print("🏁 inlcude dot case. high accracy. 🤓")
    vietnamese_sents = sentencizer(get_accuracy_nlp_client(), 'Vào ngày 27 tháng 8 năm 2018, liên quan đến việc hoàn thành Sáp nhập, Cotiviti Corporation, một công ty Delaware (“Cotiviti Corporation”) và Cotiviti Internal Holdings, Inc., một tập đoàn Delaware (cùng với Cotiviti Corporation, “Party”) ”, "Khoản vay"), mỗi công ty con của Cotiviti, đã hoàn trả đầy đủ tất cả các khoản nợ chưa thanh toán, cùng với lãi suất và tất cả các khoản khác đến hạn liên quan đến việc trả nợ đó, theo Thỏa thuận. Thỏa thuận tín dụng liên kết đầu tiên đã được sửa đổi và khôi phục ở một mức độ nào đó, kể từ ngày 28 tháng 9 năm 2016, bởi và giữa Bên vay, Cotiviti Intermediate Holdings, Inc., một công ty Delaware, bên cho vay và Ngân hàng JPMorgan Chase, NA với tư cách là cơ quan quản lý của cơ quan. người cho vay (“Hợp đồng tín dụng hiện tại”), và chấm dứt tất cả các cam kết trong đó. Việc chấm dứt Hợp đồng tín dụng hiện tại có hiệu lực vào ngày Hợp nhất có hiệu lực (“Ngày có hiệu lực”) vào ngày 27 tháng 8 năm 2018.')
    english_sents = sentencizer(get_accuracy_nlp_client(), 'On August 27, 2018, in connection with the completion of the Merger, Cotiviti Corporation, a Delaware company (“Cotiviti Corporation”) and Cotiviti Internal Holdings, Inc., a Delaware corporation (together with Cotiviti Corporation, “Party”) ”, “loan”), each subsidiary of Cotiviti, has fully repaid all outstanding debts, together with interest and all other amounts due in connection with such repayment, according to Agree. The first Linked Credit Agreement has been modified and reinstated to some extent, as of September 28, 2016, by and between the Borrower, Cotiviti Intermediate Holdings, Inc., a Delaware corporation, lender and JPMorgan Chase Bank, NA as regulator of the agency lender (the “Current Credit Agreement”), and terminate all engagements therein. Termination of the existing Credit Agreement takes effect on the effective date of the Consolidation (“Effective Date”) on August 27, 2018.')
    print(f'vietnamese {len(list(vietnamese_sents))} sentences. english {len(list(english_sents))} sentences.')
    

def old_test_vietnamese():
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