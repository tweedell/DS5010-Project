# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:37:30 2021

@author: Andrew Tweedell, Ameya Gokhale
"""

import seq_import
#from . import seq_translate
import unittest

class TestSeqImport(unittest.TestCase):

    def test_DNA_txt_to_seq(self):
        actual = seq_import.txt_to_seq('Test_DNA.txt')
        expected = 'ATGATTGACATTGAGGATCCATGACATTGAGCCATGAT'
        self.assertEqual(actual, expected)

    def test_RNA_txt_to_seq(self):
        actual = seq_import.txt_to_seq('Test_RNA.txt')
        expected = 'AUGUACGUACGUAGCGUAGCUCGCCGUACUAAAGUCGAU'
        self.assertEqual(actual, expected)

class TestNucleoFreq(unittest.TestCase):

    def setUp(self):
        self.DNA = seq_import.txt_to_seq('Test_DNA.txt')
        self.RNA = seq_import.txt_to_seq('Test_RNA.txt')

    def test_DNA_nucleo_freq(self):
        actual = seq_import.nucleo_freq(self.DNA)
        expected = {'A': 12, 'T': 11, 'G': 9, 'C': 6}
        self.assertEqual(actual, expected)

    def test_RNA_nucleo_freq(self):
        actual = seq_import.nucleo_freq(self.RNA)
        expected = {'A': 10, 'U': 10, 'G': 10, 'C': 9}
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()