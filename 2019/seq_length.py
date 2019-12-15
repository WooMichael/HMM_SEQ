from Bio import SeqIO
def fasta_sequence_record_generator(file_name,write_file):
    counter = 0
    for seq_record in SeqIO.parse(file_name, "fasta"):
        counter+=1
        output = seq_record.name+' '+str(len(seq_record.seq))
        with open(write_file,'a') as f1:
            f1.write(output+'\n')
fasta_sequence_record_generator('kaplan_sequences/2016/kaplan_1.fa','Seq_Length/2016/kp1.txt')
fasta_sequence_record_generator('kaplan_sequences/2016/kaplan_2.fa','Seq_Length/2016/kp2.txt')
fasta_sequence_record_generator('kaplan_sequences/2016/kaplan_3.fa','Seq_Length/2016/kp3.txt')
fasta_sequence_record_generator('kaplan_sequences/2016/kaplan_4.fa','Seq_Length/2016/kp4.txt')
fasta_sequence_record_generator('kaplan_sequences/2017/GutHK_0.fa','Seq_Length/2017/kpGutHK.txt')
fasta_sequence_record_generator('kaplan_sequences/2019/2017_1.fa','Seq_Length/2019/kp2017_1.txt')
fasta_sequence_record_generator('kaplan_sequences/2019/2018_1.fa','Seq_Length/2019/kp2018_1.txt')
fasta_sequence_record_generator('kaplan_sequences/2019/2018_2.fa','Seq_Length/2019/kp2018_2.txt')