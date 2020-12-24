# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from unittest import TestCase

import mock
import requests

from ndic.search import search_all
from ndic.exceptions import NdicConnectionError


class NdicSearchAllTestCase(TestCase):

    def test_search_korean_word_multiple_meaning(self):
        test_search_korean_word = "말"
        test_corresponding_english_word_1 = "(언어) word, language, speech, " \
                                            "(literary) tongue"
        test_corresponding_english_word_2 = "(동물) horse"
        test_corresponding_english_word_3 = "(마지막) end (of), close (of)"
        test_corresponding_english_word_4 = "(분량을 재는 단위) mal (≒18 liters), Korean unit of measure"
        test_corresponding_english_word_5 = "이회토(점토와 석회로 구성된 흙)"

        results = search_all(test_search_korean_word)
        self.assertEqual(len(results), 5)

        self.assertEqual(
            results[0],
            test_corresponding_english_word_1,
        )
        self.assertEqual(
            results[1],
            test_corresponding_english_word_2,
        )
        self.assertEqual(
            results[2],
            test_corresponding_english_word_3,
        )
        self.assertEqual(
            results[3],
            test_corresponding_english_word_4,
        )
        self.assertEqual(
            results[4],
            test_corresponding_english_word_5,
        )

    @mock.patch.object(requests, 'get', side_effect=requests.ConnectionError)
    def test_search_without_internet_network(self, mock_requests):
        test_search_korean_word = "사과"
        self.assertRaises(
            NdicConnectionError,
            search_all,
            test_search_korean_word,
        )
