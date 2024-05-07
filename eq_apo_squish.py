# for argument handling
import argparse
# for path, etc handling
import os

# argument handling
parser = argparse.ArgumentParser()
parser.add_argument("path_to_txt_file",
                    help="Path to the EQAPO text file to process")
parser.add_argument("squish_amount_pct",
                    type=float,
                    help="Percent value to adjust gains to (ex: 50)")
args = parser.parse_args()
path_to_txt_file = os.path.abspath(args.path_to_txt_file)

# open the file
try:
    with open(path_to_txt_file, 'r') as f:
        print(f)
except Exception as e:
    print(f"Error: Unable to access file '{path_to_txt_file}': {str(e)}")

# TODO: check for preamp
# TODO: do things with the filter gains
# TODO: save the resulting file