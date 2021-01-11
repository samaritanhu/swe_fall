# Author  :  Xinyi Hu
# Contact :  xinyih20@uci.edu

# In this part of the project, you will finally develop a search interface for searching occurrences of words in the corpus.
# Your search interface can be as simple as the one you saw in the Lucene demo -- so, console based, very simple results.
# But if you want, you can make a GUI or a Web interface (no extra credit for that, it just makes for nicer demos if you want to show this to external people).
# For sake of simplicity, there is no need for paging options; simply show the top 10 results.

import sys
sys.path.append("..")
from utils.zip_process import ZipFileProcessing
import os
from exercise2 import process_text

INV_PATH = "../data/inv-index/output-index.txt"


class SearchEngine:
    def __init__(self):
        self.zip_helper = ZipFileProcessing()
        self.inv_index = self.zip_helper.txt2dict(INV_PATH)

    def score_counts(self, processed_q):
        # Score_counts(d, q) = SUM(count(t, d)) for all terms t in q and
        score_c = {}
        for term in processed_q:
            if term in self.inv_index:
                for doc_name in self.inv_index[term]:
                    score_c[doc_name] = score_c.get(doc_name, 0) + len(self.inv_index[term][doc_name])
        return score_c

    def score_positions(self, processed_q):
        # Score_positions(d, q) = SUM(1 / Shortest(t_i, t_i+1, d)) for 0 <= i < terms t in q
        score_p = {}
        # for i in range(0) - so this loop would not begin
        for i in range(len(processed_q)-1):
            current_term_1, current_term_2 = processed_q[i], processed_q[i+1]
            if current_term_1 in self.inv_index:
                for doc_name in self.inv_index[current_term_1]:
                    if doc_name in self.inv_index[current_term_2]:
                        pos_i = self.inv_index[current_term_1][doc_name]
                        pos_j = self.inv_index[current_term_2][doc_name]
                        distance = float("inf")
                        for p_i in pos_i:
                            for p_j in pos_j:
                                if abs(p_i - p_j) < distance:
                                    distance = abs(p_i - p_j)
                        if distance != float("inf"):
                            score_p[doc_name] = 1 / distance

        return score_p

    def nlargest(self, score_query, n=10):
        sorted_score_query = sorted(score_query.items(), key=lambda item: item[1], reverse=True)
        return sorted_score_query[:n]

    def print_res(self, res):
        doc_names = [s[0] for s in res]
        if not doc_names:
            print("Not found")
            return
        print("Top 10 results:")
        for i, doc_name in enumerate(doc_names):
            print("{num}. aleph.gutenberg.org/{doc_1}/{doc_2}/{doc_3}/{doc_4}/{doc_name}".format(
                num=i+1, doc_1=doc_name[0], doc_2=doc_name[1], doc_3=doc_name[2], doc_4=doc_name[3], doc_name=doc_name
            ))

    def query(self, q):
        processed_q = process_text(q).split(' ')
        score_c = self.score_counts(processed_q)
        score_q = self.score_positions(processed_q)

        # Score(d, q) = Score_counts(d, q) + Score_positions(d, q), where
        score_query = {}
        for key in list(set(score_c) | set(score_q)):
            if score_c.get(key) and score_q.get(key):
                score_query.update({key: score_c.get(key) + score_q.get(key)})
            else:
                score_query.update({key: score_c.get(key) or score_q.get(key)})
        res = self.nlargest(score_query)
        self.print_res(res)


def main(test=True):
    search_engine = SearchEngine()
    if test:
        q = "byron's wife and children"
        print("Q> " + q)
        search_engine.query(q)
    else:
        while True:
            q = input("Q> ")
            if q == "quit":
                break
            search_engine.query(q)


if __name__ == "__main__":
    main(test=False)
