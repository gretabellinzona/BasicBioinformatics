# BasicBioinformatics
Basic Bioinformatics Script

## GContent.py
Compute GC content from a draft (or a complete, as well) genome. 

#### Requirements
- python > 3.0
- biopython 
- pandas 

The easiest way to install the dependencies is through conda:
```
conda install -c bioconda biopython pandas
```

### Usage 
Run python GContent.py --help to view how to run it:
```
Hi! Welcome to the help!

CGcontent.py: Computer mean GC content for a draft (or complete) sequence


	Arguments:
   -a,--assembly    : Assembly genome file (FASTA) - REQUIRED
   -h,--help        : Displays help menu
```

Compute mean GC content for a genome:
```
python GContent.py -a genome.fasta
```

This will print the output to screen:
```
genome.fasta  48.56
```

If you need to compute GC content for a batch of genomes and save to file:
```
for i in *.fasta; do python GContent.py -a $i; done > file.txt
```


