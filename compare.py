import argparse
import numpy as np
import ast

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='path to the input file .txt that contains paths to code files')
parser.add_argument('output_file', help='path to the output file to write')
args = parser.parse_args()  # Parsing console arguments.
in_file = args.input_file  # Name of the file with input.
out_file = args.output_file  # Name of the file for the answer.


def levenstein(str1, str2):  # Returns number -- levenstein distance, how different lines are.
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
        with open(files_paths[index], mode='r', encoding='utf-8') as file1, open(files_paths[index + 1], mode='r',
                                                                                 encoding='utf-8') as file2:
            code1 = file1.read()
            code2 = file2.read()

        tree1 = ast.parse(code1)
        tree2 = ast.parse(code2)


        def docstr_remover(tree):  # Removes docstrings.
            for node in ast.walk(tree):
                if not isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
                    continue
                if not len(node.body):
                    continue
                if not isinstance(node.body[0], ast.Expr):
                    continue
                if not hasattr(node.body[0], 'value') or not isinstance(node.body[0].value, ast.Str):
                    continue
                node.body = node.body[1:]


        docstr_remover(tree1)
        docstr_remover(tree2)

        lines1 = (ast.dump(tree1, annotate_fields=False)).split()  # Split into lines, so it takes less memory.
        lines2 = (ast.dump(tree2, annotate_fields=False)).split()
        ans = 0
        symbols = 0
        for line1, line2 in zip(lines1, lines2):
            ans += levenstein(line1, line2)
            symbols += np.max([len(line1), len(line2)])
        if ans * symbols == 0:
            answers.append(0.0)
        else:
            answers.append(ans / symbols)

with open(out_file, mode='w', encoding='utf-8') as output:  # Write into file.
    for res in answers:
        output.write('{:.3f}\n'.format(res))
