# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 09:25:15 2021

@author: Andrew Tweedell, Ameya Gokhale
"""

import os
import seq_import_tests as sit

# function to import and format text string from text files
def txt_to_seq(file):
    """
    A function to read in text file of nucleotide sequences and perform
    preliminary checks
    param file: A string containing the file name
    returns: single item list containing nucleotide sequence
    """
    # check if file name provided is string. Exit with warning if not.
    if not isinstance(file, str):
        print("Input file name not valid.")
        return None

    # open file, extract first line of text, save line, and close file
    with open(file, "rt") as my_file:
        my_lines = my_file.read()

    #check if any non-character items in sequence

    # determine if sequence represents DNA or RNA depending on precense of 'T'
    # or 'U' (DNA and RNA, respectively)
    if 'T' is in seq:
        seq_type = 'DNA'
    elif 'U' is in seq:
        seq_type = 'RNA'

    # Print import success statement
    print("Successfully import %s sequence." % seq_type)

    # return single element list containing character sequence
    return seq

# function to
def nucleo_freq(char_seq):
    """

    param :
    returns:
    """