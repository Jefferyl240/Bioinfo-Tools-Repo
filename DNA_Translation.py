#!/usr/bin/env python3
#DNA Translation
#This program can translate DNA sequence into amino acids and counts the numnber of amino acids and stop codon in inputed DNA sequence.
#Usage: $0 <dnafile>
#Author: Jie Lin
#Date: 12/2/2021
###############################################################################################################################
import sys, re, os
#checking the number of arguments.
if len(sys.argv) != 2:
    print('Usage: %s <dnafile>' % (sys.argv[0]))
    print('Incorrect number of arguments. Please input correct number of arguments.')
    exit()
#Error checking:file read checks
existence = os.path.exists(sys.argv[1])
if not(existence):#checking if the file exist.
    print('the dnafile is not exist.')
    exit()
readable_check = os.access(sys.argv[1], os.R_OK)
if not(readable_check):#checking if the file has read permission.
    print('the dnafile has no read permission.')
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
#function for reading codons from dna sequence, it will fold dna string into a list of codons.
def read_codon(str):
    codon_list = []
    for codon in range(0, len(str), 3):
        codon_list.append(str[codon : codon + 3])
    return codon_list
#translation dictionary with codon as key.
translation_table = {
    'ATA':'ILE', 'ATC':'ILE', 'ATT':'ILE', 'ATG':'MET',
    'ACA':'THR', 'ACC':'THR', 'ACG':'THR', 'ACT':'THR',
    'AAC':'ASN', 'AAT':'ASN', 'AAA':'LYS', 'AAG':'LYS',
    'AGC':'SER', 'AGT':'SER', 'AGA':'ARG', 'AGG':'ARG',
    'CTA':'LEU', 'CTC':'LEU', 'CTG':'LEU', 'CTT':'LEU',
    'CCA':'PRO', 'CCC':'PRO', 'CCG':'PRO', 'CCT':'PRO',
    'CAC':'HIS', 'CAT':'HIS', 'CAA':'GLN', 'CAG':'GLN',
    'CGA':'ARG', 'CGC':'ARG', 'CGG':'ARG', 'CGT':'ARG',
    'GTA':'VAL', 'GTC':'VAL', 'GTG':'VAL', 'GTT':'VAL',
    'GCA':'ALA', 'GCC':'ALA', 'GCG':'ALA', 'GCT':'ALA',
    'GAC':'ASP', 'GAT':'ASP', 'GAA':'GLU', 'GAG':'GLU',
    'GGA':'GLY', 'GGC':'GLY', 'GGG':'GLY', 'GGT':'GLY',
    'TCA':'SER', 'TCC':'SER', 'TCG':'SER', 'TCT':'SER',
    'TTC':'PHE', 'TTT':'PHE', 'TTA':'LEU', 'TTG':'LEU',
    'TAC':'TYR', 'TAT':'TYR', 'TAA':'***', 'TAG':'***',
    'TGC':'CYS', 'TGT':'CYS', 'TGA':'***', 'TGG':'TRP',
}
amino_list = []
#call read_codon() to convert string to codons.
codon_list = read_codon(dna_str.upper()) #change string to uppercase letter since translation dict is all capitalized.
#reading amino acids from dictionary of translation table.
for codon in codon_list:
    amino_list.append(translation_table[codon])
print('\nAmino Acid Sequence:', *amino_list)
print('\nAmino Acid Counts:\n')
amino_list.sort()
stop_codon_count = 0
amino_count_dict = {}
#count number of amino acid and stop codon in the amino acid sequence.
for amino in amino_list:
    if amino == '***': #*** represents stop codons.
        stop_codon_count +=1
    else:
        amino_count_dict[amino] = amino_list.count(amino) #storing amino acid counts in the format of dictionary for later access.
#sorting the amino acid count according to count value from 
amino_count_dict = sorted(amino_count_dict.items(), key=lambda x:x[1], reverse=True)
for amino in amino_count_dict:
    print(amino[0], amino[1])
print('')
print(len(amino_count_dict),'amino acids found.')
if stop_codon_count == 0:
    print('No stop codon was found.')
if stop_codon_count == 1:
    print('A stop codon was found.')
else:
    print(stop_codon_count,'stop codon was found.')
