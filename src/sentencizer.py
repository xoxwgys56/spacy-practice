from __future__ import annotations
from typing import TYPE_CHECKING, Generator

if TYPE_CHECKING:
    from spacy.language import Language

def sentencizer(nlp: Language, input_sentence: str) -> Generator:
    """return generator object which iterable"""
    doc = nlp(input_sentence)
    return doc.sents