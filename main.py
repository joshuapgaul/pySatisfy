import argparse
import backtracker
from structures import Variable, Literal, Clause, Circuit


parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Path to input file")
args = parser.parse_args()

file = args.input_file
