# import seq_import as imp

class nucleotide_chain:

	def __init__(self, data=None):
		self.data = data

	def findStart(self):
		#add for no start codon 
		#ADD UPPERR
		startIndex = self.data.find('AUG')
		return startIndex

	def length(self):
		return len(self.data)


	def type(self):
		if 'T' in self.data:
			seq_type = 'DNA'
		if 'U' in self.data:
			seq_type = 'RNA'
		return seq_type
	
	def translate_sequence(self):
		translate_dict = {'T' : 'A', 'A' : 'U', 'C' : 'G', 'G' : 'C'}
		translated_sequence = ''
		for i in range(0,len(self.data)):
			translated_sequence+=translate_dict.get(self.data[i])
		self.data = translated_sequence

class proteins(nucleotide_chain):
	def __init__(self, data=None):
		self.data = data

	def codon(self):
		if super().type() == 'DNA':
			super().translate_sequence()
		print(self.data)
		start_location = super().findStart()
		new_sequence = self.data[start_location:]
		codons = []
		for i in range(0, len(new_sequence), 3):
			codons.append(new_sequence[i:3+i])
		
		return codons

	def protein_sequence(self):
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
		protein_list=[]
		for i in codon_list:
			protein_list=protein_list+[amino_acid_dict.get(i)]
		print(protein_list)

if __name__ == "__main__":
	# seq = imp.txt_to_seq("Test_DNA.txt")
	X = proteins('TACGGCGTTAGACAAGTGCGTGAGTACACA')
	X.protein_sequence()
