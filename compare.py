import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='path to the input file .txt that contains paths to code files')
parser.add_argument('output_file', help='path to the output file to write')
args = parser.parse_args()  # Parsing console arguments.
in_file = args.input_file  # Name of the file with input.
out_file = args.output_file  # Name of the file for the answer.


def levenstein(line1, line2):  # returns number -- levenstein distance, how different lines are.
    matrix = [[i + j if i * j == 0 else 0 for j in range(len(line2) + 1)] for i in range(len(line1) + 1)]
    for i in range(1, len(line1) + 1):
        for j in range(1, len(line2) + 1):
            if line1[i - 1] == line2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
    return matrix[len(line1)][len(line2)]


answers = []
with open(in_file, 'r') as code_files:
    files_paths = code_files.read().split()  # Array of names of files with code.
    for index in range(0, len(files_paths) - 1, 2):
        with open(files_paths[index]) as code1, open(files_paths[index + 1]) as code2:
            words1 = code1.read().split()  # getting rid of everything but words
            words2 = code2.read().split()
            str1 = ''
            str2 = ''
            for word1, word2 in zip(words1, words2):
                str1 += word1
                str2 += word2
            answers.append(levenstein(str1, str2) / max(len(str1), len(str2)))

with open(out_file, 'w+') as output:  # write into file
    for res in answers:
        output.write('{:.3}\n'.format(res))
