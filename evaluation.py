from util import *

# Add your import statements here
import numpy as np


class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here
		relevant_docs_retrieved = 0
		for doc_id in query_doc_IDs_ordered[:k]:
			if doc_id in true_doc_IDs:
				relevant_docs_retrieved += 1
		precision = relevant_docs_retrieved / k
		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here
		precision = 0
		for query_id in query_ids:
			ground_truth = [int(qrel["id"]) for qrel in qrels if int(qrel["query_num"]) == int(query_id)]
			precision += self.queryPrecision(doc_IDs_ordered[query_id - 1], query_id, ground_truth, k)

		meanPrecision = precision / len(query_ids)
		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here
		relevant_docs_retrieved = 0
		for doc_id in query_doc_IDs_ordered[:k]:
			if doc_id in true_doc_IDs:
				relevant_docs_retrieved += 1
		
		recall = relevant_docs_retrieved / len(true_doc_IDs)
		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here
		recall = 0
		for query_id in query_ids:
			ground_truth = [int(qrel["id"]) for qrel in qrels if int(qrel["query_num"]) == int(query_id)]
			recall += self.queryRecall(doc_IDs_ordered[query_id - 1], query_id, ground_truth, k)

		meanRecall = recall / len(query_ids)
		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here
		precision = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		recall = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)

		if(precision == 0 and recall == 0):
			fscore = 0
		else:
			fscore = (2 * precision* recall) / (precision + recall)
		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here
		f_score = 0
		for query_id in query_ids:
			ground_truth = [int(qrel["id"]) for qrel in qrels if int(qrel["query_num"]) == int(query_id)]
			f_score += self.queryFscore(doc_IDs_ordered[query_id - 1], query_id, ground_truth, k)
		meanFscore = f_score/(len(query_ids))

		return meanFscore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		#Fill in code here
		true_doc_IDs_ids = true_doc_IDs[0]
		true_doc_IDs_rels = true_doc_IDs[1]
		rels = []

		DCG = 0
		for i, doc_ID in enumerate(query_doc_IDs_ordered[:k]):
			if doc_ID in true_doc_IDs_ids:
				doc_idx = true_doc_IDs_ids.index(doc_ID)
				rel = true_doc_IDs_rels[doc_idx]
				rels.append([rel ,i+1])
				DCG += rel/(np.log2(i + 2))

		optim_rels = list(sorted(rels, key = lambda item : item[0], reverse = True))
        
		IDCG = 0
		for i in range(len(optim_rels)):
			rel = optim_rels[i][0]
			IDCG += rel/(np.log2(i + 2))

		# nDCG
		if IDCG == 0: nDCG = 0
		else:
			nDCG = DCG/IDCG
		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here
		nDCG = 0
		for query_id in query_ids:
			true_doc_IDs_ids = [int(qrel["id"]) for qrel in qrels if int(qrel["query_num"]) == int(query_id)]
			true_doc_IDs_rels = [qrel["position"] for qrel in qrels if int(qrel["query_num"]) == int(query_id)]     # relavances
			nDCG += self.queryNDCG(doc_IDs_ordered[query_id - 1], query_id, [true_doc_IDs_ids, true_doc_IDs_rels], k)
		meanNDCG = nDCG/(len(query_ids))

		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here
		precision = 0
		c = 0
		for i in range(k):
			if(query_doc_IDs_ordered[i] in true_doc_IDs):
				c += 1
				precision += c / (i + 1)
		if(c == 0):
			avgPrecision = 0
		else:
			avgPrecision = precision / c

		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here
		true_doc_IDs = []
		avg_precision = 0
		for query_id in query_ids:
			true_doc_IDs = [int(qrel["id"]) for qrel in q_rels if int(qrel["query_num"]) == int(query_id)]
			avg_precision += self.queryAveragePrecision(doc_IDs_ordered[query_id - 1], query_id, true_doc_IDs, k)
		meanAveragePrecision = avg_precision/(len(query_ids))
		return meanAveragePrecision

