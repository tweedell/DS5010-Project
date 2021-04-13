# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:25:15 2021

@author: Andrew Tweedell, Ameya Gokhale
"""

import os
import string
import seq_import_tests as sit

# function to import and format text string from text files
def txt_to_seq(file):
    """
    A function to read in text file of nucleotide sequences and perform
    preliminary checks
    param file: A string containing the file name in current directory
    returns: single item list containing nucleotide sequence
    """
    # check if file name provided is string. Exit with warning if not.
    if not isinstance(file, str):
        print("Input file name not valid.")
        return None

    # open file, extract first line of text, save line, and close file
    with open(file, "rt") as my_file:
        seq = my_file.readlines()
        seq = seq[0]

    # verify that only letters for nucleotides are present in sequence
    allowed = ('A', 'T', 'C', 'G', 'U')
    if not all(char in allowed for char in seq):
        print("An unknown nucleotide item was found in the sequence!")
        return None

    # determine if sequence represents DNA or RNA depending on precense of 'T'
    # or 'U' (DNA and RNA, respectively)
    if 'T' in seq:
        seq_type = 'DNA'
    elif 'U' in seq:
        seq_type = 'RNA'
    else:
        seq_type = 'Unknown'

    # Print import success statement
    print("Successfully imported %s sequence." % seq_type)

    # return single string containing nucleotide sequence
    return seq

# function to
def nucleo_freq(x):
    """
    function to count the number of instances of each specific nucleotide in an
    imported sequence
    param x: str containing nucleotide sequence
    returns: dictionary of counts with keys as the nucleotide indicator and the
    value is the count
    """

    iterable = iter(x)
    count_dict = dict()

    for item in iterable:

        if item not in count_dict:

            count_dict[item] = 1

        elif item in count_dict:

            count_dict[item] += 1

    return count_dict


#if __name__ == "__main__":