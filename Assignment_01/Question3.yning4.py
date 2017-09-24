import numpy as np
from scipy.stats import mode
import statistics
import scipy
import math

class Data(object):
    def __init__(self):
        pass

    def getOnLineScoreData(self):
        data_file = open("data.online.scores.txt", 'r')
        lines = data_file.readlines()
        data = []

        for eachLine in lines:
            data.append(eachLine.split())
            #   change data list into data array:
        data = np.array(data)
        midterm_scores = data[:, 1]
        final_scores = data[:, 2]
        #   change str type into int:
        midterm_scores = list(map(int, midterm_scores))
        final_scores = list(map(int, final_scores))

        #   close file here：
        data_file.close()
        return midterm_scores, final_scores

    def getLibraryData(self):
        data_file = open("data.libraries.inventories.txt")
        lines = data_file.readlines()
        data = []

        for eachLine in lines:
            data.append(eachLine.split())
        cml = np.array(data[1][1:101])
        cbl = np.array(data[2][1:101])
        cml = list(map(int, cml))
        cbl = list(map(int, cbl))

        #   close file here：
        data_file.close()
        return cml, cbl



class Question3():

    def __init__(self, cml, cbl):
        self.cml = cml
        self.cbl = cbl


#   print("\nSubject:    CS 412 DATA_MINING (Fall 2017)")
    print("Title:      Homework_1 Qestion_3")
    print("Name:       Yayi Ning\n\n")

    def Jaccard_coeff(self, count_01, count_10, count_11):
        print("Question 3 (a):")
        Jaccard = count_11 /(count_01 + count_10 + count_11)
        print("The Jaccard coefficient of Citadel's Maester Library (CML) and Castle Black's library(CBL) is: ", Jaccard, "\n\n")

    def minkowski_distance(self):
        print("Question 3 (b):")
        mink_1 = scipy.spatial.distance.minkowski(self.cml, self.cbl, 1)
        mink_2 = scipy.spatial.distance.minkowski(self.cml, self.cbl, 2)
        mink_infi = scipy.spatial.distance.minkowski(self.cml, self.cbl, math.inf)
        print("The minkowski distance of CML and CBL for h = 1 is: ", mink_1)
        print("The minkowski distance of CML and CBL for h = 2 is: ", mink_2)
        print("The minkowski distance of CML and CBL for h = infinity is: ", mink_infi, "\n\n")

    def cosine_simililarity(self):
        print("Question 3 (c):")
        cos_similarity = 1 - scipy.spatial.distance.cosine(self.cml, self.cbl)
        print("The cosine similarity of CML and CBL is :", cos_similarity, "\n\n")

    def Kullback_Leibler_divergence(self):
        print("Question 3 (d):")
        p_cml = self.cml/sum(np.array(self.cml)[:])
        p_cbl = self.cbl/sum(np.array(self.cbl)[:])
        D_cml_cbl = sum(p_cml * np.log(p_cml/p_cbl))
        print("Kullbac-Leibler divergence between Citadel's Maester Library (CML) and Castle Black's library(CBL) is : ", D_cml_cbl)


""" ===================== main function ===================== """
def main():
    data = Data()
    """
    onlineScores_mid, onlineScores_final = data.getOnLineScoreData()
    q1 = Question1(onlineScores_mid)
    mean1 = q1.q1_get_mean()
    var1 = q1.q1_get_variance()

    q2 = Question2(onlineScores_mid)
    z_scores = q2.z_normolization(mean1, var1)
    q2.compare_variances(z_scores, var1)
    q2.normalize_90(mean1, var1)
    q2.correlation_final_midterm(onlineScores_mid, onlineScores_final)
    q2.covariance_final_midterm(onlineScores_mid, onlineScores_final)
    """
    cml, cbl = data.getLibraryData()
    q3 = Question3(cml, cbl)
    q3.Jaccard_coeff(120, 2, 58)
    q3.minkowski_distance()
    q3.cosine_simililarity()
    q3.Kullback_Leibler_divergence()

    print("==========================End Question 3================================\n\n")


if __name__ == "__main__":
    main()