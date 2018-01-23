"""
    ** note, this is in [python 3]
    RandomForest.py
        This file build a binary classification tree on:
            multi-class
            multi-variable (multi-values with in one variables)
            use Random Forest method
    terminal command on a linus system:
    python3 decisionTree.py training-file test-file
"""
import threading
import time
import sys
import os
import copy
import random
from collections import Counter


class Node(object):
    """
    Class Node
        left -> self.attribute is found in this data
        right  -> otherwise
    """

    def __init__(self):
        """
            DATA TYPE
            type(self.decision) = str      <- tells class prediction
            type(self.attribute) = str
            type(self.rightChildren) = Node
            type(self.leftChildren) = Node
        """
        self.decision = None
        self.attribute = None
        self.rightChildren = None
        self.leftChildren = None


def gini_attribute(traindata, classnum):
    class_count = []
    for i in range(classnum):
        cc = sum([traindata[j][0] == str((i + 1)) for j in range(len(traindata))])
        value = (cc / len(traindata)) ** 2
        class_count.append(value)
    return 1 - sum(class_count)


def findBestSplit(traindata, attribute, classnum):
    """
    Function findBestSplit(): based on gini index, return a best split and divided the data
                                for two children nodes.
        :param traindata:   :type 2-D list of strings
                            training data include class
        :param attribute:   :type 1-D list of strings
                            for some attributes and its possible values
        :param classnum:    :type int
                            number of classes
        :return index:      :type string, this is the attibute being specific value: ie, '2:3'
                final_data_a, final_data_b      :type 2-D list of strings, same format as traindata
                                                divided the passed in data into either:
                                                contains this attribute being particular value/not contains
    """
    lowest_gini = float('inf')
    index = ''

    final_data_a = []  # {[traindata[i] for i in range(len(traindata)) ]}
    final_data_b = []  # the else

    for attr in attribute:
        data_a = []  # {[traindata[i] for i in range(len(traindata)) ]}
        data_b = []  # the else
        for eachdata in traindata:
            if attr in eachdata:
                data_a.append(eachdata)  # left
            else:
                data_b.append(eachdata)

        left_gini = 0
        right_gini = 0
        if len(data_a) != 0:
            left_gini = len(data_a) / len(traindata) * gini_attribute(data_a, classnum)
        if len(data_b) != 0:
            right_gini = len(data_b) / len(traindata) * gini_attribute(data_b, classnum)
        gini = left_gini + right_gini

        if gini < lowest_gini:
            lowest_gini = gini
            index = attr
            final_data_a = data_a
            final_data_b = data_b

    return index, final_data_a, final_data_b


def majorityVote(traindata, classnum):
    count = [0] * classnum
    for eachdata in traindata:
        int_class_index = int(eachdata[0]) - 1
        count[int_class_index] += 1
    for i in range(classnum):
        if count[i] == max(count):
            return str(i + 1)


def isClassUnion(traindata):
    c = traindata[0][0]
    for eachdata in traindata:
        if c != eachdata[0]:
            return False
    return True


def buildDecisionTree(traindata, attribute, classnum, max=100):
    """
    Function buildDecisionTree():
        Recursively build a binary decision tree
        :param traindata:   type:= 2-D list of string
                            training data including the actual class
        :param attribute:   type:= 1-D list of string
                            attributes left that possible to split
        :param classnum:    type:= int
                            number of classes
        :param max:         type:= int
                            upper limit of a tree splits
        :return:            type:= Node
                            root node of the decision tree

        right -> self.attribute is found in this data
        left  -> otherwise
    """

    node = Node()
    '''
    Base cases 1:
        no data left 
        should return NULL
    '''
    if len(traindata) == 0:
        node.decision = '1'
        return node

    '''
    Base cases 2:
        no attributes left
        use majority vote
    '''
    if len(attribute) == 0:
        node.decision = majorityVote(traindata, classnum)
        return node

    '''
    Base cases 3:
        classes are united
    '''
    if isClassUnion(traindata):
        node.decision = traindata[0][0]
        return node
    '''
    Base cases 4:
        Max are used up
        use majority vote
    '''
    if max < 1:
        node.decision = majorityVote(traindata, classnum)
        return node

    node.rightChildren = None  # rightChildren
    node.leftChildren = None  # leftChildren

    attr, data_a, data_b = findBestSplit(traindata, attribute, classnum)

    attribute_right = copy.deepcopy(attribute)
    attribute_right.remove(attr)
    attribute_left = [x for x in attribute if attr[0:2] not in x]

    node.attribute = attr
    node.leftChildren = buildDecisionTree(data_a, attribute_left, classnum)  # leftChildren
    node.rightChildren = buildDecisionTree(data_b, attribute_right, classnum)  # leftChildren

    return node


def predict(root, data_i):
    node = root
    # print(data_i)
    while node.decision == None:
        # print("node.attribute", node.attribute)
        # print("data will go: ", )
        if node.attribute in data_i:
            node = node.leftChildren
        else:
            node = node.rightChildren

    # print("predicted as ==, ", node.decision)
    return node.decision


def getClassNum(data):
    libirary = []
    for data_i in data:
        libirary.append(data_i[0])
    libirary = list(set(libirary))
    return len(libirary)

def getAttributes(data):
    libirary = []
    for data_i in data:
        for i in range(1, len(data_i)):
            libirary.append(data_i[i])
    # print("Libirary", libirary)
    libirary = list(set(libirary))
    # print("attibutes from libirary = ", libirary)
    # print("len attibutes", len(libirary))
    return libirary


def predictAll(test, root):
    acc = 0
    predicted = []

    for data_i in test:
        y_i = predict(root, data_i)
        if int(data_i[0]) == int(y_i):
            acc += 1
        predicted.append(y_i)
    return predicted, acc / len(test)


def confusionMatrixPrint(actual, predictions, classnum):
    matrix = []
    for i in range(classnum):
        matrix.append([0] * classnum)

    for i in range(len(actual)):
        matrix[int(actual[i]) - 1][int(predictions[i]) - 1] += 1

    for i in range(classnum):
        line = ''
        for j in range(classnum):
            line += str(matrix[i][j]) + ' '
        print(line)


def random_data(data, want_len):
    data_copy = copy.deepcopy(data)
    for i in range(len(data) - want_len):
        data_copy.remove(random.choice(data_copy))
    return data_copy


def majorityVotePrediction(predictions):
    final_decision = []
    for i in range(len(predictions[0])):
        x = [predictions[j][i] for j in range(len(predictions))]
        x = Counter(x).most_common()
        final_decision.append(x[0][0])
    # print(final_decision)
    return final_decision


"""
def largeAattiDataPrune(data, lamda):
"""

lock = threading.Lock()
PREDICTIONS = []


class myThread(threading.Thread):
    def __init__(self, threadId, num_class, data, test, ALPHA):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.num_class = num_class
        self.data = data
        self.test = test
        self.ALPHA = ALPHA
        #self.workLoad = workLoad

    def run(self):
        #print("in thread workimng function have, thread id = ", self.threadId)
        pred_list = []

        attributes = getAttributes(self.data)
        attri_prune = random_data(attributes, int(len(attributes) * self.ALPHA))
        root = buildDecisionTree(self.data, attri_prune, self.num_class, 100)
        predictions, accuracy = predictAll(self.test, root)
        pred_list.append(predictions)
        #print("got prediction, id == ", self.threadId)

        #print("wait for lock>>>>>>>>>>>>")
        lock.acquire()
        #print("get lock   !")
        PREDICTIONS.append(pred_list[0])
        #print("Return lock")
        lock.release()


def main():
    NUM_THREAD = 20
    lamda = 0.4
    threadlist = []

    '''
    python3 RandomForest.py synthetic.social.train synthetic.social.test
    python3 RandomForest.py balance.scale.train balance.scale.test
    python3 RandomForest.py nursery.train nursery.test
    python3 RandomForest.py led.train led.test

    argv2 = 'balance.scale.train'
    argv3 = 'balance.scale.test'

    argv2 = 'nursery.train'
    argv3 = 'nursery.test'

    argv2 = 'led.train'
    argv3 = 'led.test'

    argv2 = 'synthetic.social.train'
    argv3 = 'synthetic.social.test'

    '''

    if len(sys.argv) != 3:
        print("Incorrect input format. [python RandomForest.py train_file test_file]")
        return

    argv2 = sys.argv[1]
    argv3 = sys.argv[2]

    dir = os.path.dirname(__file__)
    trainfile_path = os.path.join(dir, argv2)
    testfile_path = os.path.join(dir, argv3)
    trainfile = open(trainfile_path, 'r')
    testfile = open(testfile_path, 'r')
    train_lines = trainfile.readlines()
    test_lines = testfile.readlines()
    data = []
    test = []
    for eachLine in train_lines:
        data.append(eachLine.split())

    for eachLine in test_lines:
        test.append(eachLine.split())

    classnum = getClassNum(data)
    ALPHA = 1
    if 'balance.scale' in argv2:
        NUM_TREE  = 50
        NUM_THREAD = 50
        lamda = 0.1
        #classnum = 3

    if 'nursery' in argv2:
        NUM_TREE = 10
        NUM_THREAD = 10
        lamda = 0.6
        #classnum = 5

    if 'led' in argv2:
        NUM_TREE = 50
        NUM_THREAD = 50
        lamda = 0.5
        #classnum = 2

    if 'synthetic.social' in argv2:
        #classnum = 4

        ALPHA = 0.2 # prune attribute for time efficiency
        NUM_THREAD = 100
        lamda = 0.1

        """
        for acc = 0.6 somethong:

        ALPHA =  0.2
        NUM_THREAD =  30
        lamda =  0.1
        """

        #print("Parameters = ")
        #print("   ALPHA = ", ALPHA)
        #print("   NUM_THREAD = ", NUM_THREAD)
        #print("   lamda = ", lamda)

    datalist = []
    eachLength = int(len(data) * lamda)

    for i in range(NUM_THREAD):
        datalist.append(random_data(data, eachLength))

    # print(datalist[2])

    for i in range(NUM_THREAD):
        thread = myThread(i, classnum, datalist[i], test, ALPHA)
        thread.start()
        threadlist.append(thread)

    for t in threadlist:
        t.join()
    #print("jointed")

    actual = [test[i][0] for i in range(len(test))]
    final_predictions = majorityVotePrediction(PREDICTIONS)

    confusionMatrixPrint(actual, final_predictions, classnum)

    acc = sum([final_predictions[i] == actual[i] for i in range(len(actual))])
    #print("total accuracy =  ", acc / len(actual))


if __name__ == "__main__":
    start_time = time.time()
    main()
    #print("Time used  = %s seconds " % (time.time() - start_time))