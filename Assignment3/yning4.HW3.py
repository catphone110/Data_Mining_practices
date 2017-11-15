import numpy as np
import itertools
import math

def check_single(pattern, sequence, epslion):
    min_dis = float('inf')
    for j in range(len(sequence)):
        for k in range(len(sequence), j, -1):
            if set(pattern).issubset(set(sequence[j:k+1])) and min_dis > (k - j + 1):
                min_dis = (k - j) + 1
                # print("min_dis", min_dis, "pattern", pattern, "sequence", sequence)
                if min_dis <= math.floor(epslion*len(pattern))+len(pattern):
                    return True  # found
    return False


def minLenSatisfy(pattern, sequences, epslion, theta):
    count = 0
    for i in range(len(sequences)):
        chance = math.floor(epslion*len(pattern))
        if set(pattern).issubset(set(sequences[i])):
            if check_single(pattern, sequences[i], epslion):
                count += 1
            if checkFrequent(count, theta, sequences):
                return True
            '''
            min_dis = int(math.inf)
            for j in range(len(sequences[i])):
                for k in range(len(sequences[i]), j, -1):
                    if set(pattern).issubset(set(sequences[i][j:k])) and min_dis > (j-k):
                        min_dis = (j-k)
                        print("min_dis", min_dis, "pattern", pattern, "sequences[i]", sequences[i])
                        if 
            '''
    if not checkFrequent(count, theta, sequences):
        return False
    return True

def isFrequent(pattern, sequences, theta):
    count = 0
    for i in range(len(sequences)):
        if set(pattern).issubset(set(sequences[i])):
            count += 1
    return count >= math.ceil(theta*len(sequences))


def checkFrequent(count, theta, sequences):
    return count >= math.ceil(theta*len(sequences))


def getSingleton(sequences):
    singleton = []
    for i in range(len(sequences)):
        for j in sequences[i]:
            if not j in (singleton):
                singleton.append(j)
    return singleton


def main():

    print("main:")
    '''
    data_file = open("data.txt", 'r')
    out_file = open("ynig4-HW3.txt", 'w')

    data_file = open("test_500.txt", 'r')
    out_file = open("500_output.txt", 'w')
    
    data_file = open("test_1000.txt", 'r')
    out_file = open("1000_output.txt", 'w')
    '''

    data_file = open("data.txt", 'r')
    out_file = open("ynig4-HW3.txt", 'w')

    lines = data_file.readlines()
    data = []
    for eachLine in lines:
        data.append(eachLine.replace(',', '').split())
    data = np.array(data)
    sequences = []
    parameters = list(map(float,data[0]))
    theta = parameters[0]
    epslion = parameters[1]
    for i in range(1, len(lines)):
        si = data[i]
        si = list(map(int, si))
        sequences.append(si)
    data_file.close()

    singleton = getSingleton(sequences)
    # singleton = [1,2,4,5,6]
    print("singleton", singleton)
    for i in singleton:
        if isFrequent([i], sequences, theta):
            out_file.write(str(i)+'\n')
    for l in range(2, len(singleton)):
        for subset in itertools.combinations(singleton, l):
            if isFrequent(subset, sequences, theta):
                # print("in iside of isFrequent， subset = ", subset)
                if minLenSatisfy(subset, sequences, epslion, theta):
                    # print("inside minLenSatisfy, epslion = ", epslion, "subset = ", subset)
                    out_file.write((str(subset)+'\n').replace('(', '').replace(')', ''))

if __name__ == "__main__":
    main()