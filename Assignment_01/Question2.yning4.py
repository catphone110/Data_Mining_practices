import numpy as np
from scipy.stats import mode
import statistics

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


class Question1():
    def __init__(self, scores):
        self.scores = scores

    """
    print("\nSubject:    CS 412 DATA_MINING (Fall 2017)")
    print("Title:      Homework_1 Qestion_1")
    print("Name:       Yayi Ning\n\n") 
    """

    def q1_get_max_min_scores(self):
        max_score = max(self.scores)
        min_score = min(self.scores)
        return max_score, min_score

    def q1_get_median(self):
        quartile_1 = np.percentile(self.scores, 25)
        median = np.percentile(self.scores, 50)
        quartile_3 = np.percentile(self.scores, 75)
        return quartile_1, median, quartile_3

    def q1_get_mean(self):
        mean = np.mean(self.scores)
        return mean

    def Question1_d_find_mode_score(self):
        freqs = groupby(Counter(self.scores).most_common(), lambda x: x[1])
        # pick the first group (highest frequency)
        mode_ = [val for val, count in next(freqs)[1]]
        return mode_

    def q1_get_variance(self):
        var = statistics.variance(self.scores)
        return var


class Question2():
    def __init__(self, scores):
        self.scores = scores

#   print("\nSubject:    CS 412 DATA_MINING (Fall 2017)")
    print("Title:      Homework_1 Qestion_2")
    print("Name:       Yayi Ning\n\n")

    def z_normolization(self, mean, var):
        z_scores = (self.scores - mean)/(var)**0.5
        # print("Scores after z_score normalization :", z_scores)
        return z_scores

    def compare_variances(self, z_scores, var):
        print("Question 2 (a):")
        var_norm = statistics.variance(z_scores)
        print("Variance before normalization:", var)
        print("Variance after normalization:", var_norm, "\n\n")
        return var_norm

    def normalize_90(self, mean, var):
        print("Question 2 (b):")
        normalized_90 = (90-mean)/var**0.5
        print("Score of 90 after normalization:", normalized_90, "\n\n")

    def correlation_final_midterm(self, midterm, final):
        print("Question 2 (c):")
        corr_coeff = np.corrcoef(midterm, final)[0, 1]
        print("Person's correlation coefficient between midterm scores and final scores is: ", corr_coeff,"\n\n")

    def covariance_final_midterm(self, midterm, final):
        print("Question 2 (d):")
        covariance = np.cov(midterm, final)[0, 1]
        print("The covariance between midterm and final is:", covariance, "\n\n")
        return covariance


""" ===================== main function ===================== """
def main():
    data = Data()
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
    print("==========================End Question 2================================\n\n")


if __name__ == "__main__":
    main()