def compare(file1,file2,write_file):
    match = 0
    diff = 0
    total_lines = 0
    with open(file1,'r') as f1,open(file2,'r') as f2:
        for l1,l2 in zip(f1,f2):
            if l1==l2:
                match +=1
                #print(l1,l2)
            else:
                diff +=1
                with open(write_file,'a') as wf:
                    wf.write(l2)
    total_lines = match + diff
    with open('Statistics.txt','a') as st:
        st.write(file2+'\n')
        st.write('Match: '+ str(match)+' ')
        st.write('Diff: '+ str(diff)+' ')
        st.write('Total: '+ str(total_lines)+'\n')

    print(match,diff,total_lines)
compare('Blake/2016/kp1.txt','Woo/2016/kp2016_1.txt','Diff/2016/kp1.txt')
compare('Blake/2016/kp2.txt','Woo/2016/kp2016_2.txt','Diff/2016/kp2.txt')
compare('Blake/2016/kp3.txt','Woo/2016/kp2016_3.txt','Diff/2016/kp3.txt')
compare('Blake/2016/kp4.txt','Woo/2016/kp2016_4.txt','Diff/2016/kp4.txt')
compare('Blake/2017/GutHK.txt','Woo/2017/kpGutHK.txt','Diff/2017/kpGutHK.txt')
compare('Blake/2019/kp2017.txt','Woo/2019/kp2017.txt','Diff/2019/kp2017_1.txt')
compare('Blake/2019/kp2018_1.txt','Woo/2019/kp2018_1.txt','Diff/2019/kp2018_1.txt')
compare('Blake/2019/kp2018_2.txt','Woo/2019/kp2018_2.txt','Diff/2019/kp2018_2.txt')