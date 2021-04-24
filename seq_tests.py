# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:37:30 2021

@author: Andrew Tweedell, Ameya Gokhale
"""

import seq_import
import seq_translate
import unittest

class TestSeqImport(unittest.TestCase):

	def test_DNA_txt_to_seq(self):
		actual = seq_import.txt_to_seq('Test_DNA.txt')
		expected = 'TACATGATTGACATTGAGGATCCATGACATTGAGCCATGAT'
		self.assertEqual(actual, expected)

	def test_RNA_txt_to_seq(self):
		actual = seq_import.txt_to_seq('Test_RNA.txt')
		expected = 'AUGUACGUACGUAGCGUAGCUCGCCGUACUAAAGUCGAU'
		self.assertEqual(actual, expected)

class TestNucleotideChain(unittest.TestCase):

	def setUp(self):
		self.DNA = seq_translate.NucleotideChain(seq_import.txt_to_seq('Test_DNA.txt'))
		self.RNA = seq_translate.NucleotideChain(seq_import.txt_to_seq('Test_RNA.txt'))

	def test_DNA_nucleo_freq(self):
		actual = self.DNA.nucleo_freq()
		expected = {'T': 12, 'A': 13, 'C': 7, 'G': 9}
		self.assertEqual(actual, expected)

	def test_RNA_nucleo_freq(self):
		actual =  self.RNA.nucleo_freq()
		expected = {'A': 10, 'U': 10, 'G': 10, 'C': 9}
		self.assertEqual(actual, expected)

	def test_DNA_find_start(self):
		actual = self.DNA.find_start()
		self.assertIsNone(actual, 'Should not find start codon')

	def test_RNA_find_start(self):
		actual = self.RNA.find_start()
		self.assertEqual(actual, 0, 'Should be 0')

	def test_DNA_seq_type(self):
		self.assertEqual(self.DNA.seq_type(), 'DNA', 'Should be DNA')

	def test_RNA_seq_type(self):
		self.assertEqual(self.RNA.seq_type(), 'RNA', 'Should be RNA')

	def test_DNA_transcribe(self):
		actual = self.DNA.transcribe_sequence()
		expected = 'AUGUACUAACUGUAACUCCUAGGUACUGUAACUCGGUACUA'
		self.assertEqual(actual, expected)

	def test_RNA_transcribe(self):
		self.assertIsNone(self.RNA.transcribe_sequence(), 'Should return None')

class TestProteins(unittest.TestCase):

	def setUp(self):
		self.DNA = seq_translate.Proteins(seq_import.txt_to_seq('Test_DNA.txt'))
		self.RNA = seq_translate.Proteins(seq_import.txt_to_seq('Test_RNA.txt'))

	def test_DNA_codon(self):
		actual = self.DNA.codon()
		expected = ['AUG', 'UAC', 'UAA', 'CUG', 'UAA', 'CUC', 'CUA', 'GGU', 'ACU', 'GUA', 'ACU', 'CGG', 'UAC', 'UA']
		self.assertEqual(actual, expected)

	def test_RNA_codon(self):
		actual = self.RNA.codon()
		expected = ['AUG', 'UAC', 'GUA', 'CGU', 'AGC', 'GUA', 'GCU', 'CGC', 'CGU', 'ACU', 'AAA', 'GUC', 'GAU']
		self.assertEqual(actual, expected)

	def test_DNA_protein_sequence(self):
		actual = self.DNA.protein_sequence()
		expected = ['MET',  'TYR', 'STOP', 'LEU', 'STOP', 'LEU', 'LEU', 'GLY', 'THR', 'VAL', 'THR', 'ARG', 'TYR', None]
		self.assertEqual(actual, expected)

	def test_RNA_protein_sequence(self):
		actual = self.RNA.protein_sequence()
		expected = ['MET', 'TYR', 'VAL', 'ARG', 'SER', 'VAL', 'ALA', 'ARG', 'ARG', 'THR', 'LYS', 'VAL', 'ASP']
		self.assertEqual(actual, expected)

if __name__ == "__main__":
	unittest.main()