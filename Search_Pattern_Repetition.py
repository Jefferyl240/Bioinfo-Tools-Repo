#!/usr/bin/env python3
#Search pattern repetition in DNA
#This program print each line in which the pattern string is repeated N-times later in the line at starting positions that are multiples of the pattern string's length apart.
#Also, this program report the total number of times the pattern is repeated in this fashion.
#Usage: ./$0 <desired codon> <desired position> <dnafile>
#Author: Jie Lin
#First build on: 11/6/2021
#CSCI 132 Project Option 1

import sys #sys package for access line argument.
import re #re package for regular expression operations.
#checking number of arguments.
if len(sys.argv) != 4:
    print('Usage: %s <desired codon> <desired position> <dnafile>' % (sys.argv[0]))
    print('Incorrect number of arguments. Please input correct number of arguments.')
    exit()
#storing line arguments into variables.
pattern_str = str(sys.argv[1])
n_int = int(sys.argv[2])
pathname = sys.argv[3]
#getting content from dna file.
dna_file = open(pathname)
dna_str = dna_file.readline()
dna_file.close()
codons_list = []
position_list = []
frequency = 0
#error checking: the dna file should letters of mulitple of 3 for reading codon patterns.
if dna_str.endswith(r'\n'):
    dna_str = dna_str[:len(dna_str)-2] #removing newline character in further analysis.
else:
    print(r"The dna file is not end with a newline character'\n'")
    exit()
if len(dna_str) % 3 != 0:
    print('Searching pattern repetition failed.')
    print('The dna bases in the file is not letters of mulitiple of 3.')
    exit()
#error checking: the dna file should has only the letters a,c,g, and t and no other letter characters and the last item should be \n.
validity = re.findall("[^acgt]",dna_str) #if the dna_string only consist of a,c,g, and t.
#if validity is empty that means the file pass the error checking, since no letter other than a,c,g,t.
if validity:
    print(pathname, 'is not a dnafile.')
    print('Usage: %s <desired codon> <desired position> <dnafile>' % (sys.argv[0]))
    print('Note: dnafiles for this program should only contain four types of letter g,c,a,t.')
    exit()
#dna_str = dna_str[:len(dna_str)-2]
#Main function
#folding the dna string into a list of codons
for codon in range(0, len(dna_str), 3):
    codons_list.append(dna_str[codon : codon + 3]) 
#extracting codons on desired position.
for position in range(n_int-1, len(codons_list), n_int):
    position_list.append(codons_list[position])
#counting repetition of codons on desired postion.
for i in range(0, len(position_list)-1):
    if position_list[i] == position_list[i+1] and position_list[i] == pattern_str:
        frequency += 1
#reporting result of matching.
if (frequency >= 1):
    print('Searching for pattern %s every %s positions in file' % (pattern_str, n_int))
    print('\nString: %s' % (dna_str))
    print('Pattern is repeated: ',frequency)
else:
    print('Repetition of codon %s every %s position not found.' % (pattern_str, n_int))






