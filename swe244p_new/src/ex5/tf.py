import re
import sys
import collections
import threadpool
import os

# stopwords = set(open('stop_words').read().split(','))
# words = re.findall('\w{3,}', open(sys.argv[1]).read().lower())
# counts = collections.Counter(w for w in words if w not in stopwords)
# for (w, c) in counts.most_common(25):
#     print w, '-', c

class word_counter:
    def __init__(self):
        self.counts = collections.Counter()

    def count_file(self, file_name):
        words = re.findall('\w{3,}', open(file_name).read().lower())
        self.counts += collections.Counter(w for w in words if w not in self.stopwords)

    def main(self):
        self.stopwords = set(open('stop_words').read().split(','))
        file_names = ['anonymit.txt','cDc-0200.txt','crossbow.txt','gems.txt']
        pool = threadpool.ThreadPool(10)
        requests = threadpool.makeRequests(self.count_file, file_names)
        [pool.putRequest(req) for req in requests]  # all the requests are thrown to the pool
        pool.wait()  # quit after all the threads stop
        for (w, c) in self.counts.most_common(40):
            print(w, '-', c)


if __name__ == "__main__":
    wc = word_counter()
    wc.main()