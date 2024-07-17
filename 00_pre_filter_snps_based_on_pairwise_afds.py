#!/usr/bin/env python3
"""Keep only SNPs for which at least 1 population pair has a high enough AFD

Usage:
    <program> input_afds min_afd output_ids
"""

# Modules
import sys

# Parse user input
try:
    input_afds = sys.argv[1]
    min_afd = float(sys.argv[2])
    output_ids = sys.argv[3]
except:
    print(__doc__)
    sys.exit(1)

# Read and filter
with open(output_ids, "wt") as outfile:
    with open(input_afds) as infile:
        for line in infile:
            if line.startswith("chromo"):
                continue

            l = line.strip().split(" ")
            infos = l[:2]
            data = [round(float(x), 2) for x in l[2:]]
            print(max(data))
