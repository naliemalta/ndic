# -*- coding: utf-8 -*-

"""
This module provides functions for searching the word by Ndic

"""
from __future__ import absolute_import

from ndic.utils import make_naver_endic_url
from ndic.utils import request_naver_endic_url
from ndic.utils import get_word_meaning
from ndic.utils import get_word_meanings

def search(search_word, xth=1):
    """
    Search the word in English-Korean and Korean-English dictionaries
    and return the corresponding Korean word(s) or English word(s).

    Args:
        search_word: the word which user want to search
        xth: a specific meaning in the list of definitions returned (if there are multiple),
             denoted by the index in the result. Defaults to the first one
    Returns:
        English word(s) or Korean word(s) corresponding to the search_word
    Raises:
        NdicConnectionError: if network connection is lost.

    """
    naver_endic_url = make_naver_endic_url(search_word)
    response = request_naver_endic_url(naver_endic_url)
    word_meaning = get_word_meaning(response, xth)
    return word_meaning

def search_all(search_word):
    """
    Search the word in English-Korean and Korean-English dictionaries
    and return all corresponding Korean word(s) or English word(s) meanings.

    Args:
        search_word: the word which user want to search
    Returns:
        List of English word(s) or Korean word(s) corresponding to the search_word
    Raises:
        NdicConnectionError: if network connection is lost.

    """
    naver_endic_url = make_naver_endic_url(search_word)
    response = request_naver_endic_url(naver_endic_url)
    word_meaning = get_word_meanings(response)
    return word_meaning
