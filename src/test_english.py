import spacy

from sentencizer import sentencizer


def get_effeciency_nlp_client():
    """
    test using english
    high speed. low accuracy.
    """
    nlp = spacy.load('en_core_web_sm')
    config = {"punct_chars": None}
    nlp.add_pipe("sentencizer", config=config)

    return nlp


def get_accuracy_nlp_client():
    """
    test using english
    high accuracy. low speed
    """
    raise Exception('failed download using spacy. can not load trained pipeline')

    nlp = spacy.load("en_core_web_trf")
    config = {"punct_chars": None}
    nlp.add_pipe("sentencizer", config=config)

    return nlp

def test_english():
    print("🏁 inlcude dot case. high effeciency. 🏃🏻")
    english_sents = sentencizer(get_effeciency_nlp_client(), 'On August 27, 2018, in connection with the completion of the Merger, Cotiviti Corporation, a Delaware company (“Cotiviti Corporation”) and Cotiviti Internal Holdings, Inc., a Delaware corporation (together with Cotiviti Corporation, “Party”) ”, “loan”), each subsidiary of Cotiviti, has fully repaid all outstanding debts, together with interest and all other amounts due in connection with such repayment, according to Agree. The first Linked Credit Agreement has been modified and reinstated to some extent, as of September 28, 2016, by and between the Borrower, Cotiviti Intermediate Holdings, Inc., a Delaware corporation, lender and JPMorgan Chase Bank, NA as regulator of the agency lender (the “Current Credit Agreement”), and terminate all engagements therein. Termination of the existing Credit Agreement takes effect on the effective date of the Consolidation (“Effective Date”) on August 27, 2018.')
    print(f'english {sum(1 for _ in english_sents)} sentences.')