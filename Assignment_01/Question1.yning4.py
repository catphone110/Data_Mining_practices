""" =================================================
    Subject:    CS 412 DATA_MINING (Fall 2017)
    Title:      Homework_1 Qestion_1
    Name:       Yayi Ning
    ================================================="""
"""====================== new learnt skills ==================
1.
    map():applies a function to all the items in an input_list. Here is the blueprint
    map(function_to_apply, list_of_inputs)
    sources: http://book.pythontips.com/en/latest/map_filter.html
    一般来说成套用的: data = list(map(int, data)) --> in python 3
2.
    from scipy.stats import mode
   ========================================================== """

""" ===================== import modules ==================== """
import numpy as np
from scipy.stats import mode
import statistics

def printAssignmentInfo():
    print("\nSubject:    CS 412 DATA_MINING (Fall 2017)")
    print("Title:      Homework_1 Qestion_1")
    print("Name:       Yayi Ning\n\n")

def Question1_a_find_max_min(scores):
    print("Question 1 (a):")
    max_score = max(scores)
    min_score = min(scores)
    print("Maximum mid-term score = ", max_score)
    print("Maximum mid-term score = ", min_score,"\n")

def Question1_b_find_quartile1_median_quartile3(scores):
    print("Question 1 (b):")
    quartile_1 = np.percentile(scores, 25)
    median = np.percentile(scores, 50)
    quartile_3 = np.percentile(scores, 75)
    print("The first quartile = ", quartile_1)
    print("The median = ", median)
    print("The third quartile = ", quartile_3, "\n")

def Question1_c_find_mean_score(scores):
    print("Question 1 (c):")
    mean = np.mean(scores)
    print("The mean = ", mean, "\n")

def Question1_d_find_mode_score(scores):
    print("Question 1 (d):")
    mode_ = mode(list(scores))[0]
    print("The mode = ", int(mode_), "\n")

def Question1_e_find_empirical_varicance(scores):
    print("Question 1 (e):")
    var = statistics.variance(scores)
    print("Empirical Variance = ", var,"\n\n")

""" ===================== main function ===================== """
def main():
    printAssignmentInfo()
#   process data.online.scores.txt file into one data "list"
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
    Question1_a_find_max_min(midterm_scores)
    Question1_b_find_quartile1_median_quartile3(midterm_scores)
    Question1_c_find_mean_score(midterm_scores)
    Question1_d_find_mode_score(midterm_scores)
    Question1_e_find_empirical_varicance(midterm_scores)
    print("==========================End Question 1================================\n\n")

#   close file here：
    data_file.close()
if __name__ == "__main__":
    main()
