"""
Created on Sat Apr 10 09:25:15 2021
@author: Andrew Tweedell, Ameya Gokhale
"""

import seq_import as imp

class nucleotide_chain:
	"""
	A class to represent the string of nucleotides taken from the text file
	"""

	def __init__(self, data=None):
		"""
		Initialize the chain with the nucleotide sequence
		"""
		self.data = data

	def findStart(self):
		"""
		find the position of the start codon to know where translation starts
		returns: index of the start codon
		"""
		startIndex = self.data.find('AUG')
		return startIndex

	def type(self):
		"""
		determine if the sequence is a DNA or RNA molecule
		returns: type of sequence-DNA/RNA
		"""
		if 'T' in self.data:
			seq_type = 'DNA'

		if 'U' in self.data:
			seq_type = 'RNA'

		return seq_type
	
	def transcribe_sequence(self):
		"""
		for transcribing to RNA if the input is DNA
		returns: no return value
		"""
		translate_dict = {'T' : 'A', 'A' : 'U', 'C' : 'G', 'G' : 'C'}
		translated_sequence = ''

		for i in range(0,len(self.data)):
			translated_sequence+=translate_dict.get(self.data[i])

		self.data = translated_sequence

class proteins(nucleotide_chain):
	"""
	A class that represents the subsequent amino acid chain formed from the initial
	nucleotide sequence
	returns: list with codons
	"""
	def __init__(self, data=None):
		"""initialize the chain with the nucleotide sequence"""
		self.data = data

	def codon(self):
		"""
		break up the RNA sequence into nucleotide tripets called codons
		returns: list with codons
		"""

		#Transcribe the sequence to RNA if it is DNA"
		if super().type() == 'DNA':
			super().transcribe_sequence()
		
		#split the nucleotide sequence into triplets based on the location of the start codon
		start_location = super().findStart()

		if start_location == -1:
			return None
		
		else:
			new_sequence = self.data[start_location:]
			codons = []
			for i in range(0, len(new_sequence), 3):
				codons.append(new_sequence[i:3+i])
			return codons
	

	def protein_sequence(self):
		"""
		convert the list of codons to their respective amino acids
		returns: no return value
		"""

		codon_list = self.codon()
		amino_acid_dict = {'UUU' : 'PHE', 'UUC' : 'PHE', 'UUA' : 'LEU', 'UUG': 'LEU', 'CUU': 'LEU',  'CUC' : 'LEU', 
		'CUA' : 'LEU', 'CUG' : 'LEU', 'AUU' : 'ILE' , 'AUC' : 'ILE', 'AUA' : 'ILE', 'AUG' : 'MET', 'GUU' : 'VAL', 
		'GUC' : 'VAL', 'GUA' : 'VAL', 'GUG' : 'VAL', 'UCU' : 'SER', 'UCC' : 'SER', 'UCA' : 'SER', 'UCG' : 'SER',
		'CCU' : 'PRO', 'CCC' : 'PRO', 'CCA' : 'PRO', 'CCG' : 'PRO', 'ACU' : 'THR', 'ACC' : 'THR', 'ACA' : 'THR',
		'ACG' : 'THR', 'GCU' : 'ALA', 'GCC' : 'ALA', 'GCA' : 'ALA','GCG' : 'ALA', 'UAU' : 'TYR', 'UAC' : 'TYR', 'UAA' : 'STOP', 
		'UAG' : 'STOP', 'CAU' : 'HIS', 'CAC' : 'HIS', 'CAA' : 'GIN', 'CAV' : 'GIN', 'AAU' : 'ASN', 'AAC' : 'ASN', 'AAA' : 'LYS',
		'AAG' : 'LYS', 'GAU' : 'ASP', 'GAC' : 'ASP','GAA' : 'GLU', 'GAG' : 'GLU,', 'UGU' : 'CYS', 'UGC' : 'CYS', 'UGA' : 'STOP',
		'UGG' : 'TRP', 'CGU' : 'ARG', 'CGC' : 'ARG', 'CGA' : 'ARG', 'CGG' : 'ARG', 'AGU' : 'SER', 'AGC' : 'SER', 'AGA' : 'ARG',
		'AGG' : 'ARG', 'GGU':'GLY','GGC' : 'GLY', 'GGA' : 'GLY','GGG' : 'GLY'}

		if codon_list != None:
			protein_list=[]
			for i in codon_list:	
				protein_list=protein_list+[amino_acid_dict.get(i)]
			print(protein_list)

		else:
			print("This gene does not translate into a protein!")


