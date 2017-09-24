import numpy as np
from scipy.stats import mode
import statistics
from collections import Counter
from itertools import groupby

class Data(object):
    def Data(self):
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
        #   change str type into int:
        midterm_scores = list(map(int, midterm_scores))

        #   close file here：
        data_file.close()
        return midterm_scores


class Question1():
    def __init__(self, scores):
        self.scores = scores


    print("\nSubject:    CS 412 DATA_MINING (Fall 2017)")
    print("Title:      Homework_1 Qestion_1")
    print("Name:       Yayi Ning\n\n")

    def Question1_a_find_max_min(self):
        print("Question 1 (a):")
        max_score = max(self.scores)
        min_score = min(self.scores)
        print("Maximum mid-term score = ", max_score)
        print("Maximum mid-term score = ", min_score,"\n")
        return max_score, max_score

    def Question1_b_find_quartile1_median_quartile3(self):
        print("Question 1 (b):")
        quartile_1 = np.percentile(self.scores, 25)
        median = np.percentile(self.scores, 50)
        quartile_3 = np.percentile(self.scores, 75)
        print("The first quartile = ", quartile_1)
        print("The median = ", median)
        print("The third quartile = ", quartile_3, "\n")
        return quartile_1, median, quartile_3

    def Question1_c_find_mean_score(self):
        print("Question 1 (c):")
        mean = np.mean(self.scores)
        print("The mean = ", mean, "\n")
        return mean

    def Question1_d_find_mode_score(self):
        print("Question 1 (d):")
        freqs = groupby(Counter(self.scores).most_common(), lambda x: x[1])
        # pick the first group (highest frequency)
        print("The mode : ", [val for val, count in next(freqs)[1]],"\n\n")

    def Question1_e_find_empirical_varicance(self):
        print("Question 1 (e):")
        var = statistics.variance(self.scores)
        print("Empirical Variance = ", var,"\n\n")
        return var


""" ===================== main function ===================== """
def main():
    data = Data()
    onlineScores = data.getOnLineScoreData()
    q1 = Question1(onlineScores)
    q1.Question1_a_find_max_min()
    q1.Question1_b_find_quartile1_median_quartile3()
    q1.Question1_c_find_mean_score()
    q1.Question1_d_find_mode_score()
    q1.Question1_e_find_empirical_varicance()
    print("==========================End Question 1================================\n\n")


if __name__ == "__main__":
    main()