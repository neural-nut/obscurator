import os
import re
import glob
import sys
from collections import Counter


def clean_paths(directory, n):
    """take the paths of a directory of videos and return only the titles"""
    paths = glob.glob(directory, recursive=True)
    paths = ' '.join([str(elem) for elem in paths])

    text = re.findall(r'[\w\s,\-\'.()]+(?=\s-\s[\w\-]{11}\.mp4)', paths)
    #print(text)
    text = ' '.join([str(elem) for elem in text])
    text = re.sub(r'[\-_,.()]', '', text, flags=re.MULTILINE)
    text = text.lower()
    words = re.split(r'[.?!,:\"]+\s*|\s+', text)

    #print(words)
    grams = zip(*[words[i:] for i in range(int(n))])
    most_common = Counter(grams).most_common(1000)
    for ngram, count in most_common:
        print(' '.join(ngram), count)



if __name__ == '__main__':

    clean_paths(sys.argv[1], sys.argv[2])

