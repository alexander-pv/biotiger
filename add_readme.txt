
My fixed version of the code:

1. This repo uses python2.7

2. Install conda environment for the repo from environment.yml file:
   $ conda env create -f environment.yml 

3. Run pytest on test folder:
   $ pytest ./tests

4.Run program
$ python tiger.py index -i issidae.fasta -s 2 -o output_seq -u ?,-,N
By default, files will be stored to a new outputs folder.

$ python tiger.py rate -i outputs/output_seq.0.ti -r outputs/output_seq.ref.ti -rl rate_list

$ python tiger.py output -i outputs/output_seq.0.gr -fa issidae.fasta -o output_fasta -exc 1,2,9,10 -b 10 --mask

Create NEXUS file:
$ python tiger.py output -i outputs/output_seq.0.gr -fa issidae.fasta -f 3 -o output_nexus


