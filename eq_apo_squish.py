# for argument handling
import argparse
# for path handling (Python 3.4+)
from pathlib import Path
# for bailing out
import sys
# for regex matching
import re

# argument handling
parser = argparse.ArgumentParser()
parser.add_argument("path_to_txt_file",
                    help="Path to the EQAPO text file to process")
parser.add_argument("squish_amount_pct",
                    type=float,
                    help="Percent value to adjust gains to (ex: 50)")
args = parser.parse_args()

# path handling
path_to_txt_file = Path(args.path_to_txt_file).absolute()
parent_dir = Path(args.path_to_txt_file).absolute().parent
# generate output filename
squished_filename = "{}_squished_{}_pct.txt".format(
    Path(args.path_to_txt_file).stem, args.squish_amount_pct)
# store squishage percentage
squish_amount_pct = args.squish_amount_pct
## test printing parent dir
print(f"parent dir: {parent_dir}")
print(f"will write to: {parent_dir / squished_filename}")

input_lines = []

# open the file
try:
    with open(path_to_txt_file, 'r') as f:
        input_lines = f.readlines()
except Exception as e:
    print(f"Error: Unable to access input file: {str(e)}")
    sys.exit(1)

# check for and adjust preamp
for line in input_lines:
    if line.startswith("Preamp: "):
        preamp = float(line.strip(" dB\n").lstrip("Preamp: "))
        new_preamp = round(preamp * (squish_amount_pct / 100), 2)
        # substitute the new preamp value
        line = "Preamp: " + str(new_preamp) + " dB\n"

# WIP: do things with the filter gains
for line in input_lines:
    if re.match(r'^Filter.+Gain.+', line):
        print(line)
# TODO: save the resulting file
# try:
#     with open(parent_dir / squished_filename, 'w') as f:
#         flat_text = ""
#         for lines in input_lines:
#             flat_text += lines
#         f.write(flat_text)
# except Exception as e:
#     print(f"Error: Unable to write output file: {str(e)}")
#     sys.exit(1)
