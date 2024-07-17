#!/usr/bin/env python3
"""Compute and report all pairwise AFDs based on MAFs

Usage:
    <program> input_mafs output_afds
"""

# Modules
import sys

# Parse user input
try:
    input_mafs = sys.argv[1]
    output_afds = sys.argv[2]
except:
    print(__doc__)
    sys.exit(1)

# Read, compute, report
with open(input_mafs) as infile:
    with open(output_afds, "wt") as outfile:
        for line in infile:
            if line.startswith("Chromo"):
                continue

            l = line.strip().split("\t")
            chrom, pos = l[: 2]
            infos = [float(x) for x in l[2: ]]
            n = len(infos)

            new_line = [chrom, pos]

            for i in range(n+1):
                for j in range(i+1, n):
                    new_line.append(str(round(abs(infos[i] - infos[j]), 6)))

            outfile.write("\t".join(new_line) + "\n")
