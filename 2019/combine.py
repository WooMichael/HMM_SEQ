
def seq(file,file2,write_file):
    name = []
    seq_length = []
    with open(file,'r') as f1:
        for line in f1:
            line = line.split()
            id = line.__getitem__(0)
            seq = line.__getitem__(1)
            name.append(id)
            seq_length.append(seq)
    bit(file2,name,seq_length,write_file)
def combine(name,seq,bit_score,write_file):
    # while(len(name) > 0):
    #     print(name.pop(),seq.pop(),bit_score.pop())
    with open(write_file,'a') as f1:
        while(len(name) > 0):
            f1.write(name.pop()+' '+seq.pop()+' '+bit_score.pop()+'\n')
    #print(name,seq,bit_score)
def bit(file2,name,seq,write_file):
    bit_score = []
    with open(file2,'r') as f2:
        for line in f2:
            line = line.split()
            id = line.__getitem__(0)
            bit = line.__getitem__(2)
            bit_score.append(bit)
    combine(name,seq,bit_score,write_file)


seq('Seq_Length/2016/kaplan_1.txt','Data_Values/kp2016_1.txt','Combined_values/2016/kp2016_1.txt')
seq('Seq_Length/2016/kaplan_2.txt','Data_Values/kp2016_2.txt','Combined_values/2016/kp2016_2.txt')
seq('Seq_Length/2016/kaplan_3.txt','Data_Values/kp2016_3.txt','Combined_values/2016/kp2016_3.txt')
seq('Seq_Length/2016/kaplan_4.txt','Data_Values/kp2016_4.txt','Combined_values/2016/kp2016_4.txt')
seq('Seq_Length/2017/GutHK.txt','Data_Values/kpGutHK.txt','Combined_values/2017/kpGutHK.txt')
seq('Seq_Length/2019/kaplan_2017_1.txt','Data_Values/kp2017_1.txt','Combined_values/2019/kp2017_1.txt')
seq('Seq_Length/2019/kaplan_2018_1.txt','Data_Values/kp2018_1.txt','Combined_values/2019/kp2018_1.txt')
seq('Seq_Length/2019/kaplan_2018_2.txt','Data_Values/kp2018_2.txt','Combined_values/2019/kp2018_2.txt')
