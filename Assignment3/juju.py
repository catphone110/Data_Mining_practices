import numpy as np
import itertools
import math


def check_single(pattern, sequence, epslion):
    min_dis = float('inf')
    for j in range(len(sequence)):
        for k in range(len(sequence), j, -1):
            if set(pattern).issubset(set(sequence[j:k + 1])) and min_dis > (k - j + 1):
                min_dis = (k - j) + 1
                # print("min_dis", min_dis, "pattern", pattern, "sequence", sequence)
                if min_dis <= math.floor(epslion * len(pattern)) + len(pattern):
                    return True  # found
    return False


def minLenSatisfy(pattern, sequences, epslion, theta):
    count = 0
    for i in range(len(sequences)):
        if set(pattern).issubset(set(sequences[i])):
            if check_single(pattern, sequences[i], epslion):
                count += 1
            if checkFrequent(count, theta, sequences):
                return True
    if not checkFrequent(count, theta, sequences):
        return False
    return True


def isFrequent(pattern, sequences, theta):
    count = 0
    for i in range(len(sequences)):
        if set(pattern).issubset(set(sequences[i])):
            count += 1
    return count >= math.ceil(theta * len(sequences))


def checkFrequent(count, theta, sequences):
    return count >= math.ceil(theta * len(sequences))


def  getSeq(data):
    seq = []
    for i in range(1, len(data)):
        s = list(map(int, data[i]))
        seq.append(s)
    return seq

def processData(f):
    file = f.readlines()
    ret = []
    for l in file:
        text = l.replace(',', '')
        ret.append(text.split())
    ret = np.array(ret)
    return ret


def writeToFile(source, output):
    f1 = open(source, 'r')
    f2 = open(output, 'w')
    data = processData(f1)
    a = list(map(float, data[0]))[0]
    b = list(map(float, data[0]))[1]
    seq = getSeq(data)
    return f2, [[a, b], seq]

def main():
    '''
    data_file = open("data.txt", 'r')
    out_file = open("ynig4-HW3.txt", 'w')

    data_file = open("test_500.txt", 'r')
    out_file = open("500_output.txt", 'w')

    data_file = open("test_1000.txt", 'r')
    out_file = open("1000_output.txt", 'w')
    '''
    source = "data.txt"
    out_file = "juju_HW3.txt"
    # 原来的sequence就是 data[1]
    # 原来的theda = data[0][0]
    # 原来的ecliposon = data[0][1]
    f2, data = writeToFile(source, out_file)
    print(data[1])
    item = []
    for i in range(len(data[1])):
        for j in data[1][i]:
            if not j in (item):
                item.append(j)
    for i in item:
        count = 0
        for h in range(len(data[1])):
            if set([i]).issubset(set(data[1][h])):
                count += 1
        if count >= math.ceil(data[0][0] * len(data[1])):
            f2.write(str(i) + '\n')
    for l in range(2, len(item)):
        for subset in itertools.combinations(item, l):
            count = 0
            for h in range(len(data[1])):
                if set(subset).issubset(set(data[1][h])):
                    count += 1
            if count >= math.ceil(data[0][0] * len(data[1])):
                if minLenSatisfy(subset, data[1], data[0][1], data[0][0]):
                    f2.write((str(subset) + '\n').replace('(', '').replace(')', ''))






if __name__ == "__main__":
    main()