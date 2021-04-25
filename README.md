# Analysis of Nucleic Acid Sequences
### Authors: Andrew Tweedell, Ameya Gokhale
## Background
This Analysis of Nucleic Acid Sequences Python package aims to enable life scientists to translate and analyze DNA or RNA sequences. As gene sequencing becomes cheaper and faster and computational power increases, the ability to produce insight from statistical analyses on large sets of genetic data will become more relevant. Specific segments of DNA called genes, are used to generate an RNA sequence in a process called transcription. This RNA is then used as a template in the synthesis of amino acids called translation. This package first aims to determine whether an input sequence of nucleotides is a DNA (for purposes of this project it is assumed that the input DNA will be a single antisense string) or RNA sequence. Secondly, the specific amino acid sequence that will result from the DNA or RNA strand will be determined.

## Included Modules
seq_import.py
seq_translate.py
seq_tests.py

## Design
The modules can be thought of two phases, import and analysis. The “seq_import.py” file, by means of the “txt_to_seq” function, will extract the nucleotide sequence from a text file and return it as a string. It should be noted that the function only accepts text from the file until it encounters a whitespace. The function performs a number of checks on the string to ensure the user is importing a nucleotide string. The “seq_translate.py” module consists of two classes. The first, “NucleotideChain” serves as a parent class to represent the initial nucleotide string imported by the previous module. This class has a method (“seq_type”) that determines whether the input nucleotide sequence is an RNA or DNA molecule. If it is the latter, there is another method (“transcribe_sequence”) in the class to convert the DNA to RNA. The “find_start” method is used to determine the location of the start codon, a marker for where translation to amino acids begins. Additionally, the “nucleo_freq” method calculates the frequency of each nucleic acid present in the chain. The child class of this module, “Proteins” functions to return the amino acids sequence that results from the input sequence. The “codon” method breaks the sequence into nucleotide triplets while the “protein_sequence” matches each triplet to a corresponding amino acid sequence. Unit tests are performed from the “seq_tests.py” modules. 

## Usage
After proper installation from the Github remote repository, the users should run seq_tests.py to ensure unit tests are passed and the package is working properly. Users then would import the sequence from the target text file. To produce instances of NucleotideChain and Proteins classes, the string containing the nucleic acid sequence (imported above) will be input into the respective functions. 

>> dna_seq = txt_to_seq('Test_DNA.txt')
>> dna_chain_instance = NucleotideChain(dna_seq)
>> protein_instance = Proteins(dna_seq)

The Proteins class inherits all methods from the NucleotideChain class as protein synthesis is the next step in the process. As such, both RNA and DNA sequences can be fed into the classes, the ‘transcribe_sequence’ method from NucleotideChain will turn the DNA into RNA prior to protein synthesis, if given as input. From there, various methods are provided for the analysis and synthesis of proteins. 
