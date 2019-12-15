import re
def rmMSA(file_name,name_file,guess_file,bit_score_file):
    with open(file_name) as f1:
        for line in f1:
            line = line.split()
            name = line.__getitem__(0)
            guess = line.__getitem__(1)
            guess = re.sub('msa_', '', guess)
            bit_score = line.__getitem__(2)
            #print(line)
            with open(name_file,'a') as f2:
                f2.write(name+'\n')
            with open(guess_file, 'a') as f3:
                f3.write(guess+'\n')
            with open(bit_score_file, 'a') as f4:
                f4.write(bit_score+'\n')

def justrmMSA(file_name,write_file):
    with open(file_name) as f1:
        with open(write_file,'a') as f2:
            for line in f1:
                line = line.split()
                name = line.__getitem__(0)
                guess = line.__getitem__(1)
                guess = re.sub('msa_', '', guess)
               # bit_score = line.__getitem__(2)
                f2.write(name + ' '+ guess+ '\n')
justrmMSA('Woo/2016/kp1.txt','Woo/2016/kp2016_1.txt')
justrmMSA('Woo/2016/kp2.txt','Woo/2016/kp2016_2.txt')
justrmMSA('Woo/2016/kp3.txt','Woo/2016/kp2016_3.txt')
justrmMSA('Woo/2016/kp4.txt','Woo/2016/kp2016_4.txt')
justrmMSA('Woo/2017/GutHK.txt','Woo/2017/kpGutHK.txt')
justrmMSA('Woo/2019/kp2017.txt','Woo/2019/kp2017_1.txt')
justrmMSA('Woo/2019/kp2018_1.txt','Woo/2019/kp2018_1.txt')
justrmMSA('Woo/2019/kp2018_2.txt','Woo/2019/kp2018_2.txt')
# rmMSA('Data_Values/kp2016_1.txt','2016/Name/kp2016_1.txt','2016/Guess/kp2016_1.txt','2016/Bit_Score/kp2016_1.txt')
# rmMSA('Data_Values/kp2016_2.txt','2016/Name/kp2016_2.txt','2016/Guess/kp2016_2.txt','2016/Bit_Score/kp2016_2.txt')
# rmMSA('Data_Values/kp2016_3.txt','2016/Name/kp2016_3.txt','2016/Guess/kp2016_3.txt','2016/Bit_Score/kp2016_3.txt')
# rmMSA('Data_Values/kp2016_4.txt','2016/Name/kp2016_4.txt','2016/Guess/kp2016_4.txt','2016/Bit_Score/kp2016_4.txt')
# rmMSA('Data_Values/kpGutHK.txt','2017/Name/kpGutHK.txt','2017/Guess/kpGutHK.txt','2017/Bit_Score/kpGutHK.txt')
# rmMSA('Data_Values/kp2017_1.txt','2019_/Name/kp2017_1','2019_/Guess/kp2017_1','2019_/Bit_Score/kp2017_1')
# rmMSA('Data_Values/kp2018_1.txt','2019_/Name/kp2018_1','2019_/Guess/kp2018_1','2019_/Bit_Score/kp2018_1')
# rmMSA('Data_Values/kp2018_2.txt','2019_/Name/kp2018_2','2019_/Guess/kp2018_2','2019_/Bit_Score/kp2018_2')