import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='path to the input file .txt that contains paths to code files')
parser.add_argument('output_file', help='path to the output file to write')
args = parser.parse_args()  # Parsing console arguments.
in_file = args.input_file  # Name of the file with input.
out_file = args.output_file  # Name of the file for the answer.


def levenstein(str1, str2):  # returns number -- levenstein distance, how different lines are.
    matrix = [[i + j if i * j == 0 else 0 for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + np.min([matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]])
    return matrix[len(str1)][len(str2)]


answers = []
with open(in_file, mode='r', encoding='utf-8') as code_files:
    files_paths = code_files.read().split()  # Array of names of files with code.
    for index in range(0, len(files_paths) - 1, 2):
        with open(files_paths[index], mode='r', encoding='utf-8') as code1, open(files_paths[index + 1], mode='r',
                                                                                 encoding='utf-8') as code2:
            lines1 = code1.read().replace(' ', '').split()  # getting rid of everything but words
            lines2 = code2.read().replace(' ', '').split()
            ans = 0
            symbols = 0
            for line1, line2 in zip(lines1, lines2):
                ans += levenstein(line1, line2)
                symbols += np.max([len(line1), len(line2)])
            answers.append(ans / symbols)

with open(out_file, mode='w', encoding='utf-8') as output:  # write into file
    for res in answers:
        output.write('{:.3}\n'.format(res))
