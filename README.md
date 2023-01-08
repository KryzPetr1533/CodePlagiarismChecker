# CodePlagiarismChecker
Program using Levenshtein distance to find similarity between two python scripts in percentage.

Packages: argparse, numpy.

#### Purpose
Program shows how similar 2 codes are. Where 0 means codes are the same, 1 -- totaly different.
Program has console interface.
There are 2 arguments required -- a path to the input file with the names of the files with code to analise and a path to the file for the result.

#### Idea
During work on this program I found 5 types of algorithm, for instance, from [here](https://habr.com/ru/post/583882/). This is the simplest realization.
Basicly, program takes the texts, removes all spaces and finds Levenstein's distance between two on the same position in the text.
Then all when all distances are summarized the sum is divided by maximum length of the texts in symbols. This is the result.
