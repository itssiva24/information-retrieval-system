from util import *


from evaluation import Evaluation
import matplotlib.pyplot as plt
evaluator = Evaluation()
def Evaluation_metrics(doc_IDs_ordered, query_ids, qrels, n_comp, title, should_output = 0, output_folder = "./output/", include_plot = 0):

    precisions, recalls, fscores, MAPs, nDCGs = [], [], [], [], []
    for k in range(1,11):
        precision = evaluator.meanPrecision(
            doc_IDs_ordered, query_ids, qrels, k)
        precisions.append(precision)
        recall = evaluator.meanRecall(
            doc_IDs_ordered, query_ids, qrels, k)
        recalls.append(recall)
        fscore = evaluator.meanFscore(
            doc_IDs_ordered, query_ids, qrels, k)
        fscores.append(fscore)
        MAP = evaluator.meanAveragePrecision(
            doc_IDs_ordered, query_ids, qrels, k)
        MAPs.append(MAP)
        nDCG = evaluator.meanNDCG(
            doc_IDs_ordered, query_ids, qrels, k)
        nDCGs.append(nDCG)
        print("Precision, Recall and F-score @ " +  
            str(k) + " : " + str(precision) + ", " + str(recall) + 
            ", " + str(fscore))
        print("MAP, nDCG @ " +  
            str(k) + " : " + str(MAP) + ", " + str(nDCG))
        if (should_output > 0):
        # saving the results
            with open(output_folder+'Results/LSA_'+str(n_comp)+'.txt', 'a') as f:
                f.write(str(k) + " , " + str(precision) + ", " + str(recall) + 
                        ", " + str(fscore)+", "+str(MAP) + ", " + str(nDCG)+'\n')
            with open(output_folder+'Results/metrics_'+str(k)+'.txt', 'a') as f:
                f.write(str(n_comp) + " , " + str(precision) + ", " + str(recall) + 
                        ", " + str(fscore)+", "+str(MAP) + ", " + str(nDCG)+'\n')
            
    # Plot the metrics and save plot 
    if (include_plot == 1):
        plt.figure(figsize=(10,5))
        plt.plot(range(1, 11), precisions, label="Precision")
        plt.plot(range(1, 11), recalls, label="Recall")
        plt.plot(range(1, 11), fscores, label="F-Score")
        plt.plot(range(1, 11), MAPs, label="MAP")
        plt.plot(range(1, 11), nDCGs, label="nDCG")
        plt.legend()
        plt.title(title)
        plt.xlabel("k")
        if(should_output):
            plt.savefig(output_folder + "LSA_"+str(n_comp)+".png")
    return