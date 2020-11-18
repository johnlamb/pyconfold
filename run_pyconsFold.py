#!/usr/bin/env python3
"""Docstring"""
import sys
import pyconsFold
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("fa_file", type=str, help="input sequence file in FASTA format")
parser.add_argument("rr_file", type=str, help="Contact file in CASP format, with or without error as last column")
parser.add_argument("out_dir", type=str, help="Output directory to write results")

parser.add_argument("-fa2_file", "--fa2", type=str, help="input sequence file in FASTA format for the second sequence")
parser.add_argument("-ss_file", "--ss", default='', type=str, help="Secondary structure file in ss2/3 format")

args = parser.parse_args()

########## Only uncomment ONE of these lines
pyconsFold.model(args.fa_file, args.out_dir, rr=args.rr_file, ss=args.ss,save_step=True, tmscore_pdb_file="tests/data/2hiuA.pdb")
# pyconsFold.model_dist(args.fa_file, args.out_dir, rr=args.rr_file)
# pyconsFold.model_dock(args.fa_file, args.fa2_file, args.out_dir, rr=args.rr_file)

