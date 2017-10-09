import csv
import pandas
import numpy as np
from copy import deepcopy


def main():
    print("\nSubject:    CS 412 DATA_MINING (Fall 2017)")
    print("Title:      Homework_2 Qestion_3")
    print("Name:       Yayi Ning\n\n")

    file = open('Q3data.txt', 'r')
    lines = file.readlines()
    data = []

    for eachline in lines:
        data.append(eachline.split())
    data = np.array(data)
    # print(data.shape)
    # print(data[0])
    possible_pattern_len1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    pp_len1_count = np.zeros(len(possible_pattern_len1))
    possible_pattern_len2 = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['A', 'E'], ['A', 'F'], ['A', 'G'],
                             ['B', 'C'], ['B', 'D'], ['B', 'E'], ['B', 'F'], ['B', 'G'],
                             ['C', 'D'], ['C', 'E'], ['C', 'F'], ['C', 'G'],
                             ['D', 'E'], ['D', 'F'], ['D', 'G'],
                             ['E', 'F'], ['E', 'G'],
                             ['F', 'G']]
    pp_len2_count = np.zeros(len(possible_pattern_len2))

    possible_pattern_len3 = [['A', 'B', 'C'], ['A', 'B', 'D'], ['A', 'B', 'E'], ['A', 'B', 'F'], ['A', 'B', 'G'],
                             ['A', 'C', 'D'], ['A', 'C', 'E'], ['A', 'C', 'F'], ['A', 'C', 'G'],
                             ['A', 'D', 'E'], ['A', 'D', 'F'], ['A', 'D', 'G'],
                             ['A', 'E', 'F'], ['A', 'E', 'G'],
                             ['A', 'F', 'G'],

                             ['B', 'C', 'D'], ['B', 'C', 'E'], ['B', 'C', 'F'], ['B', 'C', 'G'],
                             ['B', 'D', 'E'], ['B', 'D', 'F'], ['B', 'D', 'G'],
                             ['B', 'E', 'F'], ['B', 'E', 'G'],
                             ['B', 'F', 'G'],

                             ['C', 'D', 'E'], ['C', 'D', 'F'], ['C', 'D', 'G'],
                             ['C', 'E', 'F'], ['C', 'E', 'G'],
                             ['C', 'F', 'G'],

                             ['D', 'E', 'F'], ['D', 'E', 'G'],
                             ['D', 'F', 'G'],

                             ['E', 'F', 'G']]
    pp_len3_count = np.zeros(len(possible_pattern_len3))

    possible_pattern_len4 = [['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'E'], ['A', 'B', 'C', 'F'], ['A', 'B', 'C', 'G'],
                             ['A', 'B', 'D', 'E'], ['A', 'B', 'D', 'F'], ['A', 'B', 'D', 'G'],
                             ['A', 'B', 'E', 'F'], ['A', 'B', 'E', 'G'],
                             ['A', 'B', 'F', 'G'],

                             ['A', 'C', 'D', 'E'], ['A', 'C', 'D', 'F'], ['A', 'C', 'D', 'G'],
                             ['A', 'C', 'E', 'F'], ['A', 'C', 'E', 'G'],
                             ['A', 'C', 'F', 'G'],

                             ['A', 'D', 'E', 'F'], ['A', 'D', 'E', 'G'],
                             ['A', 'D', 'E', 'G'],

                             ['A', 'E', 'F', 'G'],

                             ['B', 'C', 'D', 'E'], ['B', 'C', 'D', 'F'], ['B', 'C', 'D', 'G'],
                             ['B', 'C', 'E', 'F'], ['B', 'C', 'E', 'G'],
                             ['B', 'C', 'F', 'G'],

                             ['C', 'D', 'E', 'F'], ['C', 'E', 'F', 'G'],
                             ['D', 'E', 'F', 'G']]

    pp_len4_count = np.zeros(len(possible_pattern_len4))

    possible_pattern_len5 = [['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'C', 'D', 'F'], ['A', 'B', 'C', 'E', 'F'],
                             ['A', 'B', 'D', 'E', 'F'], ['A', 'C', 'D', 'E', 'F'], ['B', 'C', 'D', 'E', 'F'],

                             ['A', 'B', 'C', 'D', 'G'], ['A', 'B', 'C', 'E', 'G'], ['A', 'B', 'D', 'E', 'G'],
                             ['A', 'C', 'D', 'E', 'G'], ['B', 'C', 'D', 'E', 'G'],

                             ['A', 'B', 'C', 'F', 'G'], ['A', 'B', 'D', 'F', 'G'], ['A', 'C', 'D', 'F', 'G'],
                             ['B', 'C', 'D', 'F', 'G'],

                             ['A', 'B', 'E', 'F', 'G'], ['A', 'C', 'E', 'F', 'G'], ['B', 'C', 'E', 'F', 'G'],

                             ['A', 'D', 'E', 'F', 'G'], ['B', 'D', 'E', 'F', 'G'],

                             ['C', 'D', 'E', 'F', 'G']]

    pp_len5_count = np.zeros(len(possible_pattern_len5))

    possible_pattern_len6 = [['B', 'C', 'D', 'E', 'F', 'G'],
                             ['A', 'C', 'D', 'E', 'F', 'G'],
                             ['A', 'B', 'D', 'E', 'F', 'G'],
                             ['A', 'B', 'C', 'E', 'F', 'G'],
                             ['A', 'B', 'C', 'D', 'F', 'G'],
                             ['A', 'B', 'C', 'D', 'E', 'G'],
                                ['A', 'B', 'C', 'D', 'E', 'F']]

    pp_len6_count = np.zeros(len(possible_pattern_len6))

    possible_pattern_len7 = [['A', 'B', 'C', 'D', 'E', 'F', 'G']]
    pp_len7_count = np.zeros(len(possible_pattern_len7))
    # ___________________________________________________________________________________________________________
    # also can done by take advantage of subset:
    """
    pp_7 = set(possible_pattern_len2[0])
    data_test = ['A', 'B', 'C', 'F', 'G']
    print("pp_7",pp_7)
    print("pp_7", pp_7.issubset(data_test))
    """
    for i in range(len(possible_pattern_len1)):
        for d in range(len(data)):
            if all(item in data[d] for item in possible_pattern_len1[i]):
                pp_len1_count[i] = pp_len1_count[i] + 1
    # print(pp_len1_count)

    for i in range(len(possible_pattern_len2)):
        for d in range(len(data)):
            if all(item in data[d] for item in possible_pattern_len2[i]):
                pp_len2_count[i] = pp_len2_count[i] + 1
    # print(pp_len2_count)

    for i in range(len(possible_pattern_len3)):
        for d in range(len(data)):
            if all(item in data[d] for item in possible_pattern_len3[i]):
                pp_len3_count[i] = pp_len3_count[i] + 1
    # print(pp_len3_count)

    for i in range(len(possible_pattern_len4)):
        for d in range(len(data)):
            if all(item in data[d] for item in possible_pattern_len4[i]):
                pp_len4_count[i] = pp_len4_count[i] + 1
    # print(pp_len4_count)

    for i in range(len(possible_pattern_len5)):
        for d in range(len(data)):
            if all(item in data[d] for item in possible_pattern_len5[i]):
                pp_len5_count[i] = pp_len5_count[i] + 1
    # print(pp_len5_count)

    for i in range(len(possible_pattern_len6)):
        for d in range(len(data)):
            if all(item in data[d] for item in possible_pattern_len6[i]):
                pp_len6_count[i] = pp_len6_count[i] + 1
    # print(pp_len6_count)

    for i in range(len(possible_pattern_len7)):
        for d in range(len(data)):
            if all(item in data[d] for item in possible_pattern_len7):
                pp_len7_count[i] = pp_len7_count[i] + 1
    # print(pp_len7_count)
    print("possible_pattern_len2[8]", possible_pattern_len2[8])
    print("data[1]", data[1])

    print("this", all(item in data[1] for item in possible_pattern_len2[8]))

    print("==============================================================================")
    print("Q3.a: Suppose the minimum support is 20")
    print("==============================================================================")

    print("______________________________________________________________________________")
    print("(a.1)\n")
    count_f20 = sum(pp_len1_count >= 20) + sum(pp_len2_count >= 20) + \
                sum(pp_len3_count >= 20) + sum(pp_len4_count >= 20) + \
                sum(pp_len5_count >= 20) + sum(pp_len6_count >= 20) + \
                sum(pp_len7_count >= 20)

    print("The number of frequent patterns is count_f20 = ", count_f20, "\n\n")

    print("______________________________________________________________________________")
    print("(a.2)\n")
    count_f_len3_20 = sum(pp_len3_count >= 20)
    print("The number of frequent patterns with length 3 is count_f_len3_20 = ", count_f_len3_20, "\n\n")

    print("______________________________________________________________________________")
    print("(a.3)\n")
    print("Firstly get all the pattens that frequency exceed 20 in one max_patter_f20 array.")
    print("Secondly from short length to long length check whether each patter is included in latter longer patter.")
    print("If so, removed it from max_patter_f20 array.")
    patterns = [possible_pattern_len1,
                possible_pattern_len2,
                possible_pattern_len3,
                possible_pattern_len4,
                possible_pattern_len5,
                possible_pattern_len6,
                possible_pattern_len7]
    patterns_f20 = []
    frequency = [pp_len1_count,
                 pp_len2_count,
                 pp_len3_count,
                 pp_len4_count,
                 pp_len5_count,
                 pp_len6_count,
                 pp_len7_count]

    for i in range(len(frequency)):
        for j in range(len(frequency[i])):
            if frequency[i][j] >= 20:
                patterns_f20.append(patterns[i][j])
    # print(patterns_f20)
    # print(len(patterns_f20))
    max_patterns_f20 = deepcopy(patterns_f20)
    for i in range(len(patterns_f20)):
        pattern_i = patterns_f20[i]
        for j in range(i + 1, len(patterns_f20)):
            pattern_big = patterns_f20[j]
            if (len(pattern_i) < len(pattern_big)) and set(pattern_i).issubset(pattern_big):
                # print("need removed", pattern_i)
                max_patterns_f20.remove(pattern_i)
                break
    print("Now we have max_patterns_f20 = \n            ", max_patterns_f20, "\n")
    print("Thus, number of max patterns = len(max_patterns_f20) = ", len(max_patterns_f20), "\n\n")

    print("==============================================================================")
    print("Q3.b: Suppose the minimum support is 10")
    print("==============================================================================")
    print("______________________________________________________________________________")
    print("(b.1)\n")
    count_f10 = sum(pp_len1_count >= 10) + sum(pp_len2_count >= 10) + \
                sum(pp_len3_count >= 10) + sum(pp_len4_count >= 10) + \
                sum(pp_len5_count >= 10) + sum(pp_len6_count >= 10) + \
                sum(pp_len7_count >= 10)
    print("The number of frequent patterns is count_f10 = ", count_f10, "\n\n")

    print("______________________________________________________________________________")
    print("(b.2)\n")
    count_f_len3_10 = sum(pp_len3_count >= 10)
    print("The number of frequent patterns with length 3 is count_f_len3_10 = ", count_f_len3_10, "\n\n")
    print("______________________________________________________________________________")
    print("(b.3)\n")
    print("Firstly get all the pattens that frequency exceed 10 in one max_patter_f10 array.")
    print("Secondly from short length to long length check whether each patter is included in latter longer patter.")
    print("If so, removed it from max_patter_f10 array.")
    patterns_f10 = []

    for i in range(len(frequency)):
        for j in range(len(frequency[i])):
            if frequency[i][j] >= 10:
                patterns_f10.append(patterns[i][j])
    # print(len(patterns_f10), count_f10)
    max_patterns_f10 = deepcopy(patterns_f10)
    for i in range(len(patterns_f10)):
        pattern_i = patterns_f10[i]
        for j in range(i + 1, len(patterns_f10)):
            pattern_big = patterns_f10[j]
            if (len(pattern_i) < len(pattern_big)) and set(pattern_i).issubset(pattern_big):
                max_patterns_f10.remove(pattern_i)
                break
    print("Now we have max_patterns_f10 = \n            ", max_patterns_f10, "\n")
    print("Thus, number of max patterns = len(max_patterns_f10) = ", len(max_patterns_f10), "\n\n")

    print("______________________________________________________________________________")
    print("(b.4)\n")
    # association rule (C, E) -> A
    print("Associate support (C, E) -> A = support(C, E) and (A)) / support(C, E)")
    support_ace = 0
    support_ce = 0
    for i in range(len(data)):
        if {'A', 'C', 'E'}.issubset(data[i]):
            support_ace += 1
        if {'C', 'E'}.issubset(data[i]):
            support_ce += 1
    print("                  = ", support_ace, " / ", support_ce)
    print("                  = ", support_ace / support_ce)

    print("______________________________________________________________________________")
    print("(b.5)\n")
    # association rule (A, B, C) -> E
    print("Associate support (A, B, C) -> E = support(A, B, C) and (E)) / support(A, B, C)")
    support_abce = 0
    support_abc = 0
    for i in range(len(data)):
        if {'A', 'B', 'C', 'E'}.issubset(data[i]):
            support_abce += 1
        if {'A', 'B', 'C'}.issubset(data[i]):
            support_abc += 1
    print("                  = ", support_abce, " / ", support_abc)
    print("                  = ", support_abce / support_abc)


if __name__ == "__main__":
    main()
