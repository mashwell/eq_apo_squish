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
parent_dir = path_to_txt_file.parent
# generate output filename
output_filename = "{}_squished_{}_pct.txt".format(
    Path(args.path_to_txt_file).stem, args.squish_amount_pct)
output_full_pathname = parent_dir / output_filename
# store squishage percentage
squish_amount_pct = args.squish_amount_pct

input_lines = []
output_lines = ""

# open the file
try:
    with open(path_to_txt_file, 'r') as f:
        input_lines = f.readlines()
except Exception as e:
    print(f"Error: Unable to access input file: {str(e)}")
    sys.exit(1)

for line in input_lines:
    # regex match for filter lines
    match = re.match(r'^Filter.+Gain (.+?) dB Q.+$', line)
    # check for and adjust preamp
    if line.startswith("Preamp: "):
        preamp = float(line.strip(" dB\n").lstrip("Preamp: "))
        # calculate new preamp from squish % and round it to 3 digit precision
        new_preamp = round(preamp * (squish_amount_pct / 100), 3)
        # substitute the new preamp value
        line = "Preamp: " + str(new_preamp) + " dB\n"
        output_lines += line
    # adjust filter gains
    elif (match):
        gain = match.group(1)
        # calculate new gains from squish % and round it to 3 digit precision
        new_gain = str(round(float(gain) * (squish_amount_pct / 100), 3))
        # substitute the new gain value
        line = line.replace(gain, new_gain)
        output_lines += line
    else:
        output_lines += line

# save the resulting file
try:
    with open(output_full_pathname, 'w') as f:
        f.write(output_lines)
        print(
            f"Resulting filters written successfuly to {output_full_pathname}."
        )
except Exception as e:
    print(f"Error: Unable to write output file: {str(e)}")
    sys.exit(1)
