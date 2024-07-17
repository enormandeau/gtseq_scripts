#!/usr/bin/env python3
"""Score subset of SNPs chosen by Raphael according to the presence of
neighbouring SNPs.

- Less or no SNPs in the surrounding region is best
- SNPs with low MAFs are not as bad

Usage:
    <program> input_selected_snps input_all_snps input_genome window_size output_file
"""

# Modules
from collections import defaultdict
import gzip
import sys

# Classes
class Fasta(object):
    """Fasta object with name and sequence
    """

    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    def write_to_file(self, handle):
        handle.write(">" + self.name + "\n")
        handle.write(self.sequence + "\n")

    def __repr__(self):
        return self.name + " " + self.sequence[:31]

# Defining functions
def myopen(_file, mode="rt"):
    if _file.endswith(".gz"):
        return gzip.open(_file, mode=mode)

    else:
        return open(_file, mode=mode)

def fasta_iterator(input_file):
    """Takes a fasta file input_file and returns a fasta iterator
    """
    with myopen(input_file) as f:
        sequence = []
        name = ""
        begun = False

        for line in f:
            line = line.strip()

            if line.startswith(">"):
                if begun:
                    yield Fasta(name, "".join(sequence))

                name = line[1:]
                sequence = ""
                begun = True

            else:
                sequence += line

        if name != "":
            yield Fasta(name, "".join(sequence))

# Parsing user input
try:
    input_selected_snps = sys.argv[1]
    input_all_snps = sys.argv[2]
    input_genome = sys.argv[3]
    window_size = int(sys.argv[4])
    output_file = sys.argv[5]
except:
    print(__doc__)
    sys.exit(1)

# Load genome
genome = dict()

fasta = fasta_iterator(input_genome)

for f in fasta:
    genome[f.name.split(" ")[0]] = f.sequence.upper()

# Load all SNPs
all_snps = defaultdict(lambda: defaultdict(list))

with myopen(input_all_snps) as infile:
    for line in infile:
        if line.startswith("chromo"):
            continue

        l = line.strip().split("\t")
        chrom, pos, major, minor, ancestral, EM, nind = l
        pos = int(pos)
        EM = float(EM)
        nind = int(nind)

        pos_truncated = pos // window_size

        all_snps[chrom][pos_truncated].append((chrom, pos, major, minor, ancestral, EM, nind))

# Score selected SNPs using all the SNPs
with open(input_selected_snps) as infile:

    with open(output_file, "wt") as outfile:
        # Header
        outfile.write("Chrom\tPosition\tNumSNPs\tSumMAFs\tComplexity\tGCcontent\tChrom2\tPosition2\tMajor\tMinor\tAncestral\tFst\tNumSamples\tSequenceMod\tSequence\n")

        for line in infile:
            if "position" in line:
                continue

            l = line.strip().split("\t")
            chrom = l[0]
            pos = int(l[1])

            pos_truncated = pos // window_size

            surrounding_snps = (all_snps[chrom][pos_truncated - 1] +
                    all_snps[chrom][pos_truncated] +
                    all_snps[chrom][pos_truncated + 1])

            center_snp = [x for x in surrounding_snps if abs(x[1] - pos) == 0][0]

            # Version for Hyung Bae's data containing SNPs not in the overall bedfile
            #try:
            #    center_snp = [x for x in surrounding_snps if abs(x[1] - pos) == 0][0]
            #except:
            #    continue

            surrounding_snps = [x for x in surrounding_snps if
                    abs(x[1] - pos) and abs(x[1] - pos) <= window_size]

            sum_mafs = sum([x[5] for x in surrounding_snps])
            num_snps = len(surrounding_snps)

            seq = list(genome[chrom][pos - window_size - 1: pos + window_size])
            seq_original = "".join(seq)

            # Use compression, patterns, GC content...
            complexity = len(gzip.compress("".join(seq).encode()))
            gc_content = (seq.count("G") + seq.count("C")) / len(seq)

            for s in surrounding_snps:
                seq[s[1] - pos + window_size] = "N"

            seq[window_size] = "[" + center_snp[2] + "/" + center_snp[3] + "]"

            outfile.write("\t".join([str(x) for x in l +
                [num_snps, round(sum_mafs, 4), complexity, round(gc_content, 4)] +
                list(center_snp) +
                ["".join(seq), seq_original]
                ]) + "\n")
