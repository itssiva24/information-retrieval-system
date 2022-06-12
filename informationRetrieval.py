from util import *

# Add your import statements here
from collections import Counter
import numpy as np
import math





class InformationRetrieval():

	def __init__(self):
		self.index = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = None

		#Fill in code here
		index = {}
		for doc in docs:
			all_terms = []
			for sentence in doc:
				for term in sentence:
					all_terms.append(term)
			all_terms = list(Counter(all_terms).items())
			for term, term_freq in all_terms:
				if term not in index:
					index[term] = [[docIDs[docs.index(doc)], term_freq]]
				else:
					index[term].append([docIDs[docs.index(doc)], term_freq])

		self.docIDs = docIDs
		self.index = index


	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []

		#Fill in code here
		doc_wt = {}
		total_docs = len(self.docIDs)
		idf = {}

		for docID in self.docIDs:
			doc_wt[docID] = [0]*len(self.index.keys())

		for term in self.index:
			idf[term] = math.log(float(total_docs / len(self.index[term])))

		for key, term in enumerate(self.index):
			for docID, term_freq in self.index[term]:
				doc_wt[docID][key] = (term_freq * idf[term])
		norm_docVector = {docID: (np.linalg.norm(doc_wt[docID])) for docID in doc_wt}


		for query in queries:
			query_wt = {}
			all_terms = []
			for sentence in query:
				for term in sentence:
					all_terms.append(term)
			all_terms = list(Counter(all_terms).items())

			for term, term_freq in all_terms:
				if term in idf:
					query_wt[term] = term_freq*idf[term]
				else:
					query_wt[term] = 0

			reduced_qVector = [query_wt[term] if term in query_wt else 0 for term in self.index]
			cosine_sim = {docID: (np.dot(reduced_qVector,doc_wt[docID])/(norm_docVector[docID] * np.linalg.norm(reduced_qVector)) if norm_docVector[docID] > 0 and np.linalg.norm(reduced_qVector) > 0 else 0) for docID in doc_wt}
			doc_IDs_ordered.append(sorted(cosine_sim, key=cosine_sim.get, reverse = True))
		
		return doc_IDs_ordered



# For debugging
if __name__ == "__main__":
	ir = InformationRetrieval()
	docs = [[["experimental", "investigation", "aerodynamics", "wing", "slipstream"], ["experimental", "study", "wing", "propeller", "slipstream", "wa", "made", "order", "determine", "spanwise", "distribution", "lift", "increase", "due", "slipstream", "different", "angle", "attack", "wing", "different", "free", "stream", "slipstream", "velocity", "ratio"], ["result", "intended", "part", "evaluation", "basis", "different", "theoretical", "treatment", "problem"], ["comparative", "span", "loading", "curve", "together", "supporting", "evidence", "showed", "substantial", "part", "lift", "increment", "produced", "slipstream", "wa", "due", "/destalling/", "boundary-layer-control", "effect"], ["integrated", "remaining", "lift", "increment", "subtracting", "destalling", "lift", "wa", "found", "agree", "well", "potential", "flow", "theory"], ["empirical", "evaluation", "destalling", "effect", "wa", "made", "specific", "configuration", "experiment"]], [["simple", "shear", "flow", "past", "flat", "plate", "incompressible", "fluid", "small", "viscosity"], ["study", "high-speed", "viscous", "flow", "past", "two-dimensional", "body", "usually", "necessary", "consider", "curved", "shock", "wave", "emitting", "nose", "leading", "edge", "body"], ["consequently", "exists", "inviscid", "rotational", "flow", "region", "shock", "wave", "boundary", "layer"], ["situation", "arises", "instance", "study", "hypersonic", "viscous", "flow", "past", "flat", "plate"], ["situation", "somewhat", "different", "prandtl", "'s", "classical", "boundary-layer", "problem"], ["prandtl", "'s", "original", "problem", "inviscid", "free", "stream", "outside", "boundary", "layer", "irrotational", "hypersonic", "boundary-layer", "problem", "inviscid", "free", "stream", "must", "considered", "rotational"], ["possible", "effect", "vorticity", "recently", "discussed", "ferri", "libby"], ["present", "paper", "simple", "shear", "flow", "past", "flat", "plate", "fluid", "small", "viscosity", "investigated"], ["shown", "problem", "treated", "boundary-layer", "approximation", "novel", "feature", "free", "stream", "ha", "constant", "vorticity"], ["discussion", "restricted", "two-dimensional", "incompressible", "steady", "flow"]], [["boundary", "layer", "simple", "shear", "flow", "past", "flat", "plate"], ["boundary-layer", "equation", "presented", "steady", "incompressible", "flow", "pressure", "gradient"]], [["approximate", "solution", "incompressible", "laminar", "boundary", "layer", "equation", "plate", "shear", "flow"], ["two-dimensional", "steady", "boundary-layer", "problem", "flat", "plate", "shear", "flow", "incompressible", "fluid", "considered"], ["solution", "boundary-", "layer", "thickness", "skin", "friction", "velocity", "distribution", "boundary", "layer", "obtained", "karman-pohlhausen", "technique"], ["comparison", "boundary", "layer", "uniform", "flow", "ha", "also", "made", "show", "effect", "vorticity"]], [["one-dimensional", "transient", "heat", "conduction", "double-layer", "slab", "subjected", "linear", "heat", "input", "small", "time", "internal"], ["analytic", "solution", "presented", "transient", "heat", "conduction", "composite", "slab", "exposed", "one", "surface", "triangular", "heat", "rate"], ["type", "heating", "rate", "may", "occur", "example", "aerodynamic", "heating"]]]
	queries = [[["similarity", "law", "must", "obeyed", "constructing", "aeroelastic", "model", "heated", "high", "speed", "aircraft"]], [["structural", "aeroelastic", "problem", "associated", "flight", "high", "speed", "aircraft"]], [["problem", "heat", "conduction", "composite", "slab", "solved", "far"]], [["criterion", "developed", "show", "empirically", "validity", "flow", "solution", "chemically", "reacting", "gas", "mixture", "based", "simplifying", "assumption", "instantaneous", "local", "chemical", "equilibrium"]], [["chemical", "kinetic", "system", "applicable", "hypersonic", "aerodynamic", "problem"]], [["theoretical", "experimental", "guide", "turbulent", "couette", "flow", "behaviour"]], [["possible", "relate", "available", "pressure", "distribution", "ogive", "forebody", "zero", "angle", "attack", "lower", "surface", "pressure", "equivalent", "ogive", "forebody", "angle", "attack"]], [["method", "-dash", "exact", "approximate", "-dash", "presently", "available", "predicting", "body", "pressure", "angle", "attack"]], [["paper", "internal", "/slip", "flow/", "heat", "transfer", "study"]], [["real-gas", "transport", "property", "air", "available", "wide", "range", "enthalpy", "density"]], [["possible", "find", "analytical", "similar", "solution", "strong", "blast", "wave", "problem", "newtonian", "approximation"]], [["aerodynamic", "performance", "channel", "flow", "ground", "effect", "machine", "calculated"]], [["basic", "mechanism", "transonic", "aileron", "buzz"]], [["paper", "shock-sound", "wave", "interaction"]], [["material", "property", "photoelastic", "material"]], [["transverse", "potential", "flow", "body", "revolution", "calculated", "efficiently", "electronic", "computer"]], [["three-dimensional", "problem", "transverse", "potential", "flow", "body", "revolution", "reduced", "two-dimensional", "problem"]], [["experimental", "pressure", "distribution", "body", "revolution", "angle", "attack", "available"]], [["doe", "exist", "good", "basic", "treatment", "dynamic", "re-entry", "combining", "consideration", "realistic", "effect", "relative", "simplicity", "result"]], [["ha", "anyone", "formally", "determined", "influence", "joule", "heating", "produced", "induced", "current", "magnetohydrodynamic", "free", "convection", "flow", "general", "condition"]], [["doe", "compressibility", "transformation", "fail", "correlate", "high", "speed", "data", "helium", "air"]], [["anyone", "else", "discover", "turbulent", "skin", "friction", "sensitive", "nature", "variation", "viscosity", "temperature"]]]
	ir.buildIndex(docs, [1,2,3, 4,5])
	a = ir.rank(queries)
