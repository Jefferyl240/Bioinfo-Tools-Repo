#!/usr/bin/env python3
#A python program that will accept the pathname of dna file as it only command line argument.
#The dna file should be a text file containing a valid DNA string with no newline characters or white space characters of any kind within it. 
#The dna file should only contain the letters a,c,g,t
#Usage: $0 <dnafile>
#Author: Jie Lin
#Date: 11/21/2021
#CSCI 132 Project Option 2
######################################################################################################
import sys, re
#checking the number of arguments.
if len(sys.argv) != 2:
    print('Usage: %s <dnafile>' % (sys.argv[0]))
    print('Incorrect number of arguments. Please input correct number of arguments.')
    exit()
#storing the dna file into str variable.
dna_file = open(sys.argv[1])
dna_str = dna_file.readline()
dna_file.close()
#error checking: the dna file should letters of mulitple of 3 for reading codon patterns.
if dna_str.endswith(r'\n'): #checking if the dnafile end with newline character.
    dna_str = dna_str[:len(dna_str)-2] #removing newline character in further analysis.
else:
    print(r"The dna file is not end with a newline character'\n'")
    exit()
if len(dna_str) % 3 != 0:
    print('The dna bases in the file is not letters of mulitiple of 3.')
    exit()
#error checking: the dna file should has only the letters a,c,g, and t and no other letter characters and the last item should be \n.
validity = re.findall("[^acgt]",dna_str) #if the dna_string only consist of a,c,g, and t.
#if validity is empty that means the file pass the error checking, since no letter other than a,c,g,t.
if validity:
    print(sys.argv[1], 'is not a dnafile.')
    print('Usage: %s <desired codon> <desired position> <dnafile>' % (sys.argv[0]))
    print('Note: dnafiles for this program should only contain four types of letter g,c,a,t.')
    exit()
#Reading the codon in forward and reverse direction
codons_list_for = []
codons_list_rev = []
dna_str_rev = dna_str[::-1] #reverse dna_str.
def read_codon(codon_list, str): #function for reading codons from dna sequence.
    for codon in range(0, len(str), 3):
        codon_list.append(str[codon : codon + 3])
    return codon_list
def reading_frame(codon_list): #function for reading dna sequence according to reading frame. 
    if 'atg' not in codon_list: #if a start codon is not observed, reading_frame() will not work.
        return None
    start_codon = codon_list.index('atg') #index() will report the position of first occurance of start codon. 
    for stop_codon, codon in enumerate(codon_list):
        if codon in ['taa', 'tag','tga'] and stop_codon > start_codon:
                codon_list = codon_list[start_codon : stop_codon+1]
                return codon_list, start_codon, stop_codon #this function returns a list [reading frame, start_codon, stop_codon]
    return None #return None if a stop codon is not found at the end.
#reading frame for both directions.
codons_list_for = reading_frame(read_codon(codons_list_for, dna_str))
codons_list_rev = reading_frame(read_codon(codons_list_rev, dna_str_rev))
#display result
if (codons_list_for != None) or (codons_list_rev != None): #either of directions has a readable sequence, the result will be displayed.
    try:
        print('Forward Direction:', *codons_list_for[0])
        print('Number of Codons:', len(codons_list_for[0]))
        print('Number of bases: ', len(codons_list_for[0])*3)
    except TypeError:
        print('Forward Direction: no gene codon sequence found')
        print('The forward DNA sequence lack of start codon or stop codon.')
    try:
        print('Reverse:',*codons_list_rev[0])
        print('Number of Codons:', len(codons_list_rev[0]))
        print('Number of bases: ', len(codons_list_rev[0])*3)
    except TypeError:
        print('Reverse Direction: no gene codon sequence found')
        print('The reverse DNA sequence lack of start codon or stop codon.')
else:
    #if the file does not contain a codon sequence for a gene as desribed in both direction
    #it will print a message ot the user instead stating that no sequence is found.
    print('\nNo gene codon sequence found.')


