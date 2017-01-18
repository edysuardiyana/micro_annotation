import source_var as src
from sklearn import tree,svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier, LogisticRegressionCV
import csv
import cPickle

FALL_FORWARD = 2
FALL_BACKWARD = 6
FALL_LEFT = 10
FALL_RIGHT = 11
FALL_BLIND_FORWARD = 12
FALL_BLIND_BACKWARD = 13

FALL_SET = set([FALL_FORWARD,
                FALL_BACKWARD,
                FALL_LEFT,
                FALL_RIGHT,
                FALL_BLIND_FORWARD,
                FALL_BLIND_BACKWARD])

def train_test(list_name):
    training_set = []
    class_training = []
    total_training_set = []
    total_class_training = []

    testing_set = []
    class_testing = []
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    Prec = 0
    Rec = 0
    Fscore = 0
    Spec = 0
    res_sequence = []


    clf = tree.DecisionTreeClassifier(random_state = 1)


    for name in list_name:
        for sub_name in list_name:
            if name == sub_name:
                testing_set, class_testing= read_file(sub_name)
            else:
                training_set, class_training, annot_training = read_file(sub_name)
                for i in range(len(training_set)):
                    total_training_set.append(training_set[i])
                    total_class_training.append(class_training[i])

        print "training and testing " + name

        clf = clf.fit(total_training_set, total_class_training)
        prediction_val = clf.predict(testing_set)
        TP, FP, TN, FN = calc_metrics(prediction_val, class_testing)
        #the case when the result is on the edge
        if TP == 0 and FP == 0:
            Prec = 0
        else:
            Prec = float(TP)/(TP+FP) * 100
        Rec = float(TP)/(TP + FN) * 100
        Fscore = float((2*TP))/((2*TP)+FP+FN) * 100
        Spec = float(TN)/(FP + TN) * 100

        result_metric = [name,TP, FP, TN, FN, Prec, Rec, Fscore, Spec]
        res_sequence.append(result_metric)


        del total_training_set[:]
        del total_class_training[:]

    return res_sequence


def calc_metrics(prediction_val, class_testing):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    Prec = 0
    Rec = 0
    Fscore = 0
    Spec = 0
    temp_val = []
    temp_annot = 0
    for i in range(len(prediction_val)):
        result = accuracy_check(prediction_val[i],class_testing[i])
        if result == 1:
            TP = TP + 1
        elif result == 2:
            FP = FP + 1
        elif result == 3:
            TN = TN + 1
        else:
            FN = FN + 1

    return TP, FP, TN, FN

def accuracy_check(final_detec_flag, annot):
    result = 0
    if annot == 1 and final_detec_flag == 1:
        #true positive
        result = 1
    elif annot == 0  and final_detec_flag == 1:
        #false positive
        result = 2
    elif annot == 0 and final_detec_flag == 0:
        #true negative
        result = 3
    else: #in Fall Set and not final_detec_flag
        #false negative
        result = 4
    return result


def read_file(name):
    path = src.source_path_features()

    data = []
    class_flag = []
    annot = []

    with open(path) as accel:
        for line in accel:
            raw_data = line.split()
            ori_data = [float(i) for i in raw_data[:len(raw_data)]]
            data.append(ori_data[0:len(ori_data)-1])
            class_flag.append(ori_data[len(ori_data)-1]) #last element
    return data, class_flag


def main():
    TP, FP, TN, FN, Prec, Rec, Fscore, Spec = train_test_nonover(["kao","musaab"])
    print TP
    print FP
    print TN
    print FN


if __name__ == '__main__':
    main()
