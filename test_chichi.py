# -*- coding: utf-8 -*-

from chichi import ChiPaiException, MeloChiChiException, NotDoingAnythingException, UnknownChiChiException, chikubi, pipi, predict_cup
import unittest


class TestChiChi(unittest.TestCase):

    def test_fetch_actoress_cup(self):
        self.assertEqual(pipi('綿貫芽衣子'), 'F')


    def test_have_not_oppai(self):
        self.assertEqual(pipi('女優さん'), 'Have not Oppai!')


    def test_hello_world(self):
        self.assertEqual(pipi(), 'Hello World!')


    def test_pipi(self):
        self.assertEqual(pipi('相内しおり'), 'D')


    def test_three_size(self):
        self.assertEqual(pipi('マツコデラックス'), 'B140/W140/H140')


    def test_predict_cup(self):
        self.assertEqual(predict_cup(60, 68), 'AA')


    def test_chipai_exception(self):
        with self.assertRaises(ChiPaiException):
            predict_cup(50, 50)


    def test_melon_exception(self):
        with self.assertRaises(MeloChiChiException):
            predict_cup(200, 200)


    def test_unknown_exception(self):
        with self.assertRaises(UnknownChiChiException):
            predict_cup(100, 80)


    def test_unknown_exception_with_nokey(self):
        with self.assertRaises(UnknownChiChiException):
            predict_cup(60, 200)


    def test_chikubi(self):
        self.assertEqual(chikubi('weak'), 'もっと強くっ')


    def test_not_do_anything(self):
        with self.assertRaises(NotDoingAnythingException):
            chikubi('test')


if __name__ == "__main__":
    unittest.main()
