# for argument handling
import argparse
# for path handling (Python 3.4+)
from pathlib import Path

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
# generate output filename
squished_filename = Path(args.path_to_txt_file).stem + "_squished_" + str(
    args.squish_amount_pct) + "_pct.txt"
# test printing parent dir
parent_dir = Path(args.path_to_txt_file).absolute().parent
print(f"parent dir: {parent_dir}")
print(f"will write to: {parent_dir / squished_filename}")

# open the file
try:
    with open(path_to_txt_file, 'r') as f:
        print(f)
except Exception as e:
    print(f"Error: Unable to access file: {str(e)}")

# TODO: check for preamp
# TODO: do things with the filter gains
# TODO: save the resulting file
