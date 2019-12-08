from Bio import SeqIO
# Input: this function takes in a single file of fasta sequences,
# Output: Generate a single file of a single fasta sequence
def fasta_sequence_seperator(file_name,write_file_directory):
    counter = 0
    for seq_record in SeqIO.parse(file_name, "fasta"):
        counter+=1
        #from this information we can get the id, sequence, and length of sequence
        #print(seq_record.name, seq_record.seq, len(seq_record.seq))
        print(seq_record)
        with open(write_file_directory + '/' + seq_record.name + '.fa', 'a') as file:
            SeqIO.write(seq_record, file, "fasta", )


fasta_sequence_seperator('01_kaplan_sequences/2016/kaplan_1.fa','kaplan_sequences_individual_sequences/2016/kaplan_1')
fasta_sequence_seperator('01_kaplan_sequences/2016/kaplan_2.fa','kaplan_sequences_individual_sequences/2016/kaplan_2')
fasta_sequence_seperator('01_kaplan_sequences/2016/kaplan_3.fa','kaplan_sequences_individual_sequences/2016/kaplan_3')
fasta_sequence_seperator('01_kaplan_sequences/2016/kaplan_4.fa','kaplan_sequences_individual_sequences/2016/kaplan_4')
fasta_sequence_seperator('01_kaplan_sequences/2017/GutHK_0.fa','kaplan_sequences_individual_sequences/2017/GutHK_0')
fasta_sequence_seperator('01_kaplan_sequences/2019/2017_1.fa','kaplan_sequences_individual_sequences/2019/2017_1')
fasta_sequence_seperator('01_kaplan_sequences/2019/2018_1.fa','kaplan_sequences_individual_sequences/2019/2018_1')
fasta_sequence_seperator('01_kaplan_sequences/2019/2018_2.fa','kaplan_sequences_individual_sequences/2019/2018_2')

