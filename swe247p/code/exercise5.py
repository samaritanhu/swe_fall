# Author  :  Xinyi Hu
# Contact :  xinyih20@uci.edu
# We are going to replace Score_counts with a more fair formula: cosine similarity.


import sys

sys.path.append("..")
from utils.zip_process import ZipFileProcessing
import os
from exercise2 import process_text
import math

INV_PATH = "../data/inv-index/output-index.txt"


class SearchEngine:
    def __init__(self):
        self.zip_helper = ZipFileProcessing()
        self.inv_index = self.zip_helper.txt2dict(INV_PATH)
        self.N = 10001
        self.idf_weights = {}
        self.docu_term_numerator = {}  # (log(f_ik) + 1) log(N/n_k)
        self.docu_term_denominator = {}  # (\sum[(log(f_ik) + 1) log(N/n_k)]^2)
        self.docu_term = {}  # docu_term_numerator / docu_term_denominator
        self.query_w_numerator = {}
        self.query_w_denominator = 0
        self.query_weight = {}  # query_w_numerator / query_w_denominator

    def score_counts(self, processed_q):
        # Cosine(d, q) = \sum dij qj / \sqrt(\sum dij qj)
        score_c_numerator = {}
        score_c_denominator = {}
        score_c = {}

        # d_ik = (log(f_ik) + 1) log(N/n_k) / \sqrt(\sum[(log(f_ik) + 1) log(N/n_k)]^2)
        for term in processed_q:
            if term in self.inv_index:
                # inverse document frequency weight: log(N/n_k)
                # N is the number of documents in the collection
                # nk is the number of documents in which term k occurs.
                if term not in self.idf_weights:
                    self.idf_weights[term] = math.log(self.N / (len(self.inv_index[term])))
                # Denominator
                for docName in self.inv_index[term]:
                    if docName not in self.docu_term_numerator:
                        self.docu_term_numerator[docName] = {}
                    if term not in self.docu_term_numerator[docName]:
                        #  (log(f_ik) + 1) log(N/n_k)
                        self.docu_term_numerator[docName][term] = (math.log(len(self.inv_index[term][docName])) + 1) * \
                                                                  self.idf_weights[term]
                    if docName not in self.docu_term_denominator:
                        self.docu_term_denominator[docName] = 0
                    # ((log(f_ik) + 1) log(N/n_k))^2
                    self.docu_term_denominator[docName] += math.pow(self.docu_term_numerator[docName][term], 2)
        # d_ik = (log(f_ik) + 1) log(N/n_k) / \sqrt(\sum[(log(f_ik) + 1) log(N/n_k)]^2)
        for term in processed_q:
            if term in self.inv_index:
                for docName in self.inv_index[term]:
                    if docName not in self.docu_term:
                        self.docu_term[docName] = {}
                    self.docu_term[docName][term] = self.docu_term_numerator[docName][term] / math.sqrt(
                        self.docu_term_denominator[docName])

        # q_ik = (log(f_ik) + 1) log(N/n_k) / \sqrt(\sum[(log(f_ik) + 1) log(N/n_k)]^2)
        for term in processed_q:
            if term in self.inv_index:
                # (log(f_ik) + 1) log(N/n_k)
                self.query_w_numerator[term] = (math.log(processed_q.count(term)) + 1) * self.idf_weights[term]
                # ((log(f_ik) + 1) log(N/n_k))^2
                self.query_w_denominator += math.pow(self.query_w_numerator[term], 2)

        for term in processed_q:
            if term in self.inv_index:
                self.query_weight[term] = self.query_w_numerator[term] / math.sqrt(self.query_w_denominator)

        # cosine distance
        # Cosine(d, q) = \sum dij qj / \sqrt(\sum dij^2 qj^2)
        for doc in self.docu_term:
            for term in processed_q:
                if term in self.docu_term[doc]:
                    if doc not in score_c_numerator:
                        score_c_numerator[doc] = 0
                        score_c_denominator[doc] = 0
                    score_c_numerator[doc] += self.docu_term[doc][term] * self.query_weight[term]
                    score_c_denominator[doc] += math.pow(self.docu_term[doc][term], 2) * math.pow(
                        self.query_weight[term], 2)
        for doc in score_c_numerator:
            score_c[doc] = score_c_numerator[doc] / math.sqrt(score_c_denominator[doc])

        return score_c

    def score_positions(self, processed_q):
        # Score_positions(d, q) = SUM(1 / Shortest(t_i, t_i+1, d)) for 0 <= i < terms t in q
        score_p = {}
        for i in range(len(processed_q) - 1):
            current_term_1, current_term_2 = processed_q[i], processed_q[i + 1]
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
                num=i + 1, doc_1=doc_name[0], doc_2=doc_name[1], doc_3=doc_name[2], doc_4=doc_name[3], doc_name=doc_name
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