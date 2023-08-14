"""
reads a fasta file containing DNA sequences and reports which
entry has the highest percentage GC content.

written to solve Rosalind Problem "Computing GC Content"
http://rosalind.info/problems/gc/
"""


def lines_from_file(filename):
    """produces a list of lined from a file provided as an input"""
    lineList = open(filename, "r").read().splitlines()
    return lineList


def parse_fasta_from_lines(lines):
    ID = []
    sequence = []
    for line in len(range(lines)):
        if lines[line].startswith(">"):
            ID.append(lines[line])
        else:
            sequence.append(line)

    pass  # TODO osmart Jan 2019: write function & get rid of this line


def parse_fasta_file(filename):
    pass  # TODO osmart Jan 2019: write function & get rid of this line


def gc_percent(sequence):
    pass  # TODO osmart Jan 2019: write function & get rid of this line


def gc_percentages(seqs):
    pass  # TODO osmart Jan 2019: write function & get rid of this line


def highest_gc_in_fasta_file(file_name):
    pass  # TODO osmart Jan 2019: write function & get rid of this line
