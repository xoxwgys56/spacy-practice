from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from spacy.language import Language

def sentencizer(nlp: Language, input_sentence: str):
    print(f"original sentence before sentencizer : {input_sentence}")

    doc = nlp(input_sentence)

    for idx, sent in enumerate(doc.sents):
        print(f'{idx} {sent}')