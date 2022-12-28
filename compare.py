import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='path to the input file .txt that contains paths to code files')
parser.add_argument('output_file', help='path to the output file to write')
args = parser.parse_args()  # Parsing console arguments
in_file = args.input_file
out_file = args.output_file

with open(in_file, 'r') as code_files:
    files_paths = code_files.read().split()
    print(files_paths)
