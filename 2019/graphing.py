from matplotlib import pyplot as plt
import numpy as np


def plot(file1,file2,plot_title):
    list_bit_score = []
    list_seq_length = []
    list_bit_score_no_match = []
    list_seq_length_no_match = []

    with open(file1,"r") as f1:

        for line in f1:
            line = line.split()
            #name = line.__getitem__(0)
            seq_length = line.__getitem__(1)
            bit_score = line.__getitem__(2)
            list_bit_score.append(bit_score)
            list_seq_length.append(seq_length)
        print(list_seq_length,list_bit_score)
    with open(file2,'r') as f2:
        for line in f2:
            line = line.split()
            #name = line.__getitem__(0)
            seq_length = line.__getitem__(1)
            bit_score = line.__getitem__(2)
            list_bit_score_no_match.append(bit_score)
            list_seq_length_no_match.append(seq_length)
    createplot(list_seq_length,list_bit_score,list_seq_length_no_match,list_bit_score_no_match,plot_title)


def createplot(arr1,arr2,arr3,arr4,plot_title):
    list_seq_length = np.asfarray(arr1,float)
    list_bit_score = np.asfarray(arr2,float)
    list_seq_length_no_match = np.asfarray(arr3,float)
    list_bit_score_no_match = np.asfarray(arr4,float)

    print(list_seq_length)
    print(list_bit_score)
    plt.scatter(list_bit_score,list_seq_length,c='blue')
    plt.scatter(list_bit_score_no_match,list_seq_length_no_match,c='red')

    plt.title(plot_title)
    plt.xlabel("Bit Score")
    plt.ylabel("Sequence Length")
    #plt.savefig(plot_title+'.png',dpi=125)
    plt.show()
def plot100(file1,plot_title):
    with open(file1,"r") as f1:
        list_seq_length = []
        list_bit_score = []
        for line in f1:
            line = line.split()
            name = line.__getitem__(0)
            seq_length = line.__getitem__(1)
            bit_score = line.__getitem__(2)
            list_bit_score.append(bit_score)
            list_seq_length.append(seq_length)
        list_seq_length = np.asfarray(list_seq_length, float)
        list_bit_score = np.asfarray(list_bit_score, float)
    plt.scatter(list_bit_score, list_seq_length, c='blue')
    plt.title(plot_title)
    plt.xlabel("Bit Score")
    plt.ylabel("Sequence Length")
    #plt.savefig(plot_title+'.png', dpi=125)
    plt.show()


plot('Combined_values/2016/kp2016_1.txt','Diff_values/2016/kp2016_1.txt','2016_1')
plot('Combined_values/2016/kp2016_2.txt','Diff_values/2016/kp2016_2.txt','2016_2')
plot('Combined_values/2016/kp2016_3.txt','Diff_values/2016/kp2016_3.txt','2016_3')
plot('Combined_values/2016/kp2016_4.txt','Diff_values/2016/kp2016_4.txt','2016_4')
plot100('Combined_values/2017/kpGutHK.txt','2017_GUT')
plot('Combined_values/2019/kp2017_1.txt','Diff_values/2019/kp2017_1.txt','2017_1')
plot('Combined_values/2019/kp2018_1.txt','Diff_values/2019/kp2018_1.txt','2018_1')
plot('Combined_values/2019/kp2018_2.txt','Diff_values/2019/kp2018_2.txt','2018_2')

