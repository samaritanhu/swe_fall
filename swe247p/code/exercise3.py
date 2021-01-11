# Author  :  Xinyi Hu
# Contact :  xinyih20@uci.edu

# In this second part of the project, you are going to develop a program that reads the text files produced in the previous module and that produces an inverted index.
# Here's an example of two input files and a first version of the inverted index:
# Document 1:
# document describ market strategi carri compani agricultur chemic report predict market share chemic report market
# statist agrochem pesticid herbicid fungicid insecticid fertil predict sale market share stimul demand price cut volum sale

# Document 2:
# document predict sale market share demand price cut

# Inverted Index (output):
# agricultur 1:1:7
# agrochem 1:1:17
# carri 1:1:5
# chemic 1:2:8,13
# compani 1:1:6
# cut 1:1:30;2:1:8
# demand 1:1:28;2:1:6
# describ 1:1:2
# document 1:1:1;2:1:1
# fertil 1:1:22
# fungicid 1:1:20
# herbicid 1:1:19
# insecticid 1:1:21
# market 1:4:3,11,15,25;2:1:4
# pesticid 1:1:18
# predict 1:2:10,23;2:1:2
# price 1:1:29;2:1:7
# report 1:2:9,14
# sale 1:2:24,32;2:1:3
# share 1:2:12,26;2:1:5
# statist 1:116
# stimul 1:1:27
# strategi 1:1:4
# volum 1:1:31

# Here is what these numbers mean. Picking some random entries up there:
#
# agricultur 1:1:7 means the term "agricultur" appears in document 1, 1 time, at position 7 (1:1:7)
# market 1:4:3,11,15,25;2:1:4 means the term "market" appears in document 1, 4 times, at positions 3, 11, 15, and 25 (1:4:3,11,15,25); and in document 2, 1 time, at position 4 (2:1:4)
# etc.
# Each of these entries is called a "posting." Each posting consists of the term and the list of documents where the term occurs, along with a "payload" of additional information. In this case, the payload is the number of times the term occurs in that document, followed by its positions. Note that this payload will change slightly later on.

import collections
from utils.zip_process import ZipFileProcessing
import os
import zipfile

invertedindexdict = collections.defaultdict()
INPUT_PATH = "../data/input-transform"
OUTPUT_PATH = "../data/inv-index/output-index.txt"


def inverted_index(content, doc_name):
    for index, word in enumerate(content.split(' ')):
        if word not in invertedindexdict:
            invertedindexdict[word] = {}
        if doc_name not in invertedindexdict[word]:
            invertedindexdict[word][doc_name] = []
        invertedindexdict[word][doc_name].append(index)


def read_all(input_path, fp):
    if os.path.isdir(input_path):
        for f in os.listdir(input_path):
            if '.txt' in f:
                content = fp.readtxt(input_path + '/' + f)
                doc_name = f.replace('.txt','')
                inverted_index(content, doc_name)
            else:
                read_all(input_path + '/' + f, fp)


def convert_result():
    res = ""
    for term in sorted(invertedindexdict):
        temp = term + ' '
        for doc in sorted(invertedindexdict[term]):
            temp += doc + ':' + str(len(invertedindexdict[term][doc])) + ':'
            for pos in invertedindexdict[term][doc]:
                temp += str(pos) + ','
            temp = temp[:-1] + ';'
        res += temp[:-1] + '\n'
    return res


def run(test=True):
    if test:
        doc_1 = "document describ market strategi carri compani agricultur chemic report predict market share chemic report market statist agrochem pesticid herbicid fungicid insecticid fertil predict sale market share stimul demand price cut volum sale"
        doc_2 = "document predict sale market share demand price cut"
        inverted_index(doc_1, "1")
        inverted_index(doc_2, "2")
        print(convert_result())
    else:
        zip_helper = ZipFileProcessing()
        read_all(INPUT_PATH, zip_helper)
        zip_helper.writetxt(convert_result(), OUTPUT_PATH)


if __name__ == "__main__":
    run(test=True)