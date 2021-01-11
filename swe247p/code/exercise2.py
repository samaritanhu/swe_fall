# Author  :  Xinyi Hu
# Contact :  xinyih20@uci.edu
# The transformations should include the following: tokenization, Porter stemming, and word-stopping.
# Here is an example of an input file and the corresponding output file:
#
# INPUT:
#
# Document will describe marketing strategies carried out by U.S. companies for their agricultural
# chemicals, report predictions for market share of such chemicals, or report market statistics for
# agrochemicals, pesticide, herbicide, fungicide, insecticide, fertilizer, predicted sales, market share,
# stimulate demand, price cut, volume of sales.
# OUTPUT:
#
# document describ market strategi carri compani agricultur chemic report predict market share chemic
# report market statist agrochem pesticid herbicid fungicid insecticid fertil predict sale market share
# stimul demand price cut volum sale
#

from utils.zip_process import ZipFileProcessing
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from utils.stopwords import STOPWORDS
import os
import zipfile

INPUT_PATH = "../data/input-files"
OUTPUT_PATH = "../data/input-transform"


def tokenization(sentence):
    # **Tokenizing** is the process of forming words from the sequence of characters in a document.
    return word_tokenize(sentence)


def porter_stemming(tokens):
    # Consists of a series of rules designed to the longest possible suffix at each step
    stemmer = PorterStemmer()
    stemmed_token = [stemmer.stem(token) for token in tokens]
    return stemmed_token


def word_stopping(stemmed_token):
    # Two basic types
    # –Dictionary-based: uses lists of related words
    # –Algorithmic: uses program to determine related words
    stopword = stopwords.words('english')
    stopword.extend(STOPWORDS)
    return [word for word in stemmed_token if word not in stopword]


def process_text(file):
    tokens = tokenization(file)
    stemmed_token = porter_stemming(tokens)
    filtered = word_stopping(stemmed_token)
    sentence = ' '.join(filtered)
    return sentence


def read_all(input_path, output_path, fp):
    if os.path.isdir(input_path):
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        for f in os.listdir(input_path):
            if zipfile.is_zipfile(input_path + '/' + f):
                content = fp.readzip(input_path + '/' + f)
                fp.write(process_text(content), output_path+'/'+f[:-4]+'.txt')
                fp.into_zip(output_path+'/'+f[:-4])
            else:
                read_all(input_path + '/' + f, output_path + '/' + f, fp)


def run(test=True):
    if test:
        file = """
            Document will describe marketing strategies carried out by U.S. companies for their agricultural
            chemicals, report predictions for market share of such chemicals, or report market statistics for
            agrochemicals, pesticide, herbicide, fungicide, insecticide, fertilizer, predicted sales, market share,
            stimulate demand, price cut, volume of sales.
            """
        print(process_text(file))

    else:
        zip_helper = ZipFileProcessing()
        read_all(INPUT_PATH, OUTPUT_PATH, zip_helper)


if __name__ == "__main__":
    run(test=True)