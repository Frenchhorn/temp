import os
import json
import sys
import time
import uuid
import collections

from nltk.corpus import stopwords

COMMON_WORDS = set(stopwords.words('english'))
DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')
OUTPUT_DIRECTORY = os.path.join(os.path.dirname(__file__), 'output')

def save_file(filename, data):
    random_str = uuid.uuid4().hex
    outfile = '%s_%s.txt'%(filename.split('.')[0], random_str)
    with open(os.path.join(OUTPUT_DIRECTORY, outfile), 'w') as outfile:
        outfile.write(data)

def get_word_counts(filename):
    proc = os.getpid()
    print('Processed %s with process id: %s'%(filename, proc))
    wordcount = collections.Counter()
    # get counts
    with open(os.path.join(DATA_DIRECTORY, filename), 'r', encoding='utf8') as f:
        for line in f:
            wordcount.update(line.split())
    for word in COMMON_WORDS:
        del wordcount[word]
    # save file
    save_file(filename, json.dumps(dict(wordcount.most_common(20))))
    # simulate long-running task
    time.sleep(2)

if __name__ == '__main__':
    get_word_counts(sys.argv[1])